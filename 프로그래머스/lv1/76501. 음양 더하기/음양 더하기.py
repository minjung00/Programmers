def solution(absolutes, signs):
    answer = 0
    
    # absolutes와 signs을 인덱스별로 비교
    for i in range(len(absolutes)):
        if signs[i]: # 배열 signs가 True(+)인 경우 
            answer += absolutes[i] # 배열 absolutes 값을 더함
        else: # 배열 signs가 False(-)인 경우
            answer -= absolutes[i] # 배열 absolutes 값을 뺌
            
    return answer