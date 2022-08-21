import pygame
pygame.init()
x = 400
y = 300
velocidade = 5

janela = pygame.display.set_mode((800, 600))
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

    janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (0, 255, 0), (x, y), 50, 0)
    pygame.display.update()

pygame.quit()
