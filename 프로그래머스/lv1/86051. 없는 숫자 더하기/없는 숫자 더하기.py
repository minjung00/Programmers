def solution(numbers):
    # 0부터 9까지의 숫자를 모두 찾아 더한 수 저장하는 변수 설정
    total = 0

    # numbers에 없는 숫자를 total에 더함
    for i in range(10): # 0~9 반복
        if i not in numbers: # numbers에 없는 숫자
            total += i

    return total