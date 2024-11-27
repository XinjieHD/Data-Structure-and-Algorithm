class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distances = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if distances[nx][ny] > distances[x][y] +1:
                        distances[nx][ny] = distances[x][y] + 1
                        queue.append((nx, ny))

        return distances
