def kthlargest(nums,k):
    nums.sort(reverse=True)
    return nums[k-1]

print(kthlargest([2,3,4,42,32,1,4,6,7,78,11],2))