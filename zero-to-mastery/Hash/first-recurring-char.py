# one google interview
def simple(arr):
  for x in range(0, len(arr)):
    for k in range(x+1,len(arr)):
      if arr[x] == arr[k]:
        return x
  return 0



def hashTable(arr):
  nums = {}
  for i, x in enumerate(arL):
    if x in nums:
      return (x)
    nums[x] = i



arL = [2,1,1,4,2,4]

print(simple(arL))