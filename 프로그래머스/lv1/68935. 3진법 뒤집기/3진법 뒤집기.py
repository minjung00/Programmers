def solution(n):
    # 3진법 문자열로 변환
    n3 = "" # 3진법으로 변환한 나머지들이 들어갈 문자열 초기화
    while n > 0 :
        n, remainder = divmod(n, 3) # n을 3으로 나눈 몫(n)과 나머지(remainder)를 저장함
        n3 = str(remainder) + n3 # 나머지를 문자열로 변환해서 n3 앞에 붙이기
   
    # 3진법을 뒤집어서 10진법으로 바꾸기
    answer = int(n3[::-1], 3) # int로 10진법으로 변환, 뒤의 3은 3진법이라는 기수를 의미
    
    return answer