def countTargetPairs():
    count = 0
    n= len(nums)
    for i in range(n) :
        for j in range(i+1) :
            if nums[i] and nums[j] < target:
                count += 1
    return count
nums = [1,2,3,4,5]
target= 6
print(countTargetPairs(nums,target))

