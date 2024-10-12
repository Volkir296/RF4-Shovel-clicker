## додумать
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


cursor_image = pygame.Surface((20,20))
cursor_image.fill((255,255,0)) # Жёлтый курсор

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # получение позиции мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # очистка экрана
    screen.fill((255,255,255))

    # отображение второго курсора
    screen.blit(cursor_image, (mouse_x,mouse_y))

    screen.blit(cursor_image, (mouse_x+30,mouse_y+30))

    pygame.display.flip()
    clock.tick(60)

