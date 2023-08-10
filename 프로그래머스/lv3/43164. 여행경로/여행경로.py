def solution(tickets):
    answer = []
    graph = {}  # 그래프를 딕셔너리로 구현
    
    for a, b in tickets:
        graph[a] = graph.get(a, []) + [b]  # 출발 공항을 키로, 도착 공항을 값으로 추가
    
    for key in graph:
        graph[key].sort()  # 각 도시의 가능한 도착 공항을 알파벳 순서대로 정렬
    
    def dfs(start):
        nonlocal answer
        if len(answer) == len(tickets) + 1:  # 모든 티켓을 사용한 경우
            return True
        
        if start not in graph:  # 도시에서 더 이동할 수 없는 경우
            return False
        
        for idx, next_airport in enumerate(graph[start]):
            graph[start].pop(idx)  # 사용한 티켓 제거
            answer.append(next_airport)
            if dfs(next_airport):  # 다음 도시로 이동
                return True
            answer.pop()  # 경로가 맞지 않는 경우 티켓과 경로 제거
            graph[start].insert(idx, next_airport)  # 티켓 복원
        
        return False
    
    answer.append("ICN")  # 시작은 "ICN" 공항
    dfs("ICN")
    return answer