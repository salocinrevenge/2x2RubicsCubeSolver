import pygame       #usando pygame, usar com pip ou baixar separado
from pygame.locals import *     #necessario para eventos definidos, como o QUIT
from Labirinto import *

ALTURA = 600    #altura
LARGURA = 700  #largura
pygame.init()   #iniciar pygame
screen = pygame.display.set_mode((LARGURA, ALTURA)) #criar a janela

pygame.display.set_caption('resolver labirinto')    #dar nome a janela

clock = pygame.time.Clock() #setar maquinad e fps

labirinto = Labirinto()
labirinto.montarLabirinto("labirinto.txt")

contador = 0
while True: #loop do game
    clock.tick(20)  #fps
    for event in pygame.event.get():    #eventos como clicar em botoes ou mouse
        if event.type == QUIT:  
            pygame.quit()   #fechar jogo ao sair
    screen.fill((0, 0, 0))  #pintar tela de preto

    labirinto.mostrarLab(screen)
    if contador == 10:
        labirinto.passoResolver()
        contador = 0

    contador+=1
    pygame.display.update() #atualizar pintura