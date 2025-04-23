class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        from collections import defaultdict

        def findManhattanDistance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        n, m = len(workers), len(bikes)
        hmap = defaultdict(list)
        min_dist = float("inf")
        max_dist = float("-inf")

       
        for i in range(n):
            for j in range(m):
                dist = findManhattanDistance(workers[i], bikes[j])
                hmap[dist].append([i, j])
                min_dist = min(min_dist, dist)
                max_dist = max(max_dist, dist)

        result = [-1] * n
        assigned = [False] * n
        occupied = [False] * m
        count = 0

        for dist in range(min_dist, max_dist + 1):
            if dist in hmap:
                for w, b in hmap[dist]:
                    if not assigned[w] and not occupied[b]:
                        result[w] = b
                        assigned[w] = True
                        occupied[b] = True
                        count += 1
                        if count == n:
                            return result

        return result
