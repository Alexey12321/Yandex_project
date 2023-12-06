import pygame
import random

# Инициализация pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Звёздное небо')

# Генерация звезд
num_stars = 100
stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_stars)]

# Установка цвета фона
background_color = (0, 0, 30)

# Установка скорости движения фона
speed = 0.1

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Изменение координат звезд для создания эффекта движущегося фона
    stars = [(star[0], (star[1] + speed) % height) for star in stars]

    # Отрисовка звезд
    screen.fill(background_color)
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 2)

    pygame.display.flip()

# Завершение работы pygame
pygame.quit()
