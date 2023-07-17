def solution(n):
    answer = "수박" * (n // 2)  # "수박" 패턴 생성
   
    # n이 짝수이면 그냥 n // 2만큼 "수박" 출력하면 됨
    if n % 2 == 1:  # n이 홀수인 경우
        answer += "수"  # 패턴의 마지막에 "수" 추가

    return answer