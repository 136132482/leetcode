#两个正序数中位数
class Solution(object):

    def   findMedianSortedArrays(self, nums1, nums2):
             nums1.extend(nums2)
             nums=nums1
             for i in range(len(nums)):
                  for j in range(i+1, len(nums)):
                      if nums[i] > nums[j]:
                          nums[i],nums[j] = nums[j],nums[i]
             size=len(nums)
             if size%2==0:
                 index = size // 2
                 return (nums[index]+nums[index-1])/2
             else:
                 index = int(size//2)
                 return nums[index]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    res= Solution().findMedianSortedArrays(nums1,nums2)
    print(res)