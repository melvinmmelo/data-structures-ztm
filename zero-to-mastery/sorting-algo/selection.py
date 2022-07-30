def selection(arr):
  loopCount = 0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[j] < arr[i]:
        temp = arr[loopCount]
        arr[loopCount] = arr[j]
        arr[j] = temp

    loopCount += 1

  print(arr)

arr = [8,6,5,0,4,3,2]
selection(arr)