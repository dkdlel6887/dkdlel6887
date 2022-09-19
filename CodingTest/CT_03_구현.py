import time

# 예제 4-1 상하좌우 / 시뮬레이션 유형
n = int(input())
mv_lst = input().split()
x,y = 1,1
start_time = time.time()
for i in range(len(mv_lst)):
    if mv_lst[i] == 'L' and y > 1:
        y-=1
    elif mv_lst[i] == 'R' and y < n:
        y+=1
    elif mv_lst[i] == 'U' and x > 1:
        x-=1
    elif mv_lst[i] == 'D' and x < n:
        x+=1
    else: continue
print(x,y)

end_time = time.time()
print("time: ", end_time-start_time)
"""
# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mv_types = ['L', 'R', 'U', 'D']

for mv in mv_lst:
    for i in range(len(mv_types)):
        if mv == mv_types[i]:
            nx = x+dx[i]
            ny = x+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
"""

# 시각
n = int(input())
cnt_time = 0
for hour in range(0,n+1):
    for minute in range(0,60):
        for second in range(0,60):
            if (str(hour)+str(minute)+str(second)).count('3')>0:
                cnt_time += 1
print(cnt_time)

# 해설
"""
# 시각 / 완전탐색유형
n = int(input())
cnt_time = 0
for hour in range(0, n+1):
    for min in range(0, 60):
        for sec in range(0, 60):
            if '3' in str(hour) + str(min) + str(sec):
                cnt_time += 1
print(cnt_time)
"""

# 왕실의 나이트
mv = input()
row = int(ord(mv[0])) - int(ord('a')) + 1  # 문자값을 아스키코드로 변경
# ord() 문자 -> 아스키코드,  chr() 아스키코드 -> 문자
col = int(mv[1])

# 0,0 에서 이동할 수 있는 좌표 목록
rc_types = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
# result 2,3,4,6,8


cnt = 0
for i in rc_types:
    nr = row + i[0]
    nc = col + i[1]
    if nr>0 and nc>0 and nr<9 and nc<9:
        cnt += 1
print(cnt)


# 게임 개발 -> 해결 실패
"""
n, m = map(int, input().split())
a, b, d = map(int, input().split())
land = []

for i in range(n):
    data = list(map(int, input().split())) # 육지:0, 바다:1 입력
    land.append(data)
land[a][b] = -1    # 시작 위치

d_type = {0:'북', 1:'동', 2:'남', 3:'서'}  # 북,서,남,동
# 북으로 이동 -1,0 / 동으로 이동 0,1 / 남으로 이동 1,0 / 서로 이동 0,-1
mv_type = [(-1,0),(0,1),(1,0),(0,-1)]
mv_cnt = 0
turn_time = 0
while True:
    if d > 0:               # 반시계방향으로 방향 전환
        d -= 1
    else:
        d = 3
    na = a+mv_type[d][0]    # 보고있는 방향 1칸 앞 좌표
    nb = b+mv_type[d][1]
    print(na, nb, d)
    if land[na][nb] != 0:   # 육지가 아닌 경우 or 갔던 곳인 경우
        turn_time += 1
        if turn_time == 4:
            na = a - mv_type[d][0]  # 뒤로 한칸 이동 시 좌표
            nb = b - mv_type[d][1]
            print(na, nb, d)
            print('hi')
            if land[na][nb] == -1:
                a = na
                b = nb
            else:                   # 뒤가 바다면 종료
                print('hi2')
                break
        continue
    else:                   # 육지인 경우
        land[na][nb] = -1
        a = na
        b = nb
        print('hi3')
        mv_cnt += 1
        turn_time = 0
print(mv_cnt)

입력값:                결과값: 3
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""