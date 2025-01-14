class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        dp = [0] * (len(jobs) + 1)  
        
        sorted_end_times = [job[1] for job in jobs]
        
        for i in range(1, len(jobs) + 1):

            current_profit = jobs[i - 1][2]
            
            last_non_overlap_index = bisect_right(sorted_end_times, jobs[i - 1][0]) - 1
            
            include_profit = current_profit + (dp[last_non_overlap_index + 1] if last_non_overlap_index >= 0 else 0)

            exclude_profit = dp[i - 1]

            dp[i] = max(include_profit, exclude_profit)
        

        return dp[-1]
