import pygame

"""наследуем класс пулю изь класса спрайтов"""
class Bullet(pygame.sprite.Sprite):

	"""инициализация пули в текущей позиции пушки"""
	def __init__(self, screen, gun):
		"""super обращается к родительскому классу (Sprite). Берем метод init из Sprite"""
		super(Bullet, self).__init__()
		self.screen = screen
		self.bul_rect = pygame.Rect(0, 0, 2, 12)
		self.color = 8, 56, 9
		self.speed = 8
		self.bul_rect.centerx = gun.rect.centerx
		self.bul_rect.top = gun.rect.top
		self.y = float(self.bul_rect.y)
	
	def update(self):
		"""движение пули"""
		self.y -= self.speed
		self.bul_rect.y = self.y

	def draw_bullet(self):
		"""отрисовка пули"""
		pygame.draw.rect(self.screen, self.color, self.bul_rect)
