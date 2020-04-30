import pygame
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('GAME')


GRAVIDADE = 5
CHAO = 510

BACKGROUND_dia = pygame.image.load('imagens/ceu-diurno1.png')
x_background = 0
VELOCIDADE = 10
pos_y = 500
PERSONAGEM = pygame.image.load('imagens/personagem1.png')
pos_x_p = 470
pos_y_p = pos_y + 10
DINOSSAURO = pygame.image.load('imagens/dinossauro-correndo1.png')
pos_x_d = 260
VELOCIDADE_atores = 2

fps = pygame.time.Clock()
time = 0

while True: 
    fps.tick(25)

    if pos_y_p <= CHAO:
        pos_y_p += GRAVIDADE

    screen.fill((255, 255, 255))
    screen.blit(BACKGROUND_dia, (x_background, 0))
    screen.blit(PERSONAGEM, (pos_x_p, pos_y_p))
    screen.blit(DINOSSAURO, (pos_x_d, pos_y))

    print(pos_x_p, pos_x_d)

    pos_x_p -= VELOCIDADE_atores
    pos_x_d += VELOCIDADE_atores 

    if pos_x_p <= 950:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            pos_x_p += VELOCIDADE_atores + 2

    if pos_x_p <= 10:
        pos_x_p = 10


    x_background -= VELOCIDADE
    if x_background < -800:
        x_background = randint(-10, 3)


    if time == 600:
        screen.fill((0, 0, 0))
        BACKGROUND_dia = pygame.image.load('imagens/anoitecer_01.png')


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
               pos_y_p -= (VELOCIDADE_atores - 1) + 100
                
    time += 1
    pygame.display.flip()  # update também pode ser usado
