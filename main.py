import pygame, random

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

movXCar1 = 0 #seria o eixo x que se movimenta
movXCar2 = 0
posYcar1 = 50
posYcar2 = 180
vitoria = pygame.mixer.Sound('assets/vitoria.mp3')
vitoria.set_volume(0.5)
pygame.mixer.music.load('assets/trilha.mp3')
pygame.mixer.music.play(-1)#looping
acabou = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill( branco ) #pinta de branco
    tela.blit(fundo, (0,0)) #jogar a imagem do fundo para a tela
    tela.blit(carro1, (movXCar1,posYcar1))
    tela.blit(carro2, (movXCar2,posYcar2))
    
    
    if not acabou:
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10) 
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYcar1 = 350
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYcar2 = 480
        
    fonte = pygame.font.Font('freesansbold.ttf',60)#ttf é o arquivo da font
    textoVermelho = fonte.render('Vermelho Ganhou!', True, branco)
    textoAmarelo = fonte.render('Amarelo Ganhou!', True, branco)
        
    if posYcar1 == 350 and movXCar1 >= 900 and movXCar1 > movXCar2:
        tela.blit(textoVermelho, (270,70))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)
        
    elif posYcar2 == 480 and movXCar2 >= 900 and movXCar2 > movXCar1:
        tela.blit(textoAmarelo, (270,180))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    