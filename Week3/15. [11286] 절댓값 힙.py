from queue import PriorityQueue
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
myqueue = PriorityQueue()
queue_2 = deque()

for _ in range(n):
    queue_2.append(int(input()))

result = []
for _ in range(n):
    request = queue_2.popleft()
    if request == 0:
        if myqueue.empty():
            result.append('0')
        else:
            temp = myqueue.get()
            result.append(str(temp[1]))
    else:
        myqueue.put((abs(request), request))

for i in range(len(result)):
    print(result[i])