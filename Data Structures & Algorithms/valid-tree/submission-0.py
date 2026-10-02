class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return True
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += p2
            return False
        parent = list(range(n))
        rank = [1] * n
        for u, v in edges:
            if union(u, v):
                return False
        parent = [find(i) for i in parent]
        return True if len(set(parent)) == 1 else False