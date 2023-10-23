from Queue import Queue


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
        print(fila.getFirst())
        fila.dequeue()
    