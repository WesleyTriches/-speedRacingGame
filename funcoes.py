import random, pygame

def posicao_inicial(branco, tela, fundo, carro1, carro2, carro3, movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3):
    tela.fill(branco)  # Pinta de branco
    tela.blit(fundo, (0, 0))  # A imagem de fundo é enviada para a tela na posição (0,0)
    tela.blit(carro1, (movXCar1, posYCar1))  
    tela.blit(carro2, (movXCar2, posYCar2))  
    tela.blit(carro3, (movXCar3, posYCar3))  

def mover_carros(movXCar1, movXCar2, movXCar3, acabou):
    if not acabou:
        movXCar1 += random.randint(0, 9)
        movXCar2 += random.randint(0, 9)
        movXCar3 += random.randint(0, 9)
    return movXCar1, movXCar2, movXCar3

def contador_texto(tela, firstPlace, secondPlace, thirdPlace, distanciaPixel, distancia_segundo_terceiro, branco):
    fonte = pygame.font.Font('freesansbold.ttf', 20)
    textoWinner = fonte.render(f'{firstPlace} está {distanciaPixel} pixels na frente do carro {secondPlace}', True, branco)
    tela.blit(textoWinner, (180, 20))

    fonte = pygame.font.Font('freesansbold.ttf', 20)
    textoSegundo = fonte.render(f'{secondPlace} está {distancia_segundo_terceiro} pixels na frente do carro {thirdPlace}', True, branco)
    tela.blit(textoSegundo, (180, 40))

def carros_segunda_pista(movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3):
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 330

    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 410

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 490

    return movXCar1, movXCar2, movXCar3, posYCar1, posYCar2, posYCar3


