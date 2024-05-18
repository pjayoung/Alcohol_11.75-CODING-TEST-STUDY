import sys

Datanum = int(sys.stdin.readline())
Unsort_list = []
for _ in range(Datanum):
    Unsort_list.append(int(sys.stdin.readline()))

def Sort(Unsort_list):
    if len(Unsort_list) < 2:
        return Unsort_list
    
    mid = len(Unsort_list)//2
    left = Sort(Unsort_list[:mid])
    right = Sort(Unsort_list[mid:])
    return Merge(left, right)

def Merge(left, right):
    i, j = 0, 0
    Sort_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            Sort_list.append(left[i])
            i += 1
        else:
            Sort_list.append(right[j])
            j += 1
    while i < len(left):
        Sort_list.append(left[i])
        i += 1
    while j < len(right):
        Sort_list.append(right[j])
        j += 1
    return Sort_list

for i in Sort(Unsort_list):
    print(i)
