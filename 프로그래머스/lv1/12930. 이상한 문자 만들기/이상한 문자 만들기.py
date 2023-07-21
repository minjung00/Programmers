def solution(s):
    # 문자열 초기화
    answer = ''
    # 공백 기준으로 단어별로 분리
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0: # 짝수인 경우
                answer += i[j].upper()
            else: # 홀수인 경우
                answer += i[j].lower()
        answer+= ' ' # 해당 단어 끝에 공백을 추가
    return answer[0:-1] # 최종 결과 문자열에서 마지막 공백을 제거한 뒤 반환
