from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n+1)]
distance = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(n):
    data = list(map(int,input().split()))  # 리스트 형태로 받음
    index = 0  # 인덱스 0부터 시작 -> 0은 노드 번호
    S = data[index]  # S에 노드 번호 넣어주고
    index += 1   # 연결점들 찾기 시작 
    while True:   # break 될 때까지 계속 반복
        E = data[index]   # 노드 번호 
        if E == -1:   # -1은 종료 신호
            break
        V = data[index+1]    # 가중치(거리)
        A[S].append((E,V))  # 튜플 형태로 A 인접 리스트에 저장
        index += 2  # 가중치 건너뛰고 그 다음 노드 출력

def BFS(v):
    queue = deque()
    queue.append(v)   # 현재 노드 큐에 저장
    visited[v] = True   # 현재 노드 방문 저장
    while queue:
        now_Node = queue.popleft()    # 현재 노드 빼내고
        for i in A[now_Node]:     # 그 노드와 인접한 것들 찾아보기
            if not visited[i[0]]:    # 만약에 아직 방문하지 않았다면 (i[0] 형태인 이유! 아까 튜플로 받아서 i[0]이 노드, i[1]이 가중치)
                visited[i[0]] = True  # 방문 저장
                queue.append(i[0])  # 큐에 넣기
                distance[i[0]] = distance[now_Node] + i[1]  # 거리는 현재 노드의 거리와 인접한 노드의 거리값 더해서 업데이트

BFS(1)   # 임의의 점으로 시작
Max = 1   # 맥스값 1로 지정

for i in range(2, n+1):   # 내가 1부터 시작했으니까 이미
    if distance[Max] < distance[i]:   # 맥스값보다 더 큰 값이 나오면
        Max = i    # 멕스값 업데이트

distance = [0]*(n+1)
visited = [False]*(n+1)
BFS(Max)   # 거리와 방문 리스트 초기화 후 max 값에서 다시 시작한 후
distance.sort()   # 거리를 구하기
print(distance[n])   # 가장 마지막에 있는 값이 가장 긴 값