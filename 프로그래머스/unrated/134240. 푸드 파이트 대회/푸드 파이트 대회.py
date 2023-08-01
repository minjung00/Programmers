def solution(food):
    temp = '' # 왼쪽 선수 음식
    # 0번 음식은 물이기 때문에, 1부터 반복
    for i in range(1, len(food)):
        # 1번 이후의 음식들을 2로 나눈 몫을 구함
        ## 몫만큼 해당 음식을 반복해 문자열로 배치
        temp += str(i) * (food[i]//2)
    return temp + '0' + temp[::-1]