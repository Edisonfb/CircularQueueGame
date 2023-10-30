from Queue import Queue
import TestFunction as test
import Functions as func
import pygame
import sys
import math as mt

def newPos(angle, position):
    coord_x = (180 * mt.cos(mt.radians(angle)) + (len / 2) )
    coord_y = (180 * mt.sin(mt.radians(angle)) + (height/ 2) )
    
    return (coord_x, coord_y)

amount = int(input("Digite quantas pessoas: "))

#Inicializar o pygame
pygame.init()

#Largura e altura
len, height = 800, 600
window = pygame.display.set_mode((len, height))

angulo_soma = 360 / amount
angulo = 0


color = (255, 0 ,0)

#posição do circulo
position = (0, 0)

radius = 30

#Loop principal:
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        position = newPos(angulo, position)

        #Preencher a janela com uma cor de fundo
        window.fill((255, 255, 255))
        for i in range(0, amount):
            pygame.draw.circle(window, color, position, radius)

            angulo += angulo_soma
            position = newPos(angulo, position)
            
            

        angulo = 0

        pygame.display.update()
        

#queue = func.CriarFila(10)







