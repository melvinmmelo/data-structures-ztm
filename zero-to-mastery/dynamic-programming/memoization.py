"""
  This is Dynamic Programming
  Use in long computational
  Efficiency
  Optimizing something using a cache - cache is a basically a storage/dictinary


  best example is fibo in recursion way
    FIBO USING RECURSIVE IS O (2*n) -> O (n)

  You can think dynamic programming
        Divide and Conquer + Memoization

  Steps to follow for identifying if DP is applicable
      1. Can be divided into sub problem
      2. Recusive Solution
      3. Are theere repetitive subproblems?
      4. Memoize subproblems
      5. Demand a raise from your boss


"""

# 1

cache = {}
def memoizatonAddTo(n):
  if n in cache:
    return n
  else:
    print("long time")
    cache[n] = n +80
    return n


# 2
def memoization2AddTo():
  cache = {}

  def memoized(n):
    if n in cache:
      return n
    else:
      print("long time")
      cache[n] = n +80
      return n
  return memoized


memo = memoization2AddTo()
print(memo(7))
print(memo(7))
print(memo(7))
print(memo(7))
print(memo(5))
print(memo(5))
print(memo(5))




# print(memoization2AddTo(5))
# print(memoization2AddTo(5))
# print(memoization2AddTo(5))
