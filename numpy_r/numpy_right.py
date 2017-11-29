# 改用numpy（首先是一种常见的错误用法）
import numpy as np


def ma_numpy_right(data, ma_length):
    ma = []

    # 用numpy数组来缓存计算窗口内的数据
    data_window = np.array(data[:ma_length])

    test_data = data[ma_length:]

    for new_tick in test_data:
        # 使用numpy数组的底层数据偏移来实现数据更新
        data_window[0:ma_length - 1] = data_window[1:ma_length]
        data_window[-1] = new_tick
        ma.append(data_window.mean())

    return ma
