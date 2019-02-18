import pygame.font


class Scoreboard:

	"""class describe label which shows current score"""

	def __init__(self, settings, screen):

		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings

		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()

	def prep_score(self):
		score_str = str(self.settings.game_score)
		self.score_image = self.font.render(score_str, True, self.
											text_color,
											[255, 255, 255])

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
