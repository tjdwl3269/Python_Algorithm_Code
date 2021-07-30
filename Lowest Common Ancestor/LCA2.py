''' BOJ 11438 '''

import sys
# 시간 초과를 피하기 위한 빠른 입력 함수
input = sys.stdin.readline
# 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
sys.setrecursionlimit(int(1e5)) 
LOG = 21 # 2^20 = 1,000,000

n = int(input())
# 부모 노드 정보
parent_list = [[0] * LOG for _ in range(n + 1)] 
# 각 노드까지의 깊이
depth_list = [0] * (n + 1) 
# 각 노드의 깊이가 계산되었는지 여부
check_list = [0] * (n + 1) 
# 그래프(graph) 정보
graph_list = [[] for _ in range(n + 1)] 

for _ in range(n - 1):
    parent, child = map(int, input().split())
    graph_list[parent].append(child)
    graph_list[child].append(parent)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    check_list[x] = True
    depth_list[x] = depth
    for y in graph_list[x]:
        if check_list[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent_list[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent_list[j][i] = parent_list[parent_list[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상을 찾는 함수
def LCA(a, b):
    # b가 더 깊도록 설정
    if depth_list[a] > depth_list[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if depth_list[b] - depth_list[a] >= (1 << i):
            b = parent_list[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent_list[a][i] != parent_list[b][i]:
            a = parent_list[a][i]
            b = parent_list[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent_list[a][0]

set_parent()

m = int(input())
answers = list()
for i in range(m):
    a, b = map(int, input().split())
    answers.append(LCA(a, b))

for answser in answers:
    print(answser)
