import math
import sqlite3
import pygame
import random
import sys


def terminate():  # Функция для завершения работы игры
    pygame.quit()
    sys.exit()

best_results = []
def start_screen():
    clock.tick(60)
    screen.fill('black')
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
                        main_game(level_flag)  # начинаем игру, функция передаёт выбранный уровень сложности
                    elif 400 <= y <= 480:
                        level_flag = True
                    elif 600 <= y <= 680:
                        level_flag = False
                    elif 800 <= y <= 880:
                        best_results()
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


def main_game(level_flag):
    screen.fill('black')
    stars = [(random.randint(755, width - 1), random.randint(0, height)) for _ in range(100)]
    star_speed = 0.7  # Скорость изменения звёзд на экране
    main_running, points = True, 0
    main_font = pygame.font.Font(None, 36)
    numbers_list_level_1 = [i for i in range(11, 999)] + [i for i in range(-999, -11)]
    numbers_list_level_2 = [i for i in range(11, 99)] + [i for i in range(-99, -11)]
    start_ticks = pygame.time.get_ticks()
    input_numbers, minus_or_plus_flag, enter_flag = list(), True, False  # переменные для работы с ответами пользователя
    meteorite_flag = False

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
    pygame.draw.rect(screen, color_grey_3, (8, 954, 734, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (8, 992, 734, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (8, 954, 4, 38), 0)
    pygame.draw.rect(screen, color_grey_3, (738, 954, 4, 38), 0)
    pygame.draw.rect(screen, color_display_1, (12, 958, 726, 34), 0)
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

    starship_group = pygame.sprite.Group()
    meteorite_group = pygame.sprite.Group()
    ship_image = pygame.image.load("data/ship.png")  # Создание картинки для спрайта корабля
    ship_image = pygame.transform.scale(ship_image, (555, 262))
    starship = pygame.sprite.Sprite(starship_group)  # Создание спрайта космического корабля
    starship.image = ship_image
    starship.rect = starship.image.get_rect()
    starship.rect.x = 865
    starship.rect.y = 700

    meteorite_image = pygame.image.load("data/asteroid.png")  # Создание картинки для спрайта метеорита
    meteorite = pygame.sprite.Sprite(meteorite_group)  # Создание спрайта метеорита
    meteorite.image = meteorite_image
    meteorite.rect = meteorite.image.get_rect()
    meteorite.rect.x = 975
    meteorite.rect.y = 100
    starship_group.draw(screen)  # Отображение спрайта корабля на экране

    while main_running:  # Главный игровой цикл
        stars = [(star[0], (star[1] + star_speed) % height) for star in stars]  # Изменение координат звезд
        pygame.draw.rect(screen, 'black', (750, 0, 750, 1000), 0)
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 1)
        starship_group.draw(screen)  # Отображение спрайта корабля на экране
        pygame.display.flip()
        if not meteorite_flag:
            # Подсчёт времени
            total_time = 60
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            start_time = total_time - int(seconds) - 1
            pygame.draw.rect(screen, color_display_2, (85, 675, 590, 4), 0)
            pygame.draw.rect(screen, color_display_2, (85, 725, 590, 4), 0)
            pygame.draw.rect(screen, color_display_2, (85, 675, 4, 50), 0)
            pygame.draw.rect(screen, color_display_2, (671, 675, 4, 50), 0)
            text_surface = main_font.render('Пропустить вступление и обучение', True, color_display_3)
            screen.blit(text_surface, (165, 690))
            if start_time <= 0:
                meteorite_flag = True
            onboard_computer_comment(0)
            if start_time <= 40:
                onboard_computer_comment(1)
            if start_time <= 20:
                onboard_computer_comment(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 85 <= x <= 675:
                        if 675 <= y <= 750:
                            meteorite_flag = True
        else:
            pygame.draw.rect(screen, color_display_1, (85, 675, 590, 55), 0)
            pygame.draw.rect(screen, color_display_1, (12, 12, 726, 400), 0)
            running = True
            start_ticks = pygame.time.get_ticks()
            star_speed = 0.1  # Замедление движения звёзд во время события с метеоритом
            if level_flag:  # Начальное время в секундах
                total_time = 10
            else:
                total_time = 26
            if level_flag:  # Вывод параметров относительно уровня сложности
                num1, num2 = random.choice(numbers_list_level_1), random.choice(numbers_list_level_1)
                correct_answer = num1 + num2
                text_surface = main_font.render(f'{num1} + {num2} = ?', True, color_display_3)
            else:
                num1, num2 = random.choice(numbers_list_level_2), random.choice(numbers_list_level_2)
                correct_answer = num1 * num2
                text_surface = main_font.render(f'{num1} * {num2} = ?', True, color_display_3)
            screen.blit(text_surface, (300, 500))
            player_answer = ''
            time_add = total_time
            times = [total_time]

            while running:  # Дополнительный игровой цикл

                stars = [(star[0], (star[1] + star_speed) % height) for star in stars]  # Изменение координат звезд
                pygame.draw.rect(screen, 'black', (750, 0, 750, 1000), 0)
                for star in stars:
                    pygame.draw.circle(screen, (255, 255, 255), star, 1)
                starship_group.draw(screen)  # Отображение спрайта корабля на экране
                meteorite_group.draw(screen)  # Отображение спрайта метеорита на экране
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Подсчёт времени
                time_cur = total_time - int(seconds) - 1

                # для движения метеорита

                speed = math.ceil(460 / times[-1])
                if time_add != time_cur:
                    meteorite.rect.y += speed
                    print(f'скорость: {speed}, time: {times[-1]} ')
                time_add = time_cur

                if time_cur < 0:
                    time_cur = -1
                if time_cur >= 0:
                    # Отображение времени на экране
                    text_time = main_font.render(f'{time_cur}', True, color_display_3)
                    text_x, text_y = 360, 964
                    pygame.draw.rect(screen, color_display_1, (12, 958, 726, 34), 0)
                    screen.blit(text_time, (text_x, text_y))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
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
                    if player_answer == '' or player_answer == '-':
                        player_answer = 0
                    if int(player_answer) == correct_answer:
                        meteorite.rect.y = 100
                        if level_flag:
                            total_time += 16
                            times.append(time_cur +16)
                        else:
                            total_time += 26
                            times.append(time_cur + 26)
                        if total_time > points:
                            points = total_time



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
                    print(correct_answer)
                    screen.blit(text_surface, (300, 500))
                if time_cur < 0:
                    run_flag = True
                    screen.fill('black')
                    for i in range(200):
                        screen.fill(pygame.Color('white'),
                                    (random.random() * width,
                                     random.random() * height, 2, 2))
                    starship.rect.x = 750
                    starship.rect.y = 700
                    meteorite.rect.x = 975
                    meteorite.rect.y = 100
                    starship_group.draw(screen)  # Отображение спрайта корабля на экране
                    meteorite_group.draw(screen)  # Отображение спрайта метеорита на экране
                    pygame.display.flip()
                    while run_flag:
                        run_flag = False
                        starship_group.draw(screen)  # Отображение спрайта корабля на экране
                        meteorite_group.draw(screen)  # Отображение спрайта метеорита на экране
                        pygame.display.flip()
                    end_game(points, level_flag)


def end_game(player_score, level_flag):
    main_font = pygame.font.Font(None, 30)
    score_text = main_font.render(f'Ваш рекорд: {player_score}', True, (155, 155, 155))
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('example.db')

    # Создаем курсор для выполнения операций с базой данных
    c = conn.cursor()

    # Выполняем SQL-запрос для создания таблицы (если она не существует)
    c.execute('''CREATE TABLE IF NOT EXISTS numbers (value INTEGER)''')

    # Вставляем число в таблицу
    number = player_score
    c.execute("INSERT INTO numbers (value) VALUES (?)", (number,))

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()

    screen.blit(score_text, (width // 2 - 80, height // 2))
    pygame.draw.rect(screen, color_grey_1, (150, 460, 250, 80), 0)
    pygame.draw.rect(screen, color_grey_1, (1100, 460, 250, 80), 0)
    for i in range(2):
        pygame.draw.rect(screen, color_grey_3, (150 + i * 950, 460, 250, 4), 0)
        pygame.draw.rect(screen, color_grey_3, (150 + i * 950, 536, 250, 4), 0)
        pygame.draw.rect(screen, color_grey_3, (150 + i * 950, 460, 4, 80), 0)
        pygame.draw.rect(screen, color_grey_3, (396 + i * 950, 460, 4, 80), 0)
    text = main_font.render('Выйти в меню', True, 'black')
    screen.blit(text, (200, 490))
    text = main_font.render('Начать заново', True, 'black')
    screen.blit(text, (1150, 490))
    big_font = pygame.font.Font(None, 50)
    text = big_font.render('Игра окончена!', True, 'white')
    screen.blit(text, (width // 2 - 140, 200))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 460 <= y <= 540:
                    if 150 <= x <= 400:
                        start_screen()
                    elif 1100 <= x <= 1350:
                        main_game(level_flag)


def best_results():
    screen.fill('black')
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('example.db')

    # Создаем курсор для выполнения операций с базой данных
    c = conn.cursor()

    # Выполняем SQL-запрос для выборки значений из таблицы
    c.execute("SELECT * FROM numbers")

    # Получаем результат выборки
    rows = c.fetchall()
    results = sorted(rows, reverse=True)[:3]

    text_font = pygame.font.Font(None, 36)
    text = text_font.render(f'Лучшие результаты', True, 'white')
    screen.blit(text, (width // 2 - 103, 100))
    for i in range(len(results)):
        text_font = pygame.font.Font(None, 36)
        text = text_font.render(f'{results[i][0]}', True, 'white')
        screen.blit(text, (width//2, 100*i+200))

    # Закрываем соединение с базой данных
    conn.close()

    for i in range(200):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 2, 2))
    pygame.draw.rect(screen, color_grey_1, (1225, 900, 250, 80), 0)
    pygame.draw.rect(screen, color_grey_3, (1225, 900, 250, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (1225, 976, 250, 4), 0)
    pygame.draw.rect(screen, color_grey_3, (1225, 900, 4, 80), 0)
    pygame.draw.rect(screen, color_grey_3, (1471, 900, 4, 80), 0)
    text_font = pygame.font.Font(None, 36)
    text = text_font.render('Выйти в меню', True, 'black')
    screen.blit(text, (1265, 930))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 900 <= y <= 980 and 1200 <= x <= 1450:
                    start_screen()


def onboard_computer_comment(comment_flag):
    pygame.draw.rect(screen, color_display_1, (12, 12, 726, 400), 0)
    text_font = pygame.font.Font(None, 25)
    txt_list = [['С пробуждением вас, сэр! Вы находитесь на частном космическом корабле', 'Президента Галактики, '
                                                                                          'совершающем рейс '
                                                                                          'система Сириуса - '
                                                                                          'Солнечная Система.',
                 'Вы пробыли в криосне более 100 лет, '
                 'хотите узнать последние новости', 'Солнечной системы? Нет? Ну и отлично! Тогда мы ждём вашего '
                                                    'возвращения',
                 'на должность главного наводчика нашего нашего космического корабля.',
                 'Вернитесь на работу в течении следующих трёх часов и проведите калибровку', 'орудий. '
                                                                                              'Приятного полёта!'],
                ['Орудия откалиброваны. Желаете..?', 'ВНИМАНИЕ! Мы влетаем в пояс астероидов, миновать без потерь,',
                 'статус: НЕВОЗМОЖНО. Примите меры.', 'Ладно, я просто включу автонаводку орудий, и мы минуем его с '
                                                      'минимальными',
                 'потерями.',
                 'Автоматическое наведение, статус: НЕ РАБОТАЕТ.'],
                ['Сэр, похоже, что нам придётся отстреливаться самостоятельно!',
                 'Тогда я буду готовить главное орудие, а вы его настраивать под координаты',
                 'угрожающего нам астероида, договорились?',
                 'А, у вас всё равно нет выбора, тогда начинаем через 3.. 2.. 1..']]
    y = 16
    for i in txt_list[comment_flag]:
        text_surface = text_font.render(i, True, color_display_3)
        screen.blit(text_surface, (16, y))
        y += 26


if __name__ == '__main__':
    pygame.init()  # инициализация
    size = width, height = 1500, 1000  # установка параметров размера окна
    screen = pygame.display.set_mode(size)  # создание окна
    pygame.display.set_caption('Название')  # установка названия окна
    clock = pygame.time.Clock()
    color_dig = 'black'  # цвет символов на клавиатуре
    color_grey_1 = (108, 108, 108)  # цвет детализации объектов
    color_grey_2 = (138, 138, 138)  # основной цвет для крупных объектов
    color_grey_3 = (88, 88, 88)  # цвет для теней и детализации объектов
    color_display_1 = (36, 48, 37)  # основной цвет для экрана бортового компьютера
    color_display_2 = (36, 104, 37)  # основной цвет для объектов экрана бортового компьютера
    color_display_3 = (42, 174, 46)  # дополнительный цвет для объектов экрана бортового компьютера
    start_screen()  # Запуск главного меню игры
