N, M = map(int, input().split())

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
water_basket = [list(map(int, input().split())) for _ in range(N)] 
moves = [list(map(int, input().split())) for _ in range(M)]
    
for d, s in moves:
    cloud2 = []
    for i in range(len(cloud)):
        x, y = cloud[i][0], cloud[i][1]
        x2, y2 = (x + dx[d] * s) % N, (y + dy[d] * s) % N 
        water_basket[x2][y2] += 1
        cloud2.append((x2,y2))
          
    cloud = []
    
    for x, y in cloud2:
        cnt = 0
        for d in range(2, 9, 2): 
            x2, y2 = x + dx[d], y + dy[d]
            if (x2 in range(N) and y2 in range(N)) and water_basket[x2][y2] > 0 :
                cnt += 1
        water_basket[x][y] += cnt
        
    for x in range(N):
        for y in range(N):
            if water_basket[x][y] >=2 and (x,y) not in cloud2:
                cloud.append((x,y))
                water_basket[x][y] -= 2
    
answer = 0
for x in range(N):
    for y in range(N):
        answer += water_basket[x][y]
    
print(answer)