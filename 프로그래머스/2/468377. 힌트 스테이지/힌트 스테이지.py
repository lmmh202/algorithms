def solution(cost, hint):
    n = len(cost)
    best = [float('inf')]
    
    def solve(i, tickets, total):
        if i == n - 1:
            for s in range(n):
                use = tickets[s]
                if use > n - 1:
                    use = n - 1
                total += cost[s][use]
            if total < best[0]:
                best[0] = total
            return
        
        solve(i + 1, tickets, total)
        
        new_tickets = tickets[:]
        for j in range(1, len(hint[i])):
            stage = hint[i][j] - 1
            new_tickets[stage] += 1
        solve(i + 1, new_tickets, total + hint[i][0])
        
    solve(0, [0] * n, 0)
    return best[0]
        
        
            
