def factorialRecursively(n):
  # Base case: 1! = 1
  if n == 1:
      return 1

  # Recursive case: n! = n * (n-1)!
  else:
      return n * factorialRecursively(n-1)

def factorialLoop(num):
  tempNum = num - 1
  ans = num * (num-1)
  while tempNum > 1:
    tempNum-=1
    ans = ans * tempNum
  print(ans)





factorialOf = 1

ans = factorialRecursively(factorialOf)
print(ans)

#factorialLoop(factorialOf)