import time
dict_1 = {}
for i in range(0, 100000):
    dict_1['i{}'.format(i)] = i

dict_2 = {}
for i in range(0, 10000000):
    dict_2['i{}'.format(i)] = i

time_start = time.time()
for i in range(0, 100000):
    a = dict_1['i{}'.format(i)]
time_end = time.time()
print('size 1000 avg time is: {}s'.format((time_start - time_end) / 100000))

time_start = time.time()
for i in range(0, 100000):
    a = dict_2['i{}'.format(i)]
time_end = time.time()
print('size 100000 avg time is: {}s'.format((time_start - time_end) / 10000000))

