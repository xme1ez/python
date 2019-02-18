import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):

	"""class describe obstacle"""

	def __init__(self, settings, screen, width, height, y_pos):
		super(Obstacle, self).__init__()
		self.screen = screen
		self.settings = settings
		self.width = width
		self.height = height
		self.x = settings.screen_width
		self.y_pos = y_pos

		self.rect = pygame.Rect(0, y_pos, self.width, self.height)

	def blitme(self):
		self.x -= 1
		self.rect.x = self.x

	def update(self):
		self.x -= self.settings.game_speed
		self.rect.x = self.x

	def draw_obstacle(self):
		pygame.draw.rect(self.screen, [0, 0, 155], self.rect)

