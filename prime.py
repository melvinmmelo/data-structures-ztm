int_x = int(6)
factors = []
if (int_x <= 1):
  print(f"{int_x} is not a prime number")
else:
  for factor in range(2,int_x):
      if int_x % factor == 0:
        factors.append(int_x)
  if(len(factors)) == 0:
    print(f"{int_x} is a prime number")
  else:
    print(f"{int_x} is not a prime number. It has the ff factors: {', ' . join(map(str, factors)) }")