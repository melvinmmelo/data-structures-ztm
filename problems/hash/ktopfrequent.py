def topKFrequent(arr, k):
  count = {}
  freq = [[] for i in range(len(arr) + 1)]
  # print(freq)

  for n in arr:
    count[n] = 1 + count.get(n,0)

  # print(count.items())

  for n, c in count.items():
    # print(n)
    freq[c].append(n)

  # print(freq)

  res = []
  for i in range(len(arr)-1,0,-1):
    for n in freq[i]:
      res.append(n)
    if len(res) == k:
      return res


numsm = [1,1,1,2,2,3,89,100,100,100,100]
nums2 = [1,2,3,4,5,6]

k = 2
rs = topKFrequent(numsm, k)
print(rs)