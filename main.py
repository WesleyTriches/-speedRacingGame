import pygame, random, time 

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("recursos/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption('Corrida Maluca') #texto em cima 
branco = (255,255,255)
preto = (0,0,0)
fundo = pygame.image.load('recursos/fundo.png')
carro1 = pygame.image.load('recursos/carro1.png')
carro2 = pygame.image.load('recursos/carro2.png')
carro3 = pygame.image.load('recursos/carro3.png')

movXCar1 = 0 #seria o eixo x que se movimenta
movXCar2 = 0
movXCar3 = 0
posYcar1 = 25
posYcar2 = 115
posYCar3 = 205
vitoria = pygame.mixer.Sound('recursos/vitoria.mp3')
vitoria.set_volume(0.5)
pygame.mixer.music.load('recursos/trilha.mp3')
pygame.mixer.music.play(-1)#looping
acabou = False
somDaVitoria = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
            
    tela.fill( branco ) #pinta de branco
    tela.blit(fundo, (0,0)) #jogar a imagem do fundo para a tela
    tela.blit(carro1, (movXCar1,posYcar1))
    tela.blit(carro2, (movXCar2,posYcar2))
    tela.blit(carro3, (movXCar3,posYCar3))
    
    if not acabou:
        movXCar1 = movXCar1 + random.randint(0,9)
        movXCar2 = movXCar2 + random.randint(0,9) 
        movXCar3 = movXCar3 + random.randint(0,9)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
            

        # Contador de distância
    distanciaPixel = 0

    if movXCar1 >= movXCar2 and movXCar1 >= movXCar3:
        winner = 'Vermelho'
        if movXCar2 >= movXCar3:  # se o carro amarelo é o segundo colado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar2)

    elif movXCar2 >= movXCar1 and movXCar2 >= movXCar3:
        winner = 'Amarelo'
        if movXCar1 >= movXCar3:  #se o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar1 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)

    else:  #o carro azul é o vencedor
        winner = 'Azul'
        if movXCar1 > movXCar2:  #o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar3 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)
        else:  #o carro amarelo é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar1)

    #textos winners
    fonte = pygame.font.Font('freesansbold.ttf',20)#ttf é o arquivo da font
    textoWinner = fonte.render(f'{winner} está {distanciaPixel} pixels na frente do carro {secondPlace}', True, branco)
    tela.blit(textoWinner, (180,20))

    fonte = pygame.font.Font('freesansbold.ttf',20)#ttf é o arquivo da font
    textoSegundo = fonte.render(f'{secondPlace} está {distancia_segundo_terceiro} pixels na frente do carro {thirdPlace}', True, branco)
    tela.blit(textoSegundo, (180, 40))
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYcar1 = 330
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYcar2 = 410

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 490
        
    fonte = pygame.font.Font('freesansbold.ttf',60)#ttf é o arquivo da font
    textoVermelho = fonte.render('Vermelho Ganhou!', True, branco)
    textoAmarelo = fonte.render('Amarelo Ganhou!', True, branco)
    textoAzul = fonte.render('Azul Ganhou!', True, branco)
        
    if posYcar1 == 330 and movXCar1 >= 900 and (movXCar1 > movXCar2 and movXCar1 > movXCar3):
        tela.blit(textoVermelho, (270,70))
        acabou = True
        
    elif posYcar2 == 410 and movXCar2 >= 900 and (movXCar2 > movXCar1 and movXCar2 > movXCar3):
        tela.blit(textoAmarelo, (270,180))
        acabou = True

    elif posYCar3 == 490 and movXCar3 >= 900 and (movXCar3 > movXCar1 and movXCar3 > movXCar2):
        tela.blit(textoAzul, (270,180))
        acabou = True
        
    if acabou:
        tela.fill(preto)
        novo_fundo = pygame.image.load('recursos/finalbackground.png')
        tela.blit(novo_fundo, (0, 0))

        fonte_final = pygame.font.SysFont('arial', 30)
        distancia_primeiro_segundo = abs(movXCar1 - movXCar2) if winner == 'Vermelho' and secondPlace == 'Amarelo' or winner == 'Amarelo' and secondPlace == 'Vermelho' else abs(movXCar1 - movXCar3) if winner == 'Vermelho' else abs(movXCar2 - movXCar3)
        distancia_segundo_terceiro = abs(movXCar2 - movXCar3) if thirdPlace == 'Azul' else abs(movXCar1 - movXCar2)

        # Textos para cada colocação com distâncias
        texto_vencedor_final = fonte_final.render(f'1º lugar: Carro {winner}', True, branco)
        texto_distancia_1_2 = fonte_final.render(f'Distância para o 2º lugar: {distancia_primeiro_segundo} pixels', True, branco)
        texto_segundo_final = fonte_final.render(f'2º lugar: Carro {secondPlace}', True, branco)
        texto_distancia_2_3 = fonte_final.render(f'Distância para o 3º lugar: {distancia_segundo_terceiro} pixels', True, branco)
        texto_terceiro_final = fonte_final.render(f'3º lugar: Carro {thirdPlace}', True, branco)

        tela.blit(texto_vencedor_final, (100, 100)) 
        tela.blit(texto_distancia_1_2, (100, 160))  
        tela.blit(texto_segundo_final, (100, 220))  
        tela.blit(texto_distancia_2_3, (100, 280))  
        tela.blit(texto_terceiro_final, (100, 340)) 
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    