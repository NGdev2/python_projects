from pickle import FALSE, TRUE
import pygame, settings
from bullet import Bullet

class Gun():

	def __init__(self, screen):
		"""инициализация пушки"""

		self.screen = screen
		self.image = pygame.image.load('./graphics/sprites/sentinel.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		"""установка координат пушки и приведение типов к вещественному"""
		self.center = float(self.rect.centerx)
		self.mright = FALSE
		self.mleft = FALSE
		self.gun_on = FALSE
		self.gun_delay = 7


	def output(self):
		#рисование пушки
		self.screen.blit(self.image, self.rect)


	def update_gun(self, gun, bullets):
		#обновление позиции пушки
		if self.mright == TRUE and self.rect.right < self.screen_rect.right - 5:
			self.center += settings.GUN_SPEED
		elif self.mleft == TRUE and self.rect.left > self.screen_rect.left:
			self.center -= settings.GUN_SPEED
		if self.gun_on == TRUE and pygame.time.get_ticks() % self.gun_delay == 1:
			new_bullet = Bullet(self.screen, gun)
			bullets.add(new_bullet)

		self.rect.centerx = self.center
