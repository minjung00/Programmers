# 가로의 길이가 n, 세로의 길이가 m인 직사각형 출력하는 함수
def solution(n, m):
    for _ in range(m): # m번 반복
        print('*' * n) # n 만큼 * 출력
        
# 표준 입력으로 두 개의 정수 n과 m을 받음
n, m = map(int, input().split())
 
# 직사각형 출력
solution(n, m)
    
    