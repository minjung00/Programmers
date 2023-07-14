def solution(n):
    # 정수 n 문자열로 변환
    s = str(n)
    # 변환된 문자열을 내림차순으로 배치
    sorted_s = ''.join(sorted(s, reverse = True))
    # 문자열을 정수로 변환
    answer = int(sorted_s)
    return answer