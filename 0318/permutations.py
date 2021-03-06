from collections import List
results = []
prev_elements = []
def permutations(self, nums: List[int]) -> List[List[int]]:
    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])
       
        for e in elements:
            # elements[:] 얘는 왜 : 가 필요할까
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

    


