def solution(arr):
    ### 코드 설계
    ## 배열의 합 -> 평균 계산
    
    total = sum(arr)  # 배열 요소의 합
    average = total / len(arr)  # 합을 개수로 나눠서 평균 계산
    return average # 배열의 평균값 return