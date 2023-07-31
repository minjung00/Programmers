def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        
        # (1) 배열 array의 i번째 숫자부터 j번째 숫자까지 자르기
        array_1 = array[i-1:j]
        
        # (2) 배열 array_1 정렬하기
        array_2 = sorted(array_1)
        
        # (3) 정렬한 배열 array_2에서 k번째에 있는 수 구하기
        k_num = array_2[k-1]
        
        # 결과 배열에 추가
        answer.append(k_num)
    
    return answer