def solution(price, money, count):
    # 총 필요한 놀이기구의 이용금액 초기화
    total = 0
    # 총 필요한 놀이기구의 이용금액 구하기
    for i in range (1, count+1):
        total += price * i
    # 총 이용금액이 현재 가진 금액보다 많으면, 부족한 금액 반환
    if total > money:
        return total - money
    # 부족하지 않으면, 0 반환
    else:
        return 0