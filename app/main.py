import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('GAME')


BACKGROUND_dia = pygame.image.load('imagens/ceu-diurno1.png')

PERSONAGEM = pygame.image.load('imagens/personagem1.png')
x_inicial_p = 30

DINOSSAURO = pygame.image.load('imagens/dinossauro-correndo1.png')
x_inicial_d = - 300

VELOCIDADE = 7



while True:
    
    x_inicial_p += VELOCIDADE 
    x_inicial_d += VELOCIDADE
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(BACKGROUND_dia, (0, 0))
    screen.blit(PERSONAGEM, (x_inicial_p, 510))
    screen.blit(DINOSSAURO, (x_inicial_d, 510))


    pygame.display.update()