import pygame as pg
from gun import Gun
import sys, controls
import settings
from pygame.sprite import Group

def run():
	pg.init()
	"""запуск таймера для frame rate"""
	clock = pg.time.Clock()
	screen = pg.display.set_mode(settings.SCREEN_SIZE)
	pg.display.set_caption(settings.GAME_NAME)
	pg.display.set_icon(pg.image.load(settings.GAME_ICON))
	bg_color = settings.BLACK

	gun = Gun(screen)
	bullets = Group()

	while 1:
		controls.events(gun, screen, bullets)
		#установка скорости цикла 60 раз в секунду с учетом времени исполнения
		clock.tick(settings.FPS)
		# bullets.update()
		controls.update_bullets(bullets)
		controls.update(bg_color, screen, gun, bullets)

if __name__ == "__main__":
	run()
