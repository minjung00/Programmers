def solution(d, budget):
    d.sort()  # 신청한 금액 배열을 오름차순으로 정렬
    answer = 0 # 부서의 개수를 저장하는 변수
    for cost in d: # 부서별로 신청한 금액안에서 반복
        if budget >= cost: # 신청 금액이 예산보다 작은 경우
            budget -= cost # 신청 금액만큼 예산에서 차감
            answer += 1 # 물품 지원이 가능하니까 부서의 개수 증가
        else:
            break
    return answer