def selectSort(arr):
  #배열전체요소를 순차적으로 방문함
  for i in range(len(arr)):
    #가장작은 숫자의 인덱스다.
    minIdx = i
    for j in range(i+1, len(arr)):
      if arr[minIdx] > arr[j]: minIdx = j

    arr[i], arr[minIdx] = arr[minIdx], arr[i]
  
  return arr

print(selectSort([5,3,2,1,7]))

# 선택정렬은 전체를 반복하면서 0~n까지중에 가장 작은 숫자를 0번째로 1~n까지중에 가장 작은 숫자를 1번째로 2~n번째중에 가장 작은 숫자를 2번째로 ...