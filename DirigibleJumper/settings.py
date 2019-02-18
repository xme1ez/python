
class Settings:

	"""class describe game settings"""

	def __init__(self):

		self.title = "Dirigible"
		self.screen_width = 1000
		self.screen_height = 533
		self.obstacle_color = (0, 0, 153)
		self.distance_between_obstacle = 250
		self.game_speed = 1
		self.game_level = 1
		self.game_score = 0
		self.lives = 3
		self.active_game = False

	def reset_stats(self):
		self.game_speed = 1
		self.game_level = 1
		self.game_score = 0
		self.lives = 3
