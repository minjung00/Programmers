def solution(s):
    length = len(s)  # 단어의 길이 구하기
    mid = length // 2  # 가운데 인덱스 계산

    if length % 2 == 0:  # 단어의 길이가 짝수인 경우
        return s[mid - 1:mid + 1]  # 가운데 두글자 반환
    else:  # 단어의 길이가 홀수인 경우
        return s[mid]  # 가운데 글자 반환