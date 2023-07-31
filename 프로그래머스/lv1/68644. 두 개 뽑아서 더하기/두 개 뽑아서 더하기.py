def solution(numbers):
    sum = {numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))}
    answer = sorted(sum)
    return answer

# (1) numbers 배열에서 숫자 선택 -> i
# (2) i 다음 인덱스부터 끝까지 반복해서 다른 숫자 선택 -> j
# (3) 두 수의 합을 sum에 저장함
# (4) sorted로 sum을 오름차순 정렬해서 반환