import sys
sys.setrecursionlimit(10 ** 6) # 재귀 사용 시 꼭 쓰기
input = sys.stdin.readline

n, m = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)
arrive = False

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[now] = False

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


for i in range(n):
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)