def max_resources(N, M, grid):
    dp = [[0] * M for _ in range(N)]
    
    # 초기값 설정
    dp[0][0] = grid[0][0]
    
    # 첫 번째 행 초기화
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # 첫 번째 열 초기화
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 나머지 셀들에 대한 DP 수행
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[N-1][M-1]

# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_resources(N, M, grid))
