def SelsctSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

def QuickSort(arr,start,end):
    if start >= end: return
    pivot = start
    i = start+1
    j = end
    tmp = 0
    while i<=j:
        while i<=end and arr[i] <= arr[pivot]: i+=1
        while arr[j] >= arr[pivot] and j>start: j-=1
        if i>j:
            tmp = arr[j]
            arr[j] = arr[pivot]
            arr[pivot] = tmp
        else:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
    QuickSort(arr,start,j-1)
    QuickSort(arr,j+1,end)
    return arr

num = [1,10,5,8,7,6,4,3,2,9]
print(QuickSort(num,0,len(num)-1))