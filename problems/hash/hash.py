# checking if array has zero sum in sub array/s


# first solution is 0 (n2)

# has zero sum
def hasZeronSum(nums): # 0 (n) time complexity
  s = set()

  s.add(0)

  total = 0

  for i in nums:
    total += i

    if total in s:
      return True

    s.add(total)

  print(s)

  return False

nums = [4, -6, 3, -1, 4, 2, 7]

if hasZeronSum(nums):
    print('Sublist exists')
else:
    print('Sublist does not exist')