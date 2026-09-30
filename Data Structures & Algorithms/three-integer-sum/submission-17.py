class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []

            for i in range(len(nums)):

                l,r = i+1,len(nums)-1

                while l<r:
                    total = nums[l] + nums[r] + nums[i]
                    if total == 0:
                        if [nums[i],nums[l],nums[r]] in res:
                            l+=1
                            r-=1
                        else:
                            res.append([nums[i],nums[l],nums[r]])
                            l+=1
                            r-=1

                    elif total > 0:
                        r-=1
                    else:
                        l+=1
                    
            return res
            
        
        # nums.sort()
        # res = []

        # for i in range(len(nums)):

        #     l,r = i,len(nums)-1

        #     while l<r:
        #         total = nums[l] + nums[r] + nums[i]
        #         if total == 0:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l] == nums[l-1] and l<r:
        #                 l+=1
        #         elif total < 0:
        #             r-=1
        #         else:
        #             l+=1
                
        # return res