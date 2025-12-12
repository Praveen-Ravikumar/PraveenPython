# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

def product(nums):
    n=len(nums)
    numed=[]
    num=1
    for i in range(n):
        
        for j in range(0,n):
            if(i == j):
                continue
            num*=nums[j]
        numed.append(num)
        num=1
        # print(num)
    print(numed)

nums=[1,2,3,4]
product(nums)



