# 使用numba加速，ma_numba函数和ma_basic完全一样
import numba

@numba.jit
def ma_numba(data, ma_length):
    ma = []
    data_window = data[:ma_length]
    test_data = data[ma_length:]

    for new_tick in test_data:
        data_window.pop(0)
        data_window.append(new_tick)
        sum_tick = 0
        for tick in data_window:
            sum_tick += tick
        ma.append(sum_tick/ma_length)

    return ma
