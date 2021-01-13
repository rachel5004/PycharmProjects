def SelsctSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr


num = [1,10,5,8,7,6,4,3,2,9]
print(SelsctSort(num))