"""
탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
자료구조(Data Structure)란 ‘데이터를 표현하고 관리하고 처리하기 위한 구조’
오버플로(Overflow)는 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입
언더플로(Underflow)는 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제

스택(Stack)은 선입후출(First In Last Out)구조 또는 후입선출(Last In First Out)구조
-> append(), pop()
큐(Queue)는 선입선출(First In First Out)구조
-> append(), popleft()
* 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용

DFS: 깊이 우선 탐색 -> stack 자료구조에 기초함, 재귀함수 이용
BFS: 너비 우선 탐색 -> 가까운 노드부터 탐색하는 알고리즘, 선입선출 방식인 큐 자료구조를 이용
"""

# 재귀함수
# 최대공약수
def gcd(a,b):
    if a % b==0:  # 종료조건
        return b
    else:
        return gcd(b, a % b)

# DFS:rlvdldntjs xkator

# DFS 메서드 정의
def dfs(graph, v, visited):
# 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
    [],         # 0, 인덱스를 직관적으로 사용하기 위해 존재
    [2, 3, 8],  # 1과 연결된 노드
    [1, 7],     # 2와 연결된 노드
    [1, 4, 5],  # 3과 연결된 노드
    [3, 5],     # 4와 연결된 노드
    [3, 4],     # 5와 연결된 노드
    [7],        # 6과 연결된 노드
    [2, 6, 8],  # 7과 연결된 노드
    [1, 7]      # 8과 연결된 노드
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)


# 음료수 얼려먹기
n,m = map(int,input().split())  # n, m 공백으로 구분하여 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))    # 0, 1