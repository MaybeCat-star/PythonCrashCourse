class Settings:

	def __init__(self):
		self.screen_width = 1400
		self.screen_height = 800
		self.bg_color = (56, 56, 56)
		self.ship_speed = 1.5
		self.bullet_speed = 2.0
		self.bullet_width = 5.0
		self.bullet_height = 15
		self.bullet_color = (200, 200, 200)
		self.alien_speed = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		self.ship_limit = 3
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.bullets_allowed = 3
		self.bullet_width_scale = 1.2
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.5
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		self.bullet_width *= self.bullet_width_scale
		