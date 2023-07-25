def solution(strings, n):
    # sorted 함수 -> strings를 n번째 글자를 기준으로 오름차순 정렬
    # key -> n번째 글자를 먼저 기준으로 정렬, 
    ##       n번째 글자가 같은 문자열이 여러 개라면 사전순으로 앞선 문자열이 먼저 오도록 정렬
    # 문자열 x를 입력 받아서 (x의 n번째 글자, 문자열x)를 반환
    sorted_strings = sorted(strings, key=lambda x: (x[n], x))

    return sorted_strings