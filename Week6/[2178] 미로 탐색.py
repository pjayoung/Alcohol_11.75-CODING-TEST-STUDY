from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int,input().split())
A = [[0]*m for _ in range(n)]   # 왜 여기는 n+1을 안 할까? -> BFS를 (0,0)부터 시작할거니까
visited = [[False]*m for _ in range(n)]

for i in range(n):
    num = list(input())   # 인접 리스트에 들어갈 값 입력 받음 (n개의 행만큼 list로 입력받음)
    for j in range(m):  #m 개의 칼럼만큼
        A[i][j] = int(num[j])  # 어차피 자체로 행렬 안에 넣는 느낌이 되니까 두 줄로 쓸 필요 없음

def BFS(i,j):
    queue = deque()
    queue.append((i,j))   # 문제에서는 (1,1)로 말하지만 여기서는 그냥 (0,0) 부터 시작 (아까 리스트를 n-1, m-1로 만들어서)
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):    # 상하좌우 탐색 (그래서 길이 4)
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m:   # (0,0) ~ (n-1,m-1) 사이에 있을 때
                if A[x][y] != 0 and not visited[x][y]:   # 안에 있는 값이 0이 아니고, 방문한 적이 없다면
                    visited[x][y] = True   # 방문 리스트 업데이트하고
                    A[x][y] = A[now[0]][now[1]]+1   # 안에 값도 업데이트(그 전에 있던 값들 + 1)
                    queue.append((x,y))  # 업데이트한 값을 큐에 넣음

BFS(0,0)
print(A[n-1][m-1])