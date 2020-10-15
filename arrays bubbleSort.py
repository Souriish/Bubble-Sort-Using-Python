def bubbleSort(arr):
    o=len(arr)

    for i in range (o-1):
        for j in range (0, o-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]

arr=[9,1,2,7,5,8,6,4,0]

bubbleSort(arr)

print("Array in descending order:")
for i in range (len(arr)):
    print (arr[i])
