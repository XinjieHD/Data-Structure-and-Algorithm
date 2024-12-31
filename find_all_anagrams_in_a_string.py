class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        s_count = Counter()
        
        p_len = len(p)
        
        for i in range(len(s)):
           
            s_count[s[i]] += 1

            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1
            
            if s_count == p_count:
                result.append(i - p_len + 1)
                
        return result
