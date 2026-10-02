class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        parent = [i for i in range(n)]
        rank = [1] * n 
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x1, x2):
            p1, p2 = find(x1), find(x2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
        
        for node in range(n):
            for neigh in graph[node]:
                union(node, neigh)

        parent = [find(i) for i in parent]
        return len(set(parent))
