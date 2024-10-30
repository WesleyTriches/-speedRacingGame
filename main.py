import pygame
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption('Corrida Maluca') #texto em cima 
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load('assets/fundo.png')
carro1 = pygame.image.load('assets/carro1.png')
carro2 = pygame.image.load('assets/carro2.png')
#trilha = pygame
#vitoria = pygame
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill( branco ) #pinta de branco
    tela.blit(fundo, (0,0)) #jogar a imagem do fundo para a tela
    tela.blit(carro1, (0,50))
    tela.blit(carro2, (0,200))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    