class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {
            v: [] for v in range(numCourses)
        }
        for vs, preq in prerequisites:
            prereq[vs].append(preq)

        output = []
        visit, cycle = set(), set()

        def dfs(vs):
            if vs in cycle:
                return False
            if vs in visit:
                return True
            cycle.add(vs)

            for pre in prereq[vs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(vs)
            visit.add(vs)
            output.append(vs)
            return True
        
        for v in range(numCourses):
            if not dfs(v):
                return []
        
        return output
