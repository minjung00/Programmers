def solution(a, b):
    # a,b 중 작은 수를 start, 큰 수를 end로 설정
    start = min(a, b)
    end = max(a, b)

    # start부터 end까지의 모든 정수의 합 계산
    answer = sum(range(start, end + 1))

    return answer