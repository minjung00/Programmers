def solution(arr):
    answer = []
    
    # 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    for i in range(len(arr)): # 배열의 길이만큼 반복
        # 현재 원소와 이전 원소 비교해서 다른 경우에만 answer 리스트에 추가
        if i == 0 or arr[i] != arr[i-1]: 
            answer.append(arr[i])
        
    return answer