def solution(s, n):
    answer = ''
     
    for char in s:
        # 대문자인 경우
        if char.isupper(): 
            ## ord() 함수로 알파벳의 유니코드 값 출력
            ## chr() 함수로 다시 문자열로 변환
            ## 'A'부터 시작하여 n만큼 민 뒤, 알파벳 개수인 26으로 나눈 나머지
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
       # 소문자인 경우
        elif char.islower():  
            ## 'a'부터 시작하여 n만큼 민 뒤, 알파벳 개수인 26으로 나눈 나머지
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        # 공백인 경우 그대로 유지
        else:
            new_char = char
            
        # 시저암호를 적용한 결과를 answer에 추가   
        answer += new_char

    return answer