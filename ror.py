import sys

import pygame

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
window_size = (600, 95)
screen = pygame.display.set_mode(window_size)

# Загружаем изображение
car_image = pygame.image.load("data/car2.png")
car_image = pygame.transform.flip(car_image, True, False)
# hero_image.set_colorkey(hero_image.get_at((0, 0)))
car_rect = car_image.get_rect()

clock = pygame.time.Clock()
# координаты
car_x, car_y = 0,0
direction = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if car_x >= window_size[0]-car_rect[2]:
        direction = -1
        car_image = pygame.transform.flip(car_image, True, False)
    elif car_x <= 0:
        direction = 1
        car_image = pygame.transform.flip(car_image, True, False)
    car_x += 10 * direction


    # Очищаем экран
    screen.fill('white')
    # отображение создания
    screen.blit(car_image, (car_x, car_y))
    # Обновляем экран
    clock.tick(60)
    pygame.display.flip()

# Завершаем работу Pygame
pygame.quit()
sys.exit()
