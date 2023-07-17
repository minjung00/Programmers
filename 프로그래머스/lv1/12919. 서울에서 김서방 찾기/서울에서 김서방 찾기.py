def solution(seoul):
    # seoul에서 "Kim"의 위치 x 찾가
    x = seoul.index("Kim")
    # x를 포맷하여 결과 문자열 반환
    return "김서방은 {}에 있다".format(x)