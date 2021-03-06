# https://leetcode.com/problems/min-cost-to-connect-all-points/

def minCostConnectPoints(points):
    n = len(points)
    adj = {i : [] for i in range(n)} # i : list of [cost, node]
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    
    # Prim's
    res = 0
    visit = set()
    minH = [[0, 0]] # [cost, point]
    while len(visit) < n:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
    return res