def solution(N):
    ### 코드 설계
    ## 자연수 N을 문자열(str)로 변환
    
    answer_sum = 0 # 합을 구하는 변수 초기화
    
    for answer in str(N): # N을 문자열(str)로 변환
        answer_sum += int(answer) # 자릿수 정수로 변환
    
    return answer_sum