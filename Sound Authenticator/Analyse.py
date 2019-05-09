import numpy as np


'''
def analyse(arr, start, end, seg, std):
    toj = []
    #print(arr)
    #print(end)
    for i in range(0, (end - start + 1) // (seg // 2) - 1):
        #print(i, start + i * seg, start + (i + 1) * seg)
        if start + (i + 1) * seg >= end:
            break
        xx = arr[start + i * seg: start + (i + 1) * seg]
        tmp = np.var(xx)
        toj.append(tmp)
    cnt = 0
    for i in toj:
        if i > std:
            cnt += 1
    return cnt / (end - start + 1), toj
'''


def analyse(arr, start, end, seg, std=0.15):
    cnt = 0
    for i in range(0, (end - start + 1) // (seg // 2) - 1):
        if start + (i + 1) * seg >= end:
            break
        xx = arr[start + i * seg: start + (i + 1) * seg]
        tmp = np.var(xx)
        if tmp > std:
            cnt += 1
    return cnt / (end - start + 1)
