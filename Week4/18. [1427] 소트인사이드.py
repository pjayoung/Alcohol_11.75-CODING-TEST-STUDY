import sys
input = sys.stdin.readline

sortList = list(input())

for i in range(len(sortList)):
    value = sortList[i]
    index = i
    for j in range(len(sortList)-1, i, -1):
        if value < sortList[j]:
            value = sortList[j]
            index = j
    sortList[i], sortList[index] = sortList[index], sortList[i]

for i in range(len(sortList)):
    print(sortList[i], end="")

