from Queue import Queue
import TestFunction as test
import Functions as func
import pygame
import sys
import random as rand

tempo_inicial = func.initialTime()


amount = int(input("Digite quantas pessoas: "))

queue = func.createQueue(amount)

#Testando se ele reconhece dois objetos e funcionou
#if queue.getFirstNode == queue.getFirstNode:
#    print("deu")

angulo_soma = 360 / amount
angulo = 0


#Largura e altura
len, height = 800, 600
#posição do circulo
position = (0, 0)

#Setando a posição dos circulos
func.setPos(queue, angulo, position, len, height, angulo_soma)

test.printPosQueue(queue)

#Inicializar o pygame
pygame.init()
#Criar janela
window = pygame.display.set_mode((len, height))



color = (255, 0 ,0)

finished = False

radius = 30
#objeto que vai percorrer a lista e quando o tempo acabar ele vai excluir em quem parou
potato = queue.getFirstNode()
timetodelete = rand.randint(5,8)
#Loop principal:
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #position = newPos(angulo, position)

        aux = queue.getFirstNode()

        if func.getTime(tempo_inicial) > 1 and queue.getSize() > 1:
            potato = potato.next

        #Preencher a janela com uma cor de fundo
        window.fill((255, 255, 255))
        for i in range(0, queue.getSize()):
            pygame.draw.circle(window, color, aux.value.getPos(), radius)
            if queue.getSize() > 1:
                aux = aux.next
            
            #angulo += angulo_soma
            #position = newPos(angulo, position)
        if finished == False:    
            if func.getTime(tempo_inicial) > timetodelete:
                queue.deQueue(potato.value)
                tempo_inicial = func.initialTime()
                timetodelete = rand.randint(2,4)

        angulo = 0

        if queue.getSize() == 1:
            finished = True
            print("Temos um vencedor!")
        

        pygame.display.update()
        

#queue = func.CriarFila(10)







