def solution(phone_number):
    # '*'로 가릴 문자열 개수 구하기
    num = len(phone_number) - 4
    # '*'로 가린 문자열(num) + 핸드폰 번호의 마지막 4자리 정답으로 리턴
    answer = '*' * num + phone_number[-4:]
    return answer
