from collections import deque

def solution(participant, completion):
    # 참여자 명단을 큐에 저장
    list = deque(participant)
    
    # 완주자 목록을 딕셔너리에 저장
    completion_dict = {}
    for player in completion:
        completion_dict[player] = completion_dict.get(player, 0) + 1

    # 참여자 목록을 순회하면서 완주자 목록에 있는지 확인
    for player in list:
        if player in completion_dict and completion_dict[player] > 0:
            completion_dict[player] -= 1
        else:
            return player