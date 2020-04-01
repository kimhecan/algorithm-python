def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    # 반쪽 두개의 각 인덱스
    i = 0
    j = 0

    # 합쳐지는 리스트의 인덱스
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i+= 1
      else:
        arr[k] = right[j]
        j+= 1
      # move to the next slot
      k += 1
    
    # For all the remaining values
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
      
    return arr

print(mergeSort([8,9,6,5,4,7,1,2,3]))