# 시간과 메모리 측정하기

import time
start_time = time.time()  #측정 시작
# 프로그램 소스코드
end_time = time.time()  #측정 종료
print("time: ", end_time-start_time) #수행시간 출력

from random import randint

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time2 = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]
end_time2 = time.time()
print("time: ", end_time2 - start_time2)

array2 = []
for _ in range(10000):
    array2.append(randint(1,10000))
start_time3 = time.time()
array2.sort()
end_time3 = time.time()
print("time: ", end_time3 - start_time3)