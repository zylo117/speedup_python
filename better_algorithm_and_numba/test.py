# 这个测试目标在于仿造一个类似于实盘中，不断有新的数据推送过来，
# 然后需要计算移动平均线数值，这么一个比较常见的任务。

from __future__ import division

import random
import time

from better_algorithm_and_numba.ma_online_numba import ma_online_numba

# 生成测试用的数据
data = []
data_length = 100000  # 总数据量
ma_length = 500  # 移动均线的窗口
test_times = 10  # 测试次数

for i in range(data_length):
    data.append(random.randint(1, 100))

# 运行测试
start = time.time()

for i in range(test_times):
    result = ma_online_numba(data, ma_length)

time_per_test = (time.time() - start) / test_times
time_per_point = time_per_test / (data_length - ma_length)

print(u'单次耗时：%s秒' % time_per_test)
print(u'单个数据点耗时：%s微秒' % (time_per_point * 1000000))
print(u'最后10个移动平均值：', result[-10:])

# 单次耗时：0.055537080764770506秒
# 单个数据点耗时：0.5581616157263368微秒
# 最后10个移动平均值： [51.592, 51.544, 51.56, 51.688, 51.834, 51.842, 51.882, 51.87, 51.932, 52.03]
