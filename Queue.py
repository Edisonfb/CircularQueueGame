class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
        def __repr__(self):
            return '%s -> %s' % (self.value, self.next)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def enqueue(self, value):
        new = Node(value)
        if self.first == None:
            self.first = new
            self.last = self.first
        
        else:
            self.last.next = new
            self.last = new
            self.last.next = self.first

        self.size += 1

    def deQueue(self, value):
        if self.size > 0:
            data = self.first
            for i in range(0, self.size):
                if data.next.value == value:
                    print("Achou um valor igual")
                    data.next = data.next.next
                    self.size -= 1
                    break
                data = data.next
    
    def dequeue(self):
        if self.size > 0:
            self.first = self.first.next
            self.last.next = self.first
            self.size -= 1

    
    def __repr__(self):
        return "[" + str(self.first) + "]"

    def getFirst(self):
        return self.first.value

    def getLastNext(self):
        if self.size > 1:
            return self.last.next.value
        else:
            return self.last.value
        
    def getLast(self):
        return self.last.value
    