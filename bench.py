from statistics import mean
import importlib
import time

import numpy as np


r = np.random.random(1000*1000)


mergers = {
    'heapq': ('merge', 'nlargest', 'nsmallest'),
    'cyheapq': ('merge', 'nlargest', 'nsmallest'),
    'cytoolz': ('merge_sorted', 'topk', None),
}

mods = list(mergers.keys())
name_max_len = max(map(len, mods))


def test(runs, loops, f, *args):
    times = []
    for _ in range(runs):
        start = time.monotonic()
        for _ in range(loops):
            f(*args)
        stop = time.monotonic()
        times.append(stop-start)
    times.sort()
    return mean(times[1:-1])



for t in ('merge', 'nlargest', 'nsmallest'):
    print('---', t, '---')
    for mod, (merge, nlargest, nsmallest) in sorted(mergers.items()):
        module = importlib.import_module(mod)
        merge = getattr(module, merge)
        nlargest = getattr(module, nlargest)
        nsmallest = getattr(module, nsmallest) if nsmallest else None
    
        a = list(r)
        b = list(r)
        if t == 'merge':
            print(mod.rjust(name_max_len), 'merge', test(5, 100000, merge, a, a, b, b))
        elif t == 'nlargest':
            print(mod.rjust(name_max_len), 'nlargest', test(5, 5, nlargest, 10, a))
        elif t == 'nsmallest' and nsmallest:
            print(mod.rjust(name_max_len), 'nsmallest', test(5, 5, nsmallest, 10, a))
            