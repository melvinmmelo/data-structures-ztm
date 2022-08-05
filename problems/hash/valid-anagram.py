def isAnagram(s1, s2):
  if len(s1) != len(s2):
    return False

  ss1, ss2 = {}, {}

  for i in range(len(s1)):
    ss1[s1[i]] = 1 + ss1.get(s1[i], 0)
    ss2[s2[i]] = 1 + ss2.get(s2[i], 0)

  print(ss1)

  return ss1 == ss2




mys1 = "heelo1"
mys2 = "lohee"

print(isAnagram(mys1, mys2))