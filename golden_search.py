import numpy as np


def golden_search(func, min_val, max_val, epsilon=1e-10) :
    golden_ratio = (np.sqrt(5) - 1) / 2
    max_min = max_val - min_val
    x1 = max_val - (golden_ratio * max_min)
    x2 = min_val + (golden_ratio * max_min)
    fmin = func(min_val)
    fmax = func(max_val)
    fx1 = func(x1)
    fx2 = func(x2)
    iteration = round(np.log(epsilon / max_min) / np.log(golden_ratio))
    k = 0

    while k < iteration :
        k = k + 1
        if fx1 >= fx2 :
            max_val = x2
            fmax = fx2
            x2 = x1
            fx2 = fx1
            max_min = max_val - min_val
            x1 = max_val - golden_ratio * max_min
            fx1 = func(x1)

        else :
            min_val = x1
            fmin = fx1
            x1 = x2
            fx1 = fx2
            max_min = max_val - min_val
            x2 = min_val + golden_ratio * max_min
            fx2 = func(x2)

    if fmax < fmin :
        p = max_val
        yp = fmax
    else :
        p = min_val
        yp = fmin
    return yp, p, iteration