# 这个测试目标在于仿造一个类似于实盘中，不断有新的数据推送过来，
# 然后需要计算移动平均线数值，这么一个比较常见的任务。

from __future__ import division

import random
import time

import pyximport
pyximport.install()
import ma_cython

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
    result = ma_cython.ma_cython(data, ma_length)

time_per_test = (time.time() - start) / test_times
time_per_point = time_per_test / (data_length - ma_length)

print(u'单次耗时：%s秒' % time_per_test)
print(u'单个数据点耗时：%s微秒' % (time_per_point * 1000000))
print(u'最后10个移动平均值：', result[-10:])

# 单次耗时：1.4290493249893188秒
# 单个数据点耗时：14.362304773761998微秒
# 最后10个移动平均值： [51.048, 51.066, 51.116, 51.158, 50.992, 51.068, 51.032, 50.926, 50.984, 50.84]
