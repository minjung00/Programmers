def solution(a, b):
    answer = 0
    # 배열의 길이만큼 반복
    for i in range(len(a)):
        # a와 b의 각 원소를 곱해서 내적 값 더하기
        answer += a[i] * b[i] 
        
    return answer
