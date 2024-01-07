import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75, 75))
sprite1.image.fill((255, 0, 0))
sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((75, 75))
sprite2.image.fill((0, 255, 0))
sprite2.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
sprite1.rect.center = (150, 0)
all_group = pygame.sprite.Group([sprite2, sprite1])
test_group = pygame.sprite.Group(sprite2)
i = 1
b = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite1.rect.center = (150, i)
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)
    b += 1
    if b % 10 == 0:
        i +=1
    window.fill(0)
    all_group.draw(window)
    for s in collide:
        pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)
    pygame.display.flip()

clock = pygame.time.Clock()
clock.tick(30)
pygame.quit()
exit()