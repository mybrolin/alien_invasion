#
# 方法工具类
#
import pygame
import sys
import time

from bullet import Bullet
from alien import Alien
import log
from settings import Settings


def update_bullets(ai_game):
    """更新子弹信息"""
    # 子弹实时更新
    ai_game.bullets.update()
    # 销毁屏幕外的子弹
    _destory_bullet(ai_game)

    # 监听碰撞
    _check_bullet_alien_collisions(ai_game)


def _check_bullet_alien_collisions(ai_game):
    """
    监听子弹与外星人的碰撞
    如果碰撞，子弹和外星人都消失
    如果外星人都消失了，重新生成，如此循环三次
    """
    collisions = pygame.sprite.groupcollide(ai_game.bullets, ai_game.aliens, not ai_game.settings.bullets_super, True)

    log.info(collisions.values())
    # 记分
    for aliens in collisions.values():
        ai_game.gameStatus.hit_aliens(len(aliens))

    # 外星人都打光了，结束游戏
    if not ai_game.aliens and ai_game.settings.alien_reset_times == 0:
        ai_game.gameStatus.shut_down()

    # 一波外星人来袭制止，制造下一波
    setting = Settings()
    if not ai_game.aliens and ai_game.settings.alien_reset_times > 0:
        part_reset_game(ai_game)
        ai_game.settings.alien_reset_times -= 1

        # 提升等级
        ai_game.settings.alien_x_speen = setting.alien_x_speen * (
                1 + setting.alien_reset_times - ai_game.settings.alien_reset_times)
        ai_game.settings.ship_speed = setting.ship_speed * (
                1 + setting.alien_reset_times - ai_game.settings.alien_reset_times)
        ai_game.settings.bullet_speed = setting.bullet_speed * (
                1 + setting.alien_reset_times - ai_game.settings.alien_reset_times)


def _fire_bullet(ai_game):
    """发射子弹 在允许最大子弹数的范围内创建"""
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed and ai_game.gameStatus.is_alive():
        ai_game.bullets.add(Bullet(ai_game))


def _destory_bullet(ai_game):
    """消除屏幕外的子弹"""
    for bullet in ai_game.bullets.copy():
        if bullet.rect.bottom <= 0:
            ai_game.bullets.remove(bullet)


def _create_alien(ai_game, row, col):
    """创建单一外星人"""
    alien = Alien(ai_game)
    # alien_width = alien.rect.width  # 单个外星人宽度
    # alien_height = alien.rect.height
    alien_width, alien_height = alien.rect.size  # size  宽度与高度的元组

    alien.x = alien_width + alien_width * 2 * col
    alien.rect.x = alien.x

    alien.y = alien_height + alien_height * 2 * row
    alien.rect.y = alien.y

    return alien


def create_fleet(ai_game):
    """创建所有外星人"""
    alien = Alien(ai_game)

    # alien_width = alien.rect.width  # 单个外星人宽度
    # alien_height = alien.rect.height  # 单个外星人高度
    alien_width, alien_height = alien.rect.size  # size  宽度与高度的元组

    avilable_space_x = ai_game.settings.screen_width - (2 * alien_width)  # 可画外星人的横向区间
    number_aliens_x = avilable_space_x // (2 * alien_width)  # 间隔一个画一个，取整数个

    avilable_space_y = ai_game.settings.screen_height - 1 * alien_height - ai_game.ship.rect.height
    rows_aliens_y = (avilable_space_y // (2 * alien_height)) - ai_game.settings.alien_left_rows

    for row in range(rows_aliens_y):
        for col in range(number_aliens_x):
            ai_game.aliens.add(_create_alien(ai_game, row, col))


def _alien_change_direction(ai_game):
    """改变外星人的先进方向 并下沉一行"""
    ai_game.settings.alien_move_direct = ai_game.settings.alien_move_direct * -1
    for alien in ai_game.aliens.sprites():
        alien.rect.y += ai_game.settings.alien_y_speen


def _check_fleet_edge(ai_game):
    """判断是否任何外星人是否到了边缘"""
    for alien in ai_game.aliens.sprites():
        if alien.check_edge():
            _alien_change_direction(ai_game)
            break


def update_aliens(ai_game):
    """更新外星人坐标"""
    _check_fleet_edge(ai_game)

    ai_game.aliens.update()

    # 外星人碰撞到船或底线，都结束
    if pygame.sprite.spritecollideany(ai_game.ship, ai_game.aliens):
        _ship_hit(ai_game)
    for alien in ai_game.aliens.sprites():
        if alien.rect.bottom >= ai_game.screen.get_rect().bottom:
            _ship_hit(ai_game)
            break


def part_reset_game(ai_game):
    """飞船撞击重置，游戏不结束"""
    ai_game.ship.back_center()  # 船复位
    ai_game.bullets.empty()  # 子弹清空
    ai_game.aliens.empty()  # 外星人清空
    create_fleet(ai_game)  # 重画外星人


def reset_game(ai_game):
    """游戏重置"""
    ai_game.gameStatus.active()  # 激活

    part_reset_game(ai_game)
    ai_game.gameStatus.initial_status()  # 状态参数复位

    settings = Settings()
    ai_game.settings.alien_reset_times = settings.alien_reset_times  # 外星人重置次数还原
    ai_game.settings.alien_x_speen = settings.alien_x_speen
    ai_game.settings.ship_speed = settings.ship_speed
    ai_game.settings.bullet_speed = settings.bullet_speed


def _ship_hit(ai_game):
    """飞船撞击事件"""
    ai_game.gameStatus.ship_minus()
    if ai_game.gameStatus.is_alive():  # 如果还有命
        part_reset_game(ai_game)
        time.sleep(1)


def _check_keyup_event(ai_game, event):
    """键盘弹起事件 将移动标志都置为false，不再移动"""
    if event.key == pygame.K_RIGHT:
        ai_game.ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ai_game.ship.move_left = False
    elif event.key == pygame.K_UP:
        ai_game.ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ai_game.ship.move_down = False


def _check_keydown_event(ai_game, event):
    """
    键盘按下事件 将移动标志都置为true，更新坐标
    按Q时退出游戏
    """
    if event.key == pygame.K_RIGHT:
        ai_game.ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ai_game.ship.move_left = True
    elif event.key == pygame.K_UP:
        ai_game.ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ai_game.ship.move_down = True
    elif event.key == pygame.K_SPACE:
        _fire_bullet(ai_game)
    elif event.key == pygame.K_q:
        sys.exit()


def _check_play_begin(ai_game, position):
    """鼠标点击播放按钮事件
    """
    if ai_game.play_button.rect.collidepoint(position) and not ai_game.gameStatus.is_alive():  # 点击播放按钮
        pygame.mouse.set_visible(False)
        reset_game(ai_game)


def check_events(ai_game):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_event(ai_game, event)
        elif event.type == pygame.KEYUP:
            _check_keyup_event(ai_game, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            _check_play_begin(ai_game, position)


def update_screen(ai_game):
    """每次循环都重画屏幕"""
    ai_game.screen.fill(ai_game.settings.bg_color)
    ai_game.ship.blitme()  # 画船
    # 画出所有子弹
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()
    # 画外星人
    ai_game.aliens.draw(ai_game.screen)

    # 绘制记分板
    ai_game.dashBoard.show_dash_board()

    # 画播放按钮
    if not ai_game.gameStatus.is_alive():
        pygame.mouse.set_visible(True)
        ai_game.play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
