def mergesort(arr):
  if len(arr) == 1:
    return arr
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  print('Left {}', format(left))
  print('Right {}', format(right))

  return merge(mergesort(left), mergesort(right))

arr = [99,44,6,2,1,5,63,87,283,4,0]

def merge(left, right):
  lefi = 0
  rigi = 0

merge(arr)