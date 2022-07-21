def reverse(yStr):
  print(type(yStr))
  myList = []
  cL = len(yStr)-1
  while cL >= 0:
    myList.append(yStr[cL])
    cL-=1

  return ''.join(myList)


print(reverse("i am melo"))