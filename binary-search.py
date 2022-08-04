def search(arr, target):

  mid = len(arr) // 2
  low = arr[0]
  high = arr[len(arr)-1]

  if target > high:
    return False

  if target == arr[mid] or target == low or target == high:
    return target

  if target > arr[mid]:
    return search(arr[mid:], target)

  if arr[mid] > target:
    return search(arr[:mid],target)


arr =  [3, 4, 5, 6, 7, 8, 9]
target = 9

print(search(arr, target))