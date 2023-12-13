import pygame
import random

if __name__ == '__main__':
    pygame.init()  # Инициализация
    size = width, height = 1500, 1000  # Установка параметров окна
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Название')
    pygame.display.flip()
    running = True
    clock = pygame.time.Clock()
    stars = [(random.randint(755, width - 1), random.randint(0, height)) for _ in range(100)]
    star_speed = 0.1  # Скорость изменения звёзд на экране
    screen.fill('black')  # Отрисовка элементов главного экрана игры
    pygame.draw.rect(screen, (108, 108, 108), (0, 0, 750, 1000), 0)
    pygame.draw.rect(screen, (138, 138, 138), (742, 0, 8, 1000), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 0, 8, 1000), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 0, 750, 8), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 992, 750, 8), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 950, 750, 4), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 750, 750, 4), 0)
    pygame.draw.rect(screen, (138, 138, 138), (584, 750, 4, 200), 0)

    for i in range(1, 6):
        pygame.draw.rect(screen, (138, 138, 138), (i * 96 + 4, 750, 4, 200), 0)
        pygame.draw.rect(screen, (88, 88, 88), (i * 96, 754, 4, 196), 0)
        pygame.draw.rect(screen, (88, 88, 88), ((i - 1) * 96 + 8, 846, 90, 4), 0)
        pygame.draw.rect(screen, (88, 88, 88), ((i - 1) * 96 + 8, 946, 90, 4), 0)

    color_dig = 'white'

    for i in range(1, 6):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f'{i-1}', True, color_dig)
        screen.blit(text_surface, (i * 96 + 4 - 55, 790))

    for i in range(1, 6):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f'{i+4}', True, color_dig)
        screen.blit(text_surface, (i * 96 + 4 - 55, 890))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'+', True, color_dig)
    screen.blit(text_surface, (527, 787))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'-', True, color_dig)
    screen.blit(text_surface, (530, 887))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Enter', True, color_dig)
    screen.blit(text_surface, (630, 887))

    pygame.draw.rect(screen, (88, 88, 88), (5 * 96 + 8, 846, 94, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (5 * 96 + 8, 946, 94, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (5 * 96 + 108, 946, 154, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (6 * 96 + 4, 754, 4, 194), 0)
    pygame.draw.rect(screen, (88, 88, 88), (738, 754, 4, 196), 0)
    pygame.draw.rect(screen, (138, 138, 138), (0, 850, 584, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (8, 746, 734, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (738, 8, 4, 740), 0)
    pygame.draw.rect(screen, (88, 88, 88), (8, 8, 734, 4), 0)
    pygame.draw.rect(screen, (88, 88, 88), (8, 8, 4, 742), 0)
    pygame.draw.rect(screen, (14, 88, 14), (12, 12, 726, 734), 0)
    pygame.display.flip()

    font = pygame.font.Font(None, 36)
    text_surface = font.render('Привет, мир!', True, 'white')
    screen.blit(text_surface, (300, 300))

    while running:  # Главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        stars = [(star[0], (star[1] + star_speed) % height) for star in stars]  # Изменение координат звезд
        pygame.draw.rect(screen, 'black', (750, 0, 750, 1000), 0)
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 1)
        pygame.display.flip()
    pygame.quit()  # Завершение работы


