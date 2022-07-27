def fiboRecursive(n):
  # Base case: n < n
  if n < 2:
    return n
  # Recursive Case
  return fiboRecursive(n-1) + fiboRecursive(n-2)



ans = fiboRecursive(8)
print(ans)

#factorialLoop(factorialOf)