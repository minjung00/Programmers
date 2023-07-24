def solution(number):
    # 학생들의 수
    n = len(number)
    
    count = 0
    
    # 학생들의 번호를 더해보면서 합이 0이 되는 경우 반환
    for i in range(n - 2): # 첫번째 학생 선택
        for j in range(i + 1, n - 1): # i이후, 두번째 학생 선택
            for k in range(j + 1, n): # j이후, 세번째 학생 선택
                if number[i] + number[j] + number[k] == 0: # 학생들의 번호를 더해서 합이 0인 경우 
                    count += 1

    return count
