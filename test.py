import random

import pygame

pygame.init()

width, height = 1500, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Звёздное небо')

numstars = 100
stars = [(random.randint(750, width - 1), random.randint(0, height)) for _ in range(numstars)]

background_color = (0, 0, 20)

speed = 0.1

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
        pygame.draw.circle(screen, (255, 255, 255), star, 1)
    pygame.draw.rect(screen, (108, 108, 108), (0, 0, 750, 1000), 0)
    pygame.draw.rect(screen, (138, 138, 138), (740, 0, 10, 1000), 0)
    pygame.display.flip()

pygame.quit()
