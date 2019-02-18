import sys

import pygame
import time
import threading
import random

# from obstacle import Obstacle

"""module contains function for different events performing"""


def init_main_window(settings):
	"""initialize main window"""
	screen = pygame.display.set_mode((settings.screen_width,
									  settings.screen_height))
	pygame.display.set_caption(settings.title)

	return screen


def load_bg_img():
	bg = pygame.image.load("img/bg.png")

	return bg


def check_events(settings, screen, ship, obstacles, play_button, sb):
	"""key events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				thread = threading.Thread(name="thread", target=jump,
										  args=(ship, screen)).start()
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, screen, play_button, ship, obstacles, mouse_x, mouse_y, sb)


def check_play_button(settings, screen, play_button, ship, obstacles, mouse_x, mouse_y, sb):
	"""check play button is pressed"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not settings.active_game:
		settings.active_game = True
		ship.rect.centery = screen.get_rect().centery
		obstacle_initialization(settings, screen, obstacles)
		settings.reset_stats()



def jump(ship, screen):
	"""ship jumping"""
	ship.falling_flag = False
	for accel in range(0, 10):
		if ship.rect.top > ship.screen_rect.top:
			time.sleep(0.001)
			ship.rect.centery -= int(accel)
	for accel in range(9, -1, -1):
		if ship.rect.top > ship.screen_rect.top:
			time.sleep(0.01)
			ship.rect.centery -= int(accel)
	ship.falling_flag = True


def obstacle_initialization(settings, screen, obstacles):
	"""create obstacle"""
	position = random.randint(0, settings.screen_height -
							  settings.distance_between_obstacle)
	obstacles.add(Obstacle(settings, screen, 50, position, 0))
	obstacles.add(Obstacle(settings, screen, 50, 533 - position -
						   settings.distance_between_obstacle,
						   position + settings.distance_between_obstacle))


def update_screen(settings, screen, ship, obstacles, sb):
	"""update screen"""
	ship.blitme()
	obstacles.update()

	if len(obstacles) == 0:
		obstacle_initialization(settings, screen, obstacles)

	elif len(obstacles) == 2:
		iscollide = check_collision(ship, obstacles)
		if not iscollide:

			for sprite in obstacles.sprites():
				sprite.draw_obstacle()
				if sprite.x < -50:
					obstacles.empty()
					change_score(settings, sb)
					change_level(settings)
					break

		elif iscollide:
			decrease_lives(settings, obstacles)
	sb.prep_score()
	sb.show_score()


def check_collision(ship, obstacles):
	"""check for ship and obstacle collision"""
	if pygame.sprite.spritecollideany(ship, obstacles):
		return True
	else:
		return False


def decrease_lives(settings, obstacles):
	"""if collision is happened decrease cound of lives"""
	settings.lives -= 1
	if settings.lives == 0:
		time.sleep(3)
		settings.active_game = False
		obstacles.empty()


def change_score(settings, sb):
	"""if collision didn't happened increase score"""
	settings.game_score += settings.game_speed * settings.game_level
	sb.prep_score()


def change_level(settings):
	"""change level if ship passed through 5 obstacle"""
	if settings.game_score % 5 == 0:
		settings.game_level += 1
		settings.game_speed += 1






