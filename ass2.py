print("""
####
#name: Thomas Williamson
#Student Id: 588206
#CMPT360 spring 2021
#assignment #2
#title: quick sort
#####
""")
#recive input
##inp = input("input:\n").split(", ")
###start list
##arr = []
###convert input to integer list
##for i in inp:
##    arr.append(int(i))
##print("\n\noutput:")
import random
num = int(input("give the number of random numbers to sort: "))
arr = []
for i in range(num):
        arr.append(random.randint(0,10000))
print("input")
print(arr)
print("\n\n")
#define function quickSortMain, input:integer array, calls quickSort() with min set to 0 and max set to length of array
def quickSortMain(arr):
    arr = quickSort(arr, 0, len(arr))
    return(arr)
#define function quickSort, begins quicksort
def quickSort(arr, low, high):
    if low<high:
        pivotL = partition(arr,low,high)
        quickSort(arr, low,pivotL)
        quickSort(arr, pivotL+1, high)
    return arr
#define partition, partition is part of quickSort
def partition(arr, low, high):
    pivot = arr[low]
    leftwall = low
    for i in range(low +1, high):
        if arr[i]< pivot:
            tem = arr[i]
            arr[i] = arr[leftwall]
            arr[leftwall] = tem
            leftwall = leftwall + 1
    arr[leftwall] = pivot    
    return(leftwall)

#prints sorted array from input
print(quickSortMain(arr))
