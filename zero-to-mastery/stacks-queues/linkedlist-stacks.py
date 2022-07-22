class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack():
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    if self.top == None:
      return None
    print(self.top.data)

  def push(self, data):
    node = Node(data)
    if self.top == None:
      self.top = node
      self.bottom = node
    else:
      prev = self.top
      self.top = node
      self.top.next = prev

    self.length +=1

  def pop(self):
    if self.top == None:
      return None

    if self.top == self.bottom:
      self.bottom = None

    self.top = self.top.next
    self.length -=1



myStack = Stack()
myStack.push("Facebook")
myStack.push("Amazon")
myStack.push("Apple")
#myStack.peek()
myStack.pop()
myStack.pop()

#myStack.push("LinkedIn")
myStack.peek()



# Google -> 1st to get
# Apple
# Amazon
# Facebook -> Last to get
