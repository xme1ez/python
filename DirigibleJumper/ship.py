import pygame
from queue import Queue


class Ship:

	"""class Ship describe ship settings"""

	def __init__(self, settings, screen):

		self.settings = settings
		self.screen = screen
		self.image = pygame.image.load("img/ship.png")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		# ship appears in the middle left side
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		self.falling_flag = True
		# self.queue = Queue()

	def blitme(self):
		# Draw ship on the screen
		if self.falling_flag and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.settings.game_speed
		self.screen.blit(self.image, self.rect)
