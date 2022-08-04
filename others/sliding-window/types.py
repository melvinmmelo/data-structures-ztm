
# understanding and coding the sliding window


# The Fixed Sliding Windows

def fixed_sliding_window(arr, k):
  s_ini_arr = sum(arr[:k])
  result = [s_ini_arr]
  for i in range(1, len(arr)-k+1):
    s_ini_arr = s_ini_arr - arr[i-1] + arr[i+k-1]
    #s_ini_arr = s_ini_arr + arr[i+k-1]
    result.append(s_ini_arr)

  print(result)


# The Dynamic Sliding Window
def dynamic_sliding_window(arr, x):
  min_len = float('inf')

  start = 0
  end = 0
  c_sum = 0

  while end < len(arr):
    c_sum += arr[end]
    end += 1
    #print(c_sum)

    while start < end and c_sum >= x:
      c_sum -= arr[start]
      start += 1

      min_len = min(min_len, end-start+1)

  print(min_len)

arr = [1,2,3,4,5,6]
# fixed_sliding_window(arr,5)
dynamic_sliding_window(arr, 7)