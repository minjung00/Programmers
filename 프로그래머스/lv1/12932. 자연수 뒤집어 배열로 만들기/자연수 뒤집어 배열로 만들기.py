def solution(n):
    # 숫자를 문자열로 변경, 뒤집기
    s = str(n)[::-1]

    # 문자열을 정수로 변환, 리스트에 추가
    answer = [] # 정답 담을 리스트
    for ch in s: # 문자열 정수로 변환
        answer.append(int(ch))
    
    return answer