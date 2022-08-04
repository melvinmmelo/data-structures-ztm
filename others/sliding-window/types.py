
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

arr = [1,2,3,4,5,6]
fixed_sliding_window(arr,5)