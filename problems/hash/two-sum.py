def twoSum(nums, target):
  mydict = {}

  for i, v in enumerate(nums):
    diff = target - v
    if diff in mydict:
      return [mydict[diff], i]
    mydict[v] = i

nums = [7,2,8,13,1]
target = 9
print(twoSum(nums, target))