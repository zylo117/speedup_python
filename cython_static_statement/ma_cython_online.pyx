# cython和高速算法
def ma_cython_online(data, ma_length):
    # 静态声明变量
    cdef int sum_buffer, sum_tick, old_tick, new_tick

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
