from multiprocessing.dummy import Array

def removeDuplicates(nums : Array):
  if len(nums) > 1:
    k = 0
    for i in range(len(nums)):
      next_num = i + 1
      if next_num < len(nums):
        for j in range(next_num, len(nums)):
          if nums[i] == nums[next_num]:
            k+=1
            nums.pop(next_num)

    #print(nums)
    print(k, nums)

  return

removeDuplicates([0,0,1,1,1,2,2,3,3,4])
