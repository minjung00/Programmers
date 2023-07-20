def solution(n, m):
    # 최대공약수 구하기
    def gcd(n, m):
        # m이 0이 되었을 때 n이 최대공약수
        while m != 0:
            # n -> n을 m으로 나눈 나머지
            # m -> 그 전에 n으로 나눈 나머지로 계속 갱신
            n, m = m , n % m 
        return n

    # 최소공배수 구하기
    def lcm(n, m):
        # 두 수의 곱을 최대공약수로 나눈 값 = 최소공배수
        return n * m // gcd(n, m) 
    
    # 결과 반환
    return [gcd(n, m), lcm(n, m)]