def insertion(arr):
  length = len(arr)
  i = 1
  first = arr[0]
  while i < length:
    if arr[i] < first:
      x = arr.pop(i)
      for j in range(0,i):
        if x < arr[j]:
          arr.insert(j, x)
          break
    first = arr[i]
    i+=1

  print(arr)

arr = [6,5,3,1,8,7,2,4]
insertion(arr)