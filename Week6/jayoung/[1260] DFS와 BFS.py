from collections import deque
import sys
sys.setrecursionlimit(10 ** 6) # 재귀 사용 시 꼭 쓰기
input = sys.stdin.readline

n, m, v = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):   # 인접리스트 생성
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n+1):
    A[i].sort()    # 번호가 작은 노드부터 방문

def DFS(now):    #DFS 재귀 이용 생성
    print(now, end=' ')
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i)

DFS(v)

def BFS(now):
    queue = deque()
    queue.append(now)
    visited[now] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


print()
visited = [False]*(n+1)
BFS(v)