import random

class Queue:
    """A Class that represents the FIFO (first in First out) mehtod of data collation """
    def __init__(self):
        self.queue = []

    #Add An Element to the list
    def enqueue(self, d):
        if d not in self.queue:
            try:
                self.queue.insert(0, d)
                return True
            except ValueError:
                pass
        return False

    #Remove Element from the list
    def dequeue(self):
        #Check the length
        try:
            if len(self.queue) > 0:
                return self.queue.pop()      
            return "eMPTY lIST"      
        except IndexError:
            return "eMPTY lIST"

    #sET A SIZE For the Q
    def qsize(self):
        try:
            return len(self.queue)
        except:
            pass

    # print the contents of the Queue
    def qprint(self):
        if len(self.queue) <= 0:
            print("Defo eMPTY lIST")
        else:
            print(self.queue)


q = Queue()

print(q.enqueue(5)) 
print(q.enqueue(9)) 
print(q.enqueue(5))
print(q.enqueue(34))
print(q.enqueue(433))
print(q.enqueue(43))

print('\n\n')

print(q.qsize())  
q.qprint()

for i in range(10):
    q.enqueue(i*random.randint(i, i ** 10))
q.qprint()

for i in range(1000):  
    q.dequeue() 

print(q.dequeue())

print('\n\n')
print(q.qsize()) 
q.qprint()    
print('\n\n')


