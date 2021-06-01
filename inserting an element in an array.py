arr1 = array.array('i', [1, 2, 3])
arr2 = array.array('i', [4, 5, 6])

print(arr1)
print(arr2)

arr3 = arr1 + arr2
print(arr3)

arr1.append(4)
print(arr1)

arr1.insert(0, 10)
print(arr1)

arr1.extend(arr2)
print(arr1)