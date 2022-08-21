import pygame
import random

pygame.init()
x = 400
y = 800
lista = [70,230,420,600]
posicao_x = random.choice(lista) 
posicao_y = 1070
velocidadecarroroxo = 35
velocidade = 15

posicaofundo_x = 200
posicaofundo_y = 1070
velocidadefundo = 5

fundo = pygame.image.load("estrada51.png")
carro = pygame.image.load("carrosemfundo2.png")
carroroxo = pygame.image.load("carroroxosemfundo1.png")

janela = pygame.display.set_mode((800, 1070))
pygame.display.set_caption("Criando jogo com python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comando = pygame.key.get_pressed()
    if comando[pygame.K_UP]:
        y -= velocidade
    if comando[pygame.K_DOWN]:
        y += velocidade
    if comando[pygame.K_RIGHT]:
        x += velocidade
    if comando[pygame.K_LEFT]:
        x -= velocidade
    posicao_y = posicao_y - velocidade
    if (posicao_y <= -200):
        posicao_y = 1070
        posicao_x = random.choice(lista)  
    
    
    posicaofundo_y = posicaofundo_y + velocidadefundo
    if (posicaofundo_y <= -200):
        posicaofundo_y = 1070

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carroroxo, (posicao_x, posicao_y))
    # pygame.draw.circle(janela, (0, 255, 0), (x, y), 50, 0)
    pygame.display.update()

pygame.quit()
