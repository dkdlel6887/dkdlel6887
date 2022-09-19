# N//500 + N%500//100 + N%500%100//50 + N%500%100%50//10
"""
coin_types = [500, 100, 50, 10]
count = 0
n = int(input('비용(원): '))
for coin in coin_types:
    count += n // coin
    n = n % coin
print(f'{count}개')
"""
#1 큰 수의 법칙
from random import randint

nums = []   #N개의 랜덤한 자연수를 갖는 리스트
condition = input('입력: ')
N, M, K = condition.split()
# 위 2줄을 한줄로 표현하고 정수형 변환하면 다음과 같다.
# >>> n, m, k = map(int, input().split())

for i in range(int(N)): # randint 함수로 임의의 값 5개 받기
    num = randint(1,10001)
    nums.append(num)
    print(num, end=' ')
# n개의 수 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

nums = sorted(nums,reverse=True)    # 리스트 내림차순 정렬
#data = sorted(data,reverse=True)

#계산을 위한 변수 선언(->불필요한 변수가 너무 많음)
cnt = 0
cnt2 = 0
idx_num = 0
t_n = 0
# first = data[0] -> 가장 큰 수
# second = data[1] -> 2번째로 큰 수
# result = 0

while cnt < int(M):
    while cnt2 < int(K) and cnt < int(M):
        t_n += nums[idx_num]
        cnt2 += 1
        cnt += 1
    if cnt < int(M):
        idx_num = 1
        t_n += nums[idx_num]
        cnt += 1
        cnt2 = 0
        idx_num = 0
print()
print(t_n)

""" 
1)변수 선언 줄이고 단순하게 푸는 방법
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
2) 알고리즘 이용하여 푸는 방법
# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력    
"""

#2 숫자 카드 게임
cards = []
n, m = map(int, input('행,열 입력:').split())

for i in range(n):
    card = list(map(int, input().split()))
    cards.append(card)
# for i in range(n):        * 행렬 모양으로 출력
#     for j in range(m):
#         print(card2[j], end=' ')
#     print()
""" 랜덤하게 행렬값 받기
for i in range(n):
    card = []
    for j in range(m):
        ran = randint(1,10001)
        card.append(ran)
        print(f'{ran:5}',end=' ')
    cards.append(card)
    print()
"""
# f-string 정렬, 소수점 자릿수 지정
# 왼쪽 정렬(기본) > {문자:10s}    가운데 정렬(^) > {정수:^10d}
# 오른쪽 정렬 > {실수:>10.2f}   * 10자리, 소수점 아래 2자리, '>'오른쪽 정렬
n_min = []
for i in range(n):
    n_min.append(min(cards[i]))
print(max(n_min))

"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

(1) min() 함수 이용
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

(2) 2중 반복문 구조 이용
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""

# 1이 될때까지
# N에서 1빼기, N을 K로 나누기
cnt_1 = 0
n, k = map(int, input().split())
if n >= k:
    while n > 1:
        if n % k == 0:
            n = n/k
            cnt_1 += 1
        else:
            n -= 1
            cnt_1 += 1
print(cnt_1)

"""
n, k = map(int, input().split())
result = 0
while True:
    # (N = = K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
result += (n-1)
print(result)
"""