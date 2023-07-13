def solution(s):
    # 문자열을 소문자로 통일
    s = s.lower()
    # p와 y의 개수가 같은지 비교
    ## 같으면 True, 다르면 False
    return s.count('p') == s.count('y')