''' BOJ 11437 '''

import sys
# 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
sys.setrecursionlimit(int(1e5))

n = int(input())

# 부모 노드 정보
parent_list = [0] * (n + 1) 
#print(parent) -> n = 5, [0, 0, 0, 0, 0, 0]

# 각 노드까지의 깊이
depth_list = [0] * (n + 1) 
# 각 노드의 깊이가 계산되었는지 여부
check_list = [0] * (n + 1) 
# 그래프(graph) 정보
graph_list = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    # 서로 연결된 정점, (부모, 자식)
    parent, child = map(int, input().split()) 
    graph_list[parent].append(child)
    graph_list[child].append(parent)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수, dfs(1,0)로 시작
def dfs(node_num, depth):
    check_list[node_num] = True
    depth_list[node_num] = depth
    for node in graph_list[node_num]:
        #이미 깊이를 구했다면 넘기기
        if check_list[node]:
            continue
        parent_list[node] = node_num
        dfs(node, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def LAC(a, b):
    # 먼저 깊이(depth)가 동일하도록함
    while depth_list[a] != depth_list[b]:
        if depth_list[a] > depth_list[b]:
            a = parent_list[a]
        else:
            b = parent_list[b]

    # 노드가 같아지도록
    while a != b:
        a = parent_list[a]
        b = parent_list[b]
    
    return a

# 루트 노드는 1번 노드
dfs(1, 0)

m = int(input())
answsers = list()
for i in range(m):
    a, b = map(int, input().split())
    answsers.append(LAC(a, b))

for answser in answsers:
    print(answser)
