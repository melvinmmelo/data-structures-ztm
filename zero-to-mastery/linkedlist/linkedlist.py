from itertools import count
from pkg_resources import safe_extra


class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList():
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
      self.tail.next = newNode
      self.tail = newNode
      self.length +=1


  def prepend(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode

    self.length +=1

  def printList(self):
    arr = []
    current = self.head
    while current != None:
      arr.append(current.data)
      current = current.next

    print(arr, "Length: ", self.length)


  def printList(self):
    arr = []
    current = self.head
    while current != None:
      arr.append(current.data)
      current = current.next

    print(arr, "Length: ", self.length)
    return arr

  def printInReverse(self):
    arr = self.printList()
    counter = self.length-1
    while counter >= 0:
      print(arr[counter])
      counter -=1



  def convertToArr(self):
    arr = []
    current = self.head
    while current != None:
      arr.append(current.data)
      current = current.next

    return arr

  def printl(self):
    temp = self.head
    while temp != None:
      print(temp.data , end = ' ')
      temp = temp.next
    print('Length = '+str(self.length))

  def insert(self, index, data):
    new_node = Node(data)
    i = 0
    temp = self.head

    if index>=self.length:
      self.append(data)
      return

    if index == 0:
      self.prepend(data)
      return

    while temp != None:
      if i == index:
        prev.next = new_node
        new_node.next = temp
        self.length+=1
        break
      prev = temp
      temp = temp.next
      i+=1

  def insert2(self, index, data):
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
    nextToNewNode = leader.next
    leader.next = new_node
    new_node.next = nextToNewNode
    self.length+=1

  def traverseToIndex(self, index):
    if index > self.length:
      return False

    counter = 0
    leader = self.head
    while counter != index:
      leader = leader.next
      counter+=1

    print(f"The leader is {leader.data}")
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
    self.length-=1

  def reverse(self):
    prev = None
    self.tail = self.head
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp

    self.head = temp


l = LinkedList()
l.append(1)
l.append(10)
l.append(16)
l.append(88)


# l.insert2(5, 16)
# l.insert2(5, 88)

# l.printList()

# l.remove(0)
# l.printList()


# l.remove(6)
# l.reverse()
l.printList()

l.printInReverse()
#sl.traverseToIndex(18)