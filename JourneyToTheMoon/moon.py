import sys
import operator
from functools import reduce

def dfs(g, n, vis):
    if(vis[n]):
        return [vis, 0]
    found = 0
    stack = [n]
    while len(stack) > 0:
        curn = stack.pop()
        if(vis[curn] == 0):
            vis[curn] = 1
            found += 1
            for nn in g[curn]:
                if vis[nn] == 0:
                    stack.append(nn)
    return [vis, found]

def compSizes(g):
    sizes = []
    n = len(g)
    vis = [0]*n
    for i in range(n):
        if vis[i]==0:
            [vis, found] = dfs(g, i, vis)
            sizes.append(found)
    return sizes

def nways(l):
    if(len(l) == 1):
        return 0
    ways = 0
    s = l[0]
    for i in range(1, len(l)):
        ways += s*l[i]
        s += l[i]
    return ways

[n, k] = map(int, input().strip().split(" "))
g = [[] for i in range(n)]
for i in range(k):
    [a, b] = map(int, input().strip().split(" "))
    g[a].append(b)
    g[b].append(a)

#g = [[1, 4], [0], [3], [2], [0]]
print(nways(compSizes(g)))
