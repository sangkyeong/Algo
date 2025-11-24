from collections import deque
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()

        for a, b in dxy:
            dx = x + a
            dy = y + b
            if 0 > dx or dx >= m or 0 > dy or dy >= n or not matrix[dx][dy]: continue
            matrix[dx][dy] = 0
            q.append((dx, dy))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    m, n, k = list(map(int, input().split()))
    matrix = [[0] * n for _ in range(m)]
    cnt = 0
    
    for _ in range(k):
        a, b = list(map(int, input().split()))
        matrix[a][b] = 1
    for i in range(m):
        for j in range(n):
            if not matrix[i][j]: continue
            bfs(i, j)
            cnt += 1
    print(cnt)