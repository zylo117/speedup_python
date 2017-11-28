# 改用numpy（首先是一种常见的错误用法）
import numpy as np


def ma_numpy_wrong(data, ma_length):
    ma = []
    data_window = data[:ma_length]
    test_data = data[ma_length:]

    for new_tick in test_data:
        data_window.pop(0)
        data_window.append(new_tick)

        # 使用numpy求均线，注意这里本质上每次循环
        # 都在创建一个新的numpy数组对象，开销很大
        data_array = np.array(data_window)
        ma.append(data_array.mean())

    return ma
