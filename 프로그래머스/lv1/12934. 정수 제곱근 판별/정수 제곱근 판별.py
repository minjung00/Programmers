def solution(n):
    # x = n의 제곱근
    x = int(n**(1/2))
    # n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴
    if n == x**2:
        return (x+1)**2
    # 아니라면 -1을 리턴
    else:
        return -1