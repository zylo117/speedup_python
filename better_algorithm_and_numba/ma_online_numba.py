import numba


# 高速算法和numba结合，ma_online_numba函数和ma_online完全一样
@numba.jit
def ma_online_numba(data, ma_length):
    ma = []
    data_window = data[:ma_length]
    test_data = data[ma_length:]

    sum_buffer = 0

    for new_tick in test_data:
        old_tick = data_window.pop(0)
        data_window.append(new_tick)

        if not sum_buffer:
            sum_tick = 0
            for tick in data_window:
                sum_tick += tick
            ma.append(sum_tick / ma_length)
            sum_buffer = sum_tick
        else:
            sum_buffer = sum_buffer - old_tick + new_tick
            ma.append(sum_buffer / ma_length)

    return ma
