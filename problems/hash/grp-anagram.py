import collections

def grpAnagram(strs):
  ans = collections.defaultdict(list)

  for s in strs:
    count = [0] * 26;
    for c in s:
      count[ord(c) - ord('a')] += 1
    ans[tuple(count)].append(s)
  return ans.values()

s2 = ["eat","tea","tan","ate","nat","bat"]
print(grpAnagram(s2))

l = [3,2,1]
print(tuple(l))
