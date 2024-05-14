import sys
input = sys.stdin.readline
result = 0

def merge_sort(array):
    global result
    if len(array) <= 1:
        return array
    m = len(array)//2   # 몫만 취함
    left = merge_sort(array[:m])
    right = merge_sort(array[m:])

    i,j,k, = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            result += len(left)-i
            j += 1
        k+=1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
A = list(map(int,input().split()))

A.insert(0,0)
merge_sort(A)
print(result)