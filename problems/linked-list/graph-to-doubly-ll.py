class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, data):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
      self.length = 1
    else:
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
      self.length +=1


  def prepend(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head.prev = newNode
    self.head = newNode
    self.length +=1

  def printList(self):
    arr = []
    current = self.head
    while current != None:
      # print("Current Node", current.data, " Current Node Prev ", current.prev.data, " Current Node Next ", current.prev.data)
      arr.append(current.data)
      current = current.next

    print(arr, "Length: ", self.length)

  def reversePrint(self):
    arr = []
    current = self.tail
    while current != None:
      arr.append(current.data)
      current = current.prev

    print(arr, "Length: ", self.length)

  def printl(self):
    temp = self.head
    while temp != None:
      print(temp.data , end = ' ')
      temp = temp.next
    print('Length = '+str(self.length))

  def insert(self, index, data):
    new_node = Node(data)
    if index>=self.length:
      self.append(data)
      return

    if index == 0:
      self.prepend(data)
      return

    # leader is before the index
    # kaya may -1 sa parameter
    leader = self.traverseToIndex(index-1)
    leader.next.prev = new_node
    new_node.next = leader.next
    new_node.prev = leader
    leader.next = new_node
    self.length+=1

  def traverseToIndex(self, index):
    counter = 0
    leader = self.head
    while counter != index:
      leader = leader.next
      counter+=1
    return leader

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
      self.length-=1
      return
    else:
      index -=1

    if index >= self.length:
      print("Node index not found." , index)
      return

    leader = self.traverseToIndex(index)
    unwanteNode = leader.next
    leader.next = unwanteNode.next
    unwanteNode.next.prev = leader

    self.length-=1



l = DLinkedList()
l.append(1)
l.append(10)
l.append(19)
l.append(8)
l.prepend(69) # prepend add at the beginning
l.insert(1, 55)


l.printList()
