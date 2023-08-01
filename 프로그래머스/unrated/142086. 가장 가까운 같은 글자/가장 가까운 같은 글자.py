def solution(s):
    answer = []
    last_index = {}  # 각 글자가 마지막으로 나온 위치를 저장하는 딕셔너리

    for i in range(len(s)):
        char = s[i]
        if char not in last_index:  # 해당 글자가 처음 나온 경우
            answer.append(-1)  # 자신보다 앞에 같은 글자가 없으므로 -1을 추가
        else:  # 해당 글자가 이미 나온 경우
            answer.append(i - last_index[char])  # 현재 위치와 해당 글자가 마지막으로 나온 위치의 차이를 추가

        last_index[char] = i  # 현재 글자의 위치를 딕셔너리에 업데이트

    return answer