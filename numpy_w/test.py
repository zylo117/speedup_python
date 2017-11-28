# 这个测试目标在于仿造一个类似于实盘中，不断有新的数据推送过来，
# 然后需要计算移动平均线数值，这么一个比较常见的任务。

from __future__ import division

import random
import time

from numpy_w.numpy_wrong import ma_numpy_wrong

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
    result = ma_numpy_wrong(data, ma_length)

time_per_test = (time.time() - start) / test_times
time_per_point = time_per_test / (data_length - ma_length)

print(u'单次耗时：%s秒' % time_per_test)
print(u'单个数据点耗时：%s微秒' % (time_per_point * 1000000))
print(u'最后10个移动平均值：', result[-10:])

# 单次耗时：4.106031680107117秒
# 单个数据点耗时：41.26665005132781微秒
# 最后10个移动平均值： [49.103999999999999, 49.128, 49.049999999999997, 49.154000000000003, 49.219999999999999, 49.223999999999997, 49.125999999999998, 49.134, 48.979999999999997, 48.853999999999999]
