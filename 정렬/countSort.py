def countSort(arr):
  count = [0 for i in range(max(arr))]

  for i, item in enumerate(arr):
    count[arr[i] - 1] += 1
  
  return count

print(countSort([1,1,1,3,3,3,1,1,2,2,2,5,3,3,5,5,4,4,4]))