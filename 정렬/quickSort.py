def quickSort(arr):
  if len(arr) <= 1: return arr
  pivot = arr[len(arr) // 2]
  lessArr, equalArr, bigArr = [], [], []
  for i in arr:
    if i < pivot: lessArr.append(i)
    elif i > pivot: bigArr.append(i)
    else: equalArr.append(i)
  return quickSort(lessArr) + equalArr + quickSort(bigArr)


print(quickSort([9,7,5,6,4,3,1,2,8]))

# n = 2**k 일때를 가정하면 k는 깊이다. k = logn이 되는데 n = 2*3일때 k는 3이되며 각 단계마다 n번 비교하므로 nlogn이다.
# 한쪽으로 쏠리면 n**2