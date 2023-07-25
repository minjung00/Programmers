def solution(t, p):
    count = 0
    
    # 문자열 t에서의 인덱스 범위는 (0부터 len(t) - len(p))까지
    for i in range(len(t) - len(p) + 1):
        s = t[i : i + len(p)] # 문자열 t에서 길이가 p와 같은 부분 문자열 자름
        num_s = int(s) # 자른 부분 문자열을 숫자로 변환
        num_p = int(p) # 문자열 p을 숫자로 변환
        
        # 숫자로 변환한 부분 문자열과 p를 비교
        ## 작거나 같으면 반환
        if num_s <= num_p:
            count += 1
            
    return count