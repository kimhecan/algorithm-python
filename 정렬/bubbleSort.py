def bubleSort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
  
  return arr



print(bubleSort([6,7,5,3,2,1]))