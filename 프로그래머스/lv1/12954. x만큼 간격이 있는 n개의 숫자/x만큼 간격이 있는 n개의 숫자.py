def solution(x, n):
    answer = [] # 리스트 초기화
    
    # x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 만드는 반복문
    for i in range(n):
        # x부터 x씩 증가하는 숫자
        answer.append(x * (i + 1))
    return answer