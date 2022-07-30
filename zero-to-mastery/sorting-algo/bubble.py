def bubble(arr):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[j] < arr[i]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

  print(arr)

arr = [5,9,1,2,7,3,8,2]
bubble(arr)