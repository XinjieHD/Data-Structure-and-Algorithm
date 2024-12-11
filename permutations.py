class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        stack = [([], nums)]

        while stack:
            path, remaining = stack.pop()
            if not remaining:
                results.append(path)
            for i in range(len(remaining)):
                stack.append((path + [remaining[i]], remaining[:i] + remaining[i+1:]))

        return results
