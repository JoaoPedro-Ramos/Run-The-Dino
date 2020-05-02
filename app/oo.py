import pygame
from pygame.locals import *
from random import randint


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('RUN THE DINO')
        self.screen = pygame.display.set_mode((1000, 600))   
        self.GRAVIDADE = 5
        self.CHAO = 510
        self.BACKGROUND_dia = pygame.image.load('imagens/ceu-diurno1.png')
        self.x_background = 0
        self.VELOCIDADE = 10
        self.pos_y = 500
        self.PERSONAGEM = pygame.image.load('imagens/personagem1.png')
        self.pos_x_p = 470
        self.pos_y_p = self.pos_y + 10
        self.DINOSSAURO = pygame.image.load('imagens/dinossauro-correndo1.png')
        self.pos_x_d = 260
        self.VELOCIDADE_atores = 2
        self.fps = pygame.time.Clock()
        self.time = 0

#################################################

class Personagem(Game):

    def __init__(self):
        super().__init__()

    def movimentacao(self):
        pass

#################################################

class Render(Game):

    def __init__(self):
        super().__init__()
    
    def render_(self):
        while True: 
            self.fps.tick(25)

            if self.pos_y_p <= self.CHAO:     # GRAVIDADE 
                self.pos_y_p += self.GRAVIDADE # GRAVIDADE

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.BACKGROUND_dia, (self.x_background, 0))
            self.screen.blit(self.PERSONAGEM, (self.pos_x_p, self.pos_y_p))
            self.screen.blit(self.DINOSSAURO, (self.pos_x_d, self.pos_y))

            self.pos_x_p -= self.VELOCIDADE_atores    # MOVIMENTO CONTINUO DOS ATORES (PERSONAGEM)
            self.pos_x_d += self.VELOCIDADE_atores    # MOVIMENTO CONTINUO DOS ATORES (DINOSSAURO)

            if self.pos_x_p <= 950:           # MOVIMENTO DO JOGADOR CONTROLANDO O PERSONAGEM
                pressed = pygame.key.get_pressed()    # MOVIMENTO DO JOGADOR CONTROLANDO O PERSONAGEM
                if pressed[pygame.K_RIGHT]:             # MOVIMENTO DO JOGADOR CONTROLANDO O PERSONAGEM
                    self.pos_x_p += self.VELOCIDADE_atores + 2  # MOVIMENTO DO JOGADOR CONTROLANDO O PERSONAGEM

            if self.pos_x_p <= 10:      # VALOR MÍNIMO DO X DO PERSONAGEM
                self.pos_x_p = 10       # VALOR MÍNIMO DO X DO PERSONAGEM


            self.x_background -= self.VELOCIDADE    # MOVIMENTO DO CENÁRIO
            if self.x_background < -800:       # MOVIMENTO DO CENÁRIO
                self.x_background = randint(-10, 3)  # MOVIMENTO DO CENÁRIO


            if self.time == 600:            # TEMPO PARA MUDANÇA DE CENÁRIO
                self.screen.fill((0, 0, 0))       # COR DE FUNDO DO CENÁRIO
                self.BACKGROUND_dia = pygame.image.load('imagens/anoitecer_01.png')  # TROCA DE CENÁRIO PARA ANOITECER


            for event in pygame.event.get():     # EVENTOS DO USUÁRIO
                if event.type == QUIT:           # EVENTO DO USUÁRIO PARA SAIR DO JOGO
                    pygame.quit()                 # SAINDO DO JOGO
                if event.type == KEYDOWN:         # EVENTO DO TECLADO
                    if event.key == pygame.K_SPACE:  # EVENTO DE APERTAR O SPACE
                        self.pos_y_p -= (self.VELOCIDADE_atores - 1) + 100   # PULO DO PERSONAGEM
                        
            self.time += 1   # CONTAGEM DO TEMPO
            pygame.display.flip()  # RENDERIZAÇÃO DE TUDO

#################################################

if __name__ == '__main__':
    r = Render()
    r.__init__()