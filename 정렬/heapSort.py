def heapify(arr, n, i):
  largest = i
  leftIdx = 2 * i + 1
  rightIdx = 2 * i + 2

  if leftIdx < n and arr[i] < arr[leftIdx]:
    largest = leftIdx
  
  if rightIdx < n and arr[largest] < arr[rightIdx]:
    largest = rightIdx

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def heapSort(arr):
  n = len(arr)

  # Build a maxheap
  for i in range(n//2 - 1, -1, -1):
    heapify(arr, n, i)
  
  # One by One extarct elements
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
  
  return arr


print(heapSort([5,2,3,1,4]))