class Stack():
  def __init__(self):
    self.arr = []

  def peek(self):
    if len(self.arr) == 0:
      return None
    print(self.arr[len(self.arr)-1])

  def push(self, data):
    self.arr.append(data)

  def pop(self):
    if len(self.arr) == 0:
      return None
    self.arr.pop()






myStack = Stack()
myStack.push("Facebook")
myStack.push("Amazon")
myStack.push("Apple")
myStack.push("Google")

#myStack.peek()
myStack.pop()
myStack.pop()

# myStack.pop()

#myStack.push("LinkedIn")
myStack.peek()



# Google -> 1st to get
# Apple
# Amazon
# Facebook -> Last to get
