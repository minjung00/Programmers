def solution(s):
    # 문자열 s를 내림차순으로 정렬 -> join으로 문자열 연결해서 반환
    return ''.join(sorted(s, reverse=True))