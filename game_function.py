import pygame
import sys

from bullet import Bullet
from alien import Alien


def update_bullets(ai_game):
    """更新子弹信息"""
    # 子弹实时更新
    ai_game.bullets.update()
    # 销毁屏幕外的子弹
    destory_bullet(ai_game)


def fire_bullet(ai_game):
    """发射子弹 在允许最大子弹数的范围内创建"""
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
        ai_game.bullets.add(Bullet(ai_game))


def destory_bullet(ai_game):
    """消除屏幕外的子弹"""
    for bullet in ai_game.bullets.copy():
        if bullet.rect.bottom <= 0:
            ai_game.bullets.remove(bullet)


def create_alien(ai_game, row, col):
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
            ai_game.aliens.add(create_alien(ai_game, row, col))


def alien_change_direction(ai_game):
    """改变外星人的先进方向 并下沉一行"""
    ai_game.settings.alien_move_direct = ai_game.settings.alien_move_direct * -1
    for alien in ai_game.aliens.sprites():
        alien.rect.y += ai_game.settings.alien_y_speen


def check_fleet_edge(ai_game):
    """判断是否任何外星人是否到了边缘"""
    for alien in ai_game.aliens.sprites():
        if alien.check_edge():
            alien_change_direction(ai_game)
            break


def update_aliens(ai_game):
    """更新外星人坐标"""
    check_fleet_edge(ai_game)

    ai_game.aliens.update()


def check_keyup_event(ai_game, event):
    """键盘弹起事件 将移动标志都置为false，不再移动"""
    if event.key == pygame.K_RIGHT:
        ai_game.ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ai_game.ship.move_left = False
    elif event.key == pygame.K_UP:
        ai_game.ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ai_game.ship.move_down = False


def check_keydown_event(ai_game, event):
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
        fire_bullet(ai_game)
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_game):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(ai_game, event)
        elif event.type == pygame.KEYUP:
            check_keyup_event(ai_game, event)


def update_screen(ai_game):
    """每次循环都重缓屏幕"""
    ai_game.screen.fill(ai_game.settings.bg_color)
    ai_game.ship.blitme()  # 画船
    # 画出所有子弹
    for bullet in ai_game.bullets.sprites():
        bullet.draw_bullet()
    # 画外星人
    ai_game.aliens.draw(ai_game.screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()
