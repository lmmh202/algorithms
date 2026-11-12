def solution(m, n, h, w, drops):
    D = len(drops)
    INF = D + 1
    t = [INF] * (m*n)
    for i, (r, c) in enumerate(drops, 1):
        t[r * n + c] = i
    
    W = n + 1
    def first_dry(k):
        P = [0] * ((m+1) * W)
        for r in range(m):
            run,base = 0, r*n
            for c in range(n):
                run += t[base + c] <= k
                P[(r+1)*W + c+1] = P[r*W + c+1] + run
        for r in range(m - h + 1):
            for c in range(n - w + 1):
                if (P[(r+h)*W + c+w] - P[r*W + c+w]
                    - P[(r+h)*W + c] + P[r*W + c]) == 0:
                    return [r, c]
        return None
    
    lo, hi = 0, D
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if first_dry(mid): 
            lo = mid
        else:
            hi = mid - 1
    return first_dry(lo)
