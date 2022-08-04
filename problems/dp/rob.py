
def rob(nums):
  dp = [0]*len(nums)
  print(dp)
  if len(nums)==1:
    return nums[-1]
  dp[0] = nums[0]
  dp[1] = nums[1]
  if len(nums)>2:
    dp[2] = dp[0]+nums[2]
  for i in range(3,len(nums)):
    dp[i]=nums[i] + max(dp[i-2],dp[i-3])

  #print(dp)
  return(max(dp[-1], dp[-2]))


nums = [2,7,9,3,1]
print(rob(nums))