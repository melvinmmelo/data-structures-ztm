x = 0
def fiboMaster():
  cache = {}

  def fibo(n):
    x+=1
    if n in cache:
      return cache[n]
    else:
      if n < 2:
        return n
      else:
        cache[n] = fibo(n-1) + fibo(n-2)
        return cache[n]



fibMaster = fiboMaster()
fibMaster(8)
print(f"Calculations: {x}")
#factorialLoop(factorialOf)