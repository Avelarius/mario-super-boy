import pygame
from pygame import *


WIN_WIDTH = 800 #ширина экрана
WIN_HEIGTH = 640 #высота экрана
DISPLAY = (WIN_WIDTH, WIN_HEIGTH) #объедение в одну переменную высоты и ширины
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGTH = 32
PLATFORM_COLOR = "#FF6262"

def main():
	level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

	pygame.init () #инициализация pygame хз зачем, так нужно
	screen = pygame.display.set_mode (DISPLAY) #создаём окошечко
	pygame.display.set_caption ("Super Mario Boy") #пишем название в шапку (типо title)
	bg = Surface((WIN_WIDTH, WIN_HEIGTH)) #создание видимой поверхности
	                                      #будем использовать как фон
	bg.fill (Color(BACKGROUND_COLOR))     #Заливаем поверхность сплошным цветом

	while 1:
		for e in pygame.event.get (): #обработчик событий
			if e.type == QUIT:
				raise SystemExit, "QUIT"
	x=y=0
	for row in level:
		for col in row:
			if col == "-":
				pf = Surface((PLATFORM_WIDTH,PLATFORM_HEIGTH))
				pf.fill (Color(PLATFORM_COLOR))
				screen.blit(pf,(x,y))
			x += PLATFORM_WIDTH
		y += PLATFORM_HEIGTH
		x=0
		
		screen.blit (bg, (0,0))  #каждую итерацию необходимо всё переписывать (зачем не понятно(и что вообще такое итерация?!?!?))
		pygame.display.update () #обновление и вывод всех изменений на экран

if __name__ == '__main__':
	main()
