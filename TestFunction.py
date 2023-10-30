from Queue import Queue
from Circle import Circle

def testQueue():
    test = Queue()

    test.enqueue("a")
    test.enqueue("b")
    test.enqueue("c")
    test.enqueue("d")
    print(test.getSize())
    test.deQueue("t")
    print(test.getSize())
    printQueue(test)
    print(test.getSize())

def printQueue(fila):
    
    for i in range(0, fila.getSize()):
        print(i, " ", fila.getFirst().print())
        fila.dequeue()

def printPosQueue(queue):
    aux = queue.getFirstNode()
    for i in range(0, queue.getSize()):
        print(aux.value.getPos())
        aux = aux.next
    
