def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        count = 0
        # 약수인 경우 count에 추가
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
                
        # 짝수인 경우 더하기
        if count % 2 == 0:
            answer += num
        # 홀수인 경우 빼기
        else:
            answer -= num

    return answer