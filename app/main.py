import pygame
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('GAME')


BACKGROUND_dia = pygame.image.load('imagens/ceu-diurno1.png')
x_background = 0
VELOCIDADE = 10
PERSONAGEM = pygame.image.load('imagens/personagem1.png')
pos_x_p = 470
DINOSSAURO = pygame.image.load('imagens/dinossauro-correndo1.png')
pos_x_d = 260
pos_y = 500
VELOCIDADE_atores = 1

fps = pygame.time.Clock()
time = 0

while True: 
    fps.tick(25)

    screen.fill((255, 255, 255))
    screen.blit(BACKGROUND_dia, (x_background, 0))
    screen.blit(PERSONAGEM, (pos_x_p, pos_y + 10))
    screen.blit(DINOSSAURO, (pos_x_d, pos_y))

    print(pos_x_p, pos_x_d)
    pos_x_p -= VELOCIDADE_atores
    pos_x_d += VELOCIDADE_atores 

    x_background -= VELOCIDADE
    if x_background < -800:
        x_background = randint(-10, 3)


    if time == 300:
        screen.fill((0, 0, 0))
        BACKGROUND_dia = pygame.image.load('imagens/anoitecer_01.png')


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                # PULO DO PERSONAGEM
                pass
            if event.key == pygame.K_RIGHT:
                pos_x_p += VELOCIDADE_atores + 10

    time += 1
    pygame.display.flip()  # update também pode ser usado
