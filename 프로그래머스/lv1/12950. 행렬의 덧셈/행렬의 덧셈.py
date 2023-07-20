def solution(arr1, arr2):
    # 결과를 반환하는 행렬 초기화
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
  
    
    # 행렬의 행,열 길이만큼 반복
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            # 행렬 arr1과 arr2 덧셈 -> 결과 행렬에 저장
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer