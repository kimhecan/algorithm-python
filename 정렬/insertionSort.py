def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    # 인덱스 i값보다 인덱스 j값이 더 크다면 바꿈
    while j>=0 and arr[j]>key:
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key
  return arr


print(insertionSort([5,3,2,1,7]))

