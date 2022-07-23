class CrazyQueue():
  def __init__(self):
    self.s1 = []
    self.s2 = []

  def peek(self):
    if len(self.s2) > 0:
      print(self.s2[0])
    else:
      print(self.s1[0])

  def push(self, data):
    self.s1.append(data)
    while self.s1:
     self.s2.append(self.s1.pop())

  def pop(self):
    countS2 = len(self.s2)
    while self.s2:
     self.s1.append(self.s2.pop())

    self.s1.pop()

  def printS1(self):
    print("s1 = ", self.s1)

  def printS2(self):
    print("s2 = ", self.s2)


  def empty(self):
    return len(self.s1) == 0



myStack = CrazyQueue()
myStack.push(5)
myStack.push(2)
myStack.push(3)
myStack.peek()
myStack.pop()



#myStack.peek()




# Melvin -> 1st to get
# Abo
# Apple
# Kris -> Last to get
