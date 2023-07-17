def solution(arr, divisor):
    #  divisor로 나누어 떨어지는 값 저장할 리스트
    answer = []
    
     # array의 각 element 중 divisor로 나누어 떨어지는 값
    for num in arr:
        if num % divisor == 0: # divisor로 나누어 떨어지는 값
            answer.append(num) # 그 값을 리스트에 추가
    
    # divisor로 나누어 떨어지는 element가 하나도 없다면
    if not answer:
        return [-1] # 배열에 -1을 담아 반환
    
    # 값을 오름차순으로 반환
    return sorted(answer)