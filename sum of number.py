 i = 0
        
        j = len(nums) -1
        while i<j:
            sm = nums[i]+nums[j]
            if target == sm:
                print(i,j)
                return True
            elif sm<target:
                i+=1
            else:
                j -=1
        return False
