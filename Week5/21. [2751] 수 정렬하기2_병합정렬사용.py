import sys
input = sys.stdin.readline

def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array)//2   # 몫만 취함
    left = merge_sort(array[:m])
    right = merge_sort(array[m:])

    i,j,k, = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
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
A = []

for i in range(n):
    A.append(int(input()))

result = merge_sort(A)

for i in result:
    print(i)
