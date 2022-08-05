def isContainsDuplicate(nums):
  mySet = {}

  for i in range(len(nums)):
    if nums[i] in mySet:
      return True
    mySet[nums[i]] = True


arr = [1,2,3,4,5,6,6]

print(isContainsDuplicate(arr))