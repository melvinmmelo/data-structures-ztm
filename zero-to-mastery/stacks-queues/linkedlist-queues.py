class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue():
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    if self.first == None:
      return None
    print(self.first.data)

  def enqueue(self, data):
    node = Node(data)
    if self.first == None:
      self.first = node
      self.last = node
    else:
      self.last.next = node
      self.last = node

    self.length +=1

  def dequeue(self):
    if self.first == None:
      return None
    
    self.first = self.first.next
    self.length -=1

  def printList(self):
    arr = []
    current = self.first
    while current != None:
      arr.append(current.data)
      current = current.next

    print(arr, "Length: ", self.length)



myStack = Queue()
myStack.peek()
myStack.enqueue("Melvin")
myStack.enqueue("Abo")
myStack.enqueue("Apple")
myStack.dequeue()
myStack.dequeue()
myStack.dequeue()


myStack.printList()


# Melvin -> 1st to get
# Abo
# Apple
# Kris -> Last to get
