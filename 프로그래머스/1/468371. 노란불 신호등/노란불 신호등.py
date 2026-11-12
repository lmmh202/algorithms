from math import lcm

def solution(signals):
    limit = 1
    for g, y, r in signals:
        limit = lcm(limit, g+y+r)
    
    for i in range(1, limit + 1):
        if all(g <= (i-1) % (g+y+r) < g + y for g, y, r in signals):
            return i
    return -1
