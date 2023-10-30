from Queue import Queue
from Circle import Circle
import math as mt
import time

def createQueue(amount):
    queue = Queue()
    #Ele pega a referencia, então toda a minha fila iria ser um objeto só, caso eu 
    #mudasse em um mudava em todos
    #aux = Circle()
    for i in range(0, amount):
        name = input("digite o nome ")
        queue.enqueue(Circle(name))
    return queue

def newPos(angle, position, lenght, height):
    coord_x = (200 * mt.cos(mt.radians(angle)) + (lenght / 2) )
    coord_y = (200 * mt.sin(mt.radians(angle)) + (height/ 2) )
    
    return (coord_x, coord_y)

def setPos(queue, angle, position, lenght, height, angulo_soma):
    aux = queue.getFirstNode()

    for i in range(0, queue.getSize()):
        value = newPos(angle, position, lenght, height)
        aux.value.setPos(value[0], value[1])
        aux = aux.next
        angle += angulo_soma

def initialTime():
    return time.time()

def getTime(initialtime):
    return (time.time() - initialtime)

def delay(valueToDelay):
    time.sleep(valueToDelay)