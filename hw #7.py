import time
import random
import sys

sys.setrecursionlimit(10000000)

def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def random_partition(array, low, high):
    # Select random pivot and swap with last element
    pivot_idx = random.randint(low, high)
    array[pivot_idx], array[high] = array[high], array[pivot_idx]
    
    # Use the regular partition function since pivot is now at the end
    return partition(array, low, high)
    


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi)
        quickSort(array, pi, high)
        
def quickSortrandom(array, low, high):
    if low < high:
        pi = random_partition(array, low, high)
        quickSortrandom(array, low, pi)
        quickSortrandom(array, pi, high)
        
 
        
arr = []        
for x in range(1000): 
    arr.append(x)  


def getTimeRandom(arr):
    start = time.time()
    quickSortrandom(arr, 0, len(arr)-1)
    elapsed = time.time() - start
    return elapsed

def getTimeNormal(arr):
    start = time.time()
    quickSort(arr, 0, len(arr)-1)
    elapsed = time.time() - start
    return elapsed

print("Sorted list")
print(f'Last element = pivot: {getTimeNormal(arr)}')
print(f'Random element = pivot: {getTimeRandom(arr)}') 
print("\n")   
print("reverse sorted list")
print(f'Last element = pivot: {getTimeNormal(arr[::-1])}')
print(f'Random element = pivot: {getTimeRandom(arr[::-1])}')
print('\n')

sizes = [500,1000,2000, 10000]
for size in sizes:
    arr2 = []
    for _ in range(size):
        arr2.append(random.randint(0,500))
    print(f'random list with {size} elements:')
    print(f'Last element = pivot:{getTimeNormal(arr2)}')
    print(f'Random element = pivot: {getTimeRandom(arr2)}')
    print("\n")
        
    