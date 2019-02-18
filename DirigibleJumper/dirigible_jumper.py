import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():

	"""Main function"""

	# initialize pygame
	pygame.init()
	settings = Settings()
	screen = gf.init_main_window(settings)
	ship = Ship(settings, screen)
	bg = gf.load_bg_img()
	obstacles = Group()
	play_button = Button(settings, screen, "Play")
	sb = Scoreboard(settings, screen)

	while True:
		screen.blit(bg, (0, 0))
		gf.check_events(settings, screen, ship, obstacles, play_button, sb)
		if not settings.active_game:
			play_button.draw_button()
		elif settings.active_game:
			gf.update_screen(settings, screen, ship, obstacles, sb)
		pygame.display.flip()


run_game()



