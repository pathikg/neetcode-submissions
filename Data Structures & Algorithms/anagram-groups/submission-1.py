class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution_dict = {}
        for str_s in strs:
            sorted_s = ''.join(sorted(str_s))
            if sorted_s not in solution_dict:
                solution_dict[sorted_s] = [str_s]
            else:
                solution_dict[sorted_s].append(str_s)

        return list(solution_dict.values())