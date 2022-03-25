from pickle import FALSE, TRUE
import pygame as pg
import sys, gun, settings
from bullet import Bullet

def events(gun, screen, bullets):
	"""обработчик событий"""
	for event in pg.event.get():
		#событие выхода
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			if (event.key == pg.K_ESCAPE):
				sys.exit()
			elif event.key == pg.K_a or event.key == pg.K_LEFT:
				gun.mleft = TRUE
			elif event.key == pg.K_d or event.key == pg.K_RIGHT:
				gun.mright = TRUE
			elif event.key == pg.K_SPACE:
				gun.gun_on = TRUE
		elif event.type == pg.KEYUP:
			if event.key == pg.K_d or event.key == pg.K_RIGHT:
				gun.mright = FALSE
			elif event.key == pg.K_a or event.key == pg.K_LEFT:
				gun.mleft = FALSE
			elif event.key == pg.K_SPACE:
				gun.gun_on = FALSE

def update(bg_color, screen, gun, bullets):
	"""обновление экрана"""
	screen.fill(bg_color)
	gun.update_gun(gun, bullets)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	gun.output()
	#отрисовка рамки
	pg.draw.rect(screen, settings.WHITE, (10, 10, settings.SCREEN_SIZE[0] - 20, settings.SCREEN_SIZE[1] - 20), 5)
	#отрисовывает прогруженную текстурку. можно использовать flip
	pg.display.flip()

def update_bullets(bullets):
	"""удаление пуль вне игровой области"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.bul_rect.bottom <= 0:
			bullets.remove(bullet)
		# print(len(bullets))
