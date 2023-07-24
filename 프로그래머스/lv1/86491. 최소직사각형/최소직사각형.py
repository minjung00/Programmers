def solution(sizes):
    # 가로와 세로 길이의 최댓값을 저장하는 변수
    max_w = max_h = 0
    
    # 가로 길이와 세로 길이를 비교하면서 최댓값과 최솟값 갱신
    for w, h in sizes:
        max_w = max(max_w, max(w, h)) # w와 h중에서 더 큰 값을 최댓값으로 선택
        max_h = max(max_h, min(w, h)) # w와 h중에서  더 작은 값을 최솟값으로 선택
    
    # 지갑의 크기 반환
    return max_w * max_h