# Function to find the length of the largest subsequence formed by consecutive integers
def findMaxLenSubseq(A): # O(n)

    # construct a set out of input elements
    S = set(A)

    # initialize result by 0
    maxlength = 0

    # do for each element of the input sequence
    for e in A:

        # check if the current element `e` is a candidate for starting a sequence;
        # i.e., the previous element `e-1` doesn't exist in the set
        if (e - 1) not in S:


            # `len` stores the length of subsequence, starting with the current element
            len = 1

            # check for presence of elements `e+1`, `e+2`, `e+3`, … ,`e+len` in the set
            while (e + len) in S:
                len += 1

            # update result with the length of current consecutive subsequence
            maxlength = max(maxlength, len)

    # return result
    return maxlength

def findMaxLenSubseq2(A): # O (n log n)
  B = sorted(A)
  #print(B)
  maxL = 0
  for i in range(len(A)):
    if (i+1) < (len(A)-1) and (B[i+1]-B[i] == 1):
      maxL += 1
  return maxL


A = [3, 2, 6, 1, 0, 7, 5, 7, 6, 8, 9]

print("The length of the maximum consecutive subsequence is:",
    findMaxLenSubseq(A))

# maxlength2 = max(2, 4)
# print(maxlength2)