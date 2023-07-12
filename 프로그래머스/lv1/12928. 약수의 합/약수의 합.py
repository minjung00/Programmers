def solution(n):
    ### 코드 설계
    ## 약수 : n 을 나누었을 때 나머지가 0인 것
    
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0: # 약수 구하기
            answer += i # 약수인 경우에만 answer에 더하기
    return answer