import numpy as np


'''
对这段区间的数字按照seg分段，每段里求方差，若方差大于标准值，计数
返回 计数与所有段数的比值
'''

def analyse(arr, start, end, seg, std=0.15):
    cnt = 0
    for i in range(0, (end - start + 1) // (seg // 2) - 1):
        if start + (i + 1) * seg >= end:
            break
        xx = arr[start + i * seg: start + (i + 1) * seg]
        tmp = np.var(xx)    #计算方差
        if tmp > std:
            cnt += 1
    return cnt / (end - start + 1)
