nemo = ['test', 'nemo', 'naame', 'neadi']

def findNemo(array):
  for x in array:
    if x == 'nemo':
      print('Found nemo.')
      break

findNemo(nemo)