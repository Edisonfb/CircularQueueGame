from Queue import Queue
from Circle import Circle

def CriarFila(amount):
    queue = Queue()
    aux = Circle()
    for i in range(0, amount):
        queue.enqueue(aux)
    return queue

