def merge(ar1, ar2):
  i = 0
  j =0
  mL = []


  while i<len(ar1) and j<len(ar2):
    if ar1[i] <= ar2[j]:
      mL.append(ar1[i])
      i+=1

    elif ar2[j] < ar1[i]:
      mL.append(ar2[j])
      j+=1

  return mL+ar1[i:]+ar2[j:]

ar1 = [0,1,3]
ar2 = [2,4,5,6,7,8]
print(merge(ar1, ar2))