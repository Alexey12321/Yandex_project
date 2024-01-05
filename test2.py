from pygame import (init as pg_init, quit as pg_quit, QUIT as ev_quit, K_c as key_c)
from pygame.display import (set_mode, set_caption as win_title, flip as display_flip)

from pygame.rect import Rect
from pygame.draw import rect

from pygame.font import init as font_init, SysFont
from pygame.event import get as pg_ev_get
from pygame.key import get_pressed

from sys import exit as sys_exit

pg_init()
font_init()

window = set_mode((800, 800))

win_title('titl')

running = True

font = SysFont('Arial', 16)

x = 30

while running:
    r_rect = Rect(x, 0, 50, 50)
    _rect = rect(window, (255, 255, 255), r_rect)

    # Рассчитываем область текста
    text_surface = font.render(f'Buffer size: {x}.', True, (255, 255, 255))
    text_width, text_height = text_surface.get_size()
    text_x, text_y = 0, 0

    # Заполняем область с текстом сплошным чёрным цветом
    window.fill((0, 0, 0), (text_x, text_y, text_width, text_height))
    window.blit(text_surface, (text_x, text_y))

    for event in pg_ev_get():
        # Handle close event.
        if event.type == ev_quit:
            pg_quit()

            sys_exit(0)

    keys = get_pressed()

    if keys[key_c]:
        x += 1

    display_flip()




