class Node():
  def __init(self, data):
    self.data = data
    self.next = None

class Stack():
  def __init(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top

  def push(self, data):
    node = Node(data)
    if self.top == None:
      self.bottom = node
      self.bottom.next = node
      self.top = node
    else:
      prev = self.top
      self.top = node
      prev.next = node

    self.length +=1

  def pop(self):
    print("remove top")



myStack = Stack()
myStack.push("Facebokk")
myStack.push("Apple")
myStack.push("Google")

print(myStack.peek())


# Google -> 1st to get
# Apple
# Facebook -> Last to get
