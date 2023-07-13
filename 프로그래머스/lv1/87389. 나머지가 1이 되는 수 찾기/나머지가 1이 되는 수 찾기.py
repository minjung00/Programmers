def solution(n):
    x = 1 # 자연수x 1로 초기화
    # 나머지가 1이 되는 x 찾기
    while n % x != 1:
        # 1씩 증가시키면서 나머지 계산 -> 나머지가 1이 되면 반복문 탈출
        x += 1 
    return x