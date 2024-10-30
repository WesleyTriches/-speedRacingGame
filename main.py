import pygame
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption('Corrida Maluca') #texto em cima 
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load('assets/fundo.png')
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill( branco )
    tela.blit(fundo, (0,0)) #jogar a imagem do fundo para a tela
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    