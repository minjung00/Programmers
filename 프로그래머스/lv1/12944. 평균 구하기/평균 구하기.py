def solution(arr):
    ### 코드 설계
    ## 1. 문자열이 아닌 경우
    ## 2. 배열의 합 -> 평균 계산
    
    # 문자열이 아니면 0 반환
    if not arr:
        return 0
    
    total = sum(arr)  # 배열 요소의 합
    average = total / len(arr)  # 합을 개수로 나눠서 평균 계산
    return average # 배열의 평균값 return