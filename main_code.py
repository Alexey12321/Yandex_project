import pygame
import random
import sys

def terminate():  # Функция для завершения работы игры
    pygame.quit()
    sys.exit()


def start_screen():
    for i in range(200):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 2, 2))
    for i in range(4):
        pygame.draw.rect(screen, color_grey_1, (600, i * 200 + 200, 300, 80), 0)
        pygame.draw.rect(screen, color_grey_3, (600, i * 200 + 200, 300, 4), 0)
        pygame.draw.rect(screen, color_grey_3, (600, i * 200 + 276, 300, 4), 0)
        pygame.draw.rect(screen, color_grey_3, (600, i * 200 + 200, 4, 80), 0)
        pygame.draw.rect(screen, color_grey_3, (896, i * 200 + 200, 4, 80), 0)
    level_flag = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 600 <= x <= 900:
                    if 200 <= y <= 280:
                        return level_flag  # начинаем игру, функция возвращает выбранный уровень сложности
                    elif 400 <= y <= 480:
                        level_flag = True
                    elif 600 <= y <= 680:
                        level_flag = False
                    elif 800 <= y <= 880:
                        print('Лучшие результаты')
            font = pygame.font.Font(None, 36)
            txt_list = ['Начать игру', 'Уровень сложности 1', 'Уровень сложности 2', 'Лучшие результаты']
            x_txt_list = [680, 620, 620, 630]
            for i in range(4):
                text_surface = font.render(txt_list[i], True, color_dig)
                screen.blit(text_surface, (x_txt_list[i], i * 200 + 230))
            pygame.draw.rect(screen, color_grey_1, (620, 454, 260, 6), 0)
            pygame.draw.rect(screen, color_grey_1, (620, 656, 260, 6), 0)
            if level_flag:
                pygame.draw.rect(screen, color_dig, (620, 454, 260, 6), 0)
                pygame.draw.rect(screen, color_dig, (620, 656, 260, 6), 1)
            else:
                pygame.draw.rect(screen, color_dig, (620, 454, 260, 6), 1)
                pygame.draw.rect(screen, color_dig, (620, 656, 260, 6), 0)
            pygame.display.flip()


def end_game(points):
    pygame.draw.rect(screen, color_grey_3, (width // 2, height // 2, 100, 50), 0)
    font = pygame.font.Font(None, 36)
    text_answer = font.render(f'Ваш счёт {points}', True, (155, 155, 155))
    text_width, text_height = text_answer.get_size()
    text_x, text_y = width // 2, height // 2
    screen.fill((0, 0, 0), (text_x, text_y, text_width, text_height))
    screen.blit(text_answer, (text_x, text_y))
    pygame.display.flip()
    print('sos')


def main_game(level_flag):
    stars = [(random.randint(755, width - 1), random.randint(0, height)) for _ in range(100)]

    star_speed = 0.2  # Скорость изменения звёзд на экране
    running = True
    main_font = pygame.font.Font(None, 36)
    pygame.draw.rect(screen, color_grey_2, (0, 0, 750, 1000), 0)  # Отрисовка элементов игры
    pygame.draw.rect(screen, color_grey_3, (8, 746, 734, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (738, 8, 4, 740), 0)
    pygame.draw.rect(screen, color_grey_3, (8, 8, 734, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (8, 8, 4, 742), 0)
    pygame.draw.rect(screen, color_display_1, (12, 12, 726, 734), 0)
    pygame.draw.rect(screen, color_display_2, (102, 600, 544, 4), 0)
    pygame.draw.rect(screen, color_display_2, (122, 640, 504, 4), 0)
    for i in range(6):
        pygame.draw.rect(screen, color_grey_1, (8 + 96 * i, 754, 92, 96), 0)
        pygame.draw.rect(screen, color_grey_1, (8 + 96 * i, 854, 92, 96), 0)
        pygame.draw.rect(screen, color_grey_3, (96 * (i + 1), 754, 4, 96), 0)
        pygame.draw.rect(screen, color_grey_3, (8 + 96 * i, 846, 92, 4), 0)
        pygame.draw.rect(screen, color_grey_3, (96 * (i + 1), 854, 4, 96), 0)
        pygame.draw.rect(screen, color_grey_3, (8 + 96 * i, 946, 92, 4), 0)
    for i in range(2):
        delta = 100 * i
        pygame.draw.rect(screen, color_grey_1, (584, 754 + delta, 158, 96), 0)
        pygame.draw.rect(screen, color_grey_3, (738, 754 + delta, 4, 96), 0)
        pygame.draw.rect(screen, color_grey_3, (584, 846 + delta, 158, 4), 0)
    pygame.draw.rect(screen, color_grey_1, (8, 954, 734, 38), 0)
    pygame.display.flip()
    for i in range(1, 6):
        text_surface = main_font.render(f'{i - 1}', True, color_dig)
        screen.blit(text_surface, (i * 96 + 4 - 55, 790))
    for i in range(1, 6):
        text_surface = main_font.render(f'{i + 4}', True, color_dig)
        screen.blit(text_surface, (i * 96 + 4 - 55, 890))

    text_surface = main_font.render(f'+', True, color_dig)
    screen.blit(text_surface, (527, 787))
    text_surface = main_font.render(f'-', True, color_dig)
    screen.blit(text_surface, (530, 887))
    text_surface = main_font.render(f'Enter', True, color_dig)
    screen.blit(text_surface, (630, 887))
    text_surface = main_font.render(f'Delete', True, color_dig)
    screen.blit(text_surface, (625, 790))

    numbers_list_level_1 = [i for i in range(9, 999)]
    numbers_list_level_2 = [i for i in range(11, 99)]
    if level_flag:  # Вывод параметров относительно уровня сложности
        num1, num2 = random.choice(numbers_list_level_1), random.choice(numbers_list_level_1)
        correct_answer = num1 + num2
        text_surface = main_font.render(f'{num1} + {num2} = ?', True, color_display_3)
    else:
        num1, num2 = random.choice(numbers_list_level_2), random.choice(numbers_list_level_2)
        correct_answer = num1 * num2
        text_surface = main_font.render(f'{num1} * {num2} = ?', True, color_display_3)
    screen.blit(text_surface, (300, 300))

    input_numbers, minus_or_plus_flag, enter_flag = list(), True, False  # переменные для работы с ответами пользователя

    total_time = 2  # Время в секундах
    start_ticks = pygame.time.get_ticks()
    points = 0




    while running:  # Главный игровой цикл
        font = pygame.font.Font(None, 36)
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        # Отображение времени на экране
        time_cur = total_time - int(seconds) - 1
        text_time = font.render(f'{time_cur}', True, (155, 155, 155))
        text_width, text_height = text_time.get_size()
        text_x, text_y = 150, 960

        # Заполняем область с текстом сплошным чёрным цветом
        screen.fill((0, 0, 0), (text_x, text_y, text_width, text_height))
        screen.blit(text_time, (text_x, text_y))

        stars = [(star[0], (star[1] + star_speed) % height) for star in stars]  # Изменение координат звезд
        pygame.draw.rect(screen, 'black', (750, 0, 750, 1000), 0)
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 1)

        ship = pygame.image.load("data/ship2.png").convert_alpha()
        ship = pygame.transform.scale(ship, (222, 222))
        # Отображение изображения на экране
        screen.blit(ship, (1000, 600))


        pygame.display.flip()
        player_answer = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not enter_flag:
                    if (854 <= y <= 950) and (588 <= x <= 740):
                        enter_flag = True
                    elif (754 <= y <= 850) and (588 <= x <= 740):
                        if len(input_numbers) > 0:
                            input_numbers.pop()
                    elif 754 <= y <= 850:
                        if 8 <= x <= 100:
                            input_numbers.append(0)
                        elif 8 + 100 * 1 <= x <= 100 + 96 * 1:
                            input_numbers.append(1)
                        elif 8 + 100 * 2 <= x <= 100 + 96 * 2:
                            input_numbers.append(2)
                        elif 8 + 100 * 3 <= x <= 100 + 96 * 3:
                            input_numbers.append(3)
                        elif 8 + 100 * 4 <= x <= 100 + 96 * 4:
                            input_numbers.append(4)
                        elif 8 + 100 * 5 <= x <= 100 + 96 * 5:
                            minus_or_plus_flag = True
                    elif 854 <= y <= 950:
                        if 8 <= x <= 100:
                            input_numbers.append(5)
                        elif 8 + 100 * 1 <= x <= 100 + 96 * 1:
                            input_numbers.append(6)
                        elif 8 + 100 * 2 <= x <= 100 + 96 * 2:
                            input_numbers.append(7)
                        elif 8 + 100 * 3 <= x <= 100 + 96 * 3:
                            input_numbers.append(8)
                        elif 8 + 100 * 4 <= x <= 100 + 96 * 4:
                            input_numbers.append(9)
                        elif 8 + 100 * 5 <= x <= 100 + 96 * 5:
                            minus_or_plus_flag = False
                    print_numbers = list()
                    to_add_and_print = ''
                    if not minus_or_plus_flag:
                        to_add_and_print = '-'
                    for i in range(len(input_numbers)):
                        if i <= 24:
                            print_numbers.append(str(input_numbers[i]))
                        else:
                            break
                    player_answer = to_add_and_print + ''.join(print_numbers)
                    pygame.draw.rect(screen, color_display_1, (122, 620, 504, 20), 0)
                    text_surface = main_font.render(player_answer, True, color_display_3)
                    screen.blit(text_surface, (142, 620))
                    pygame.draw.rect(screen, color_display_2, (122, 640, 504, 4), 0)
                    input_numbers = [int(i) for i in print_numbers]
        if enter_flag:

            print(correct_answer)
            if player_answer == '':
                player_answer = 0
            if int(player_answer) == correct_answer:
                print('win')
                points += 1
                total_time += 10
            elif time_cur == 0:
                # end_game(points)
                print('lose')
            enter_flag = False
            input_numbers.clear()
            pygame.draw.rect(screen, color_display_1, (122, 620, 504, 20), 0)
            pygame.draw.rect(screen, color_display_1, (200, 200, 400, 400), 0)
            if level_flag:
                num1, num2 = random.choice(numbers_list_level_1), random.choice(numbers_list_level_1)
                correct_answer = num1 + num2
                text_surface = main_font.render(f'{num1} + {num2} = ?', True, color_display_3)
            else:
                num1, num2 = random.choice(numbers_list_level_2), random.choice(numbers_list_level_2)
                correct_answer = num1 * num2
                text_surface = main_font.render(f'{num1} * {num2} = ?', True, color_display_3)
            screen.blit(text_surface, (300, 300))

        # Создание поверхности для прямоугольника
        if time_cur <= 0:

            rect_surface = pygame.Surface((width, height))
            rect_surface.set_alpha(1)  # Устанавливаем прозрачность (0 - полностью прозрачно, 255 - непрозрачно)
            # Заливка поверхности цветом
            rect_surface.fill((0, 0, 0))  # Например, красный цвет

            # Отображение прямоугольника на экране
            screen.blit(rect_surface, (0, 0))

            font = pygame.font.Font(None, 36)


            text_big = font.render(f'Ваш счёт {points}', True, (155, 155, 155))
            text_big_width, text_big_height = text_time.get_size()
            text_big_x, text_big_y = width//4, height//2
            screen.blit(text_big, (text_big_x, text_big_y))



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos and time_cur <= 0:
                        main_game(1)

        # Загрузка изображения




if __name__ == '__main__':
    pygame.init()  # инициализация
    size = width, height = 1500, 1000  # установка параметров размера окна
    screen = pygame.display.set_mode(size)  # создание окна
    pygame.display.set_caption('Название')  # установка названия окна
    clock = pygame.time.Clock()
    # clock.tick(6000)
    color_dig = 'black'  # цвет символов на клавиатуре
    color_grey_1 = (108, 108, 108)  # цвет детализации объектов
    color_grey_2 = (138, 138, 138)  # основной цвет для крупных объектов
    color_grey_3 = (88, 88, 88)  # цвет для теней и детализации объектов
    color_display_1 = (14, 88, 14)  # основной цвет для экрана бортового компьютера
    color_display_2 = (39, 144, 75)  # основной цвет для объектов экрана бортового компьютера
    color_display_3 = (39, 180, 75)  # дополнительный цвет для объектов экрана бортового компьютера
    screen.fill('black')
    need_flag = start_screen()  # загрузка меню
    main_game(need_flag)  # загрузка основного этапа игры с передачей уровня сложности
