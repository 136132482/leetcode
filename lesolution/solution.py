
#两数之和
class  Solution(object):
      #排序
      def  twosum(self,nums:list,target:int):
             for  i  in range(len(nums)-1):
                   list=nums[i+1:]
                   for  j in range(len(list)):
                          if nums[i]+list[j] == target:
                              print(nums[i],list[j])
                              num=nums.index(list[j])
                              if i ==num:
                                  indexes = self.find_all_indices(nums, list[j])
                                  return i,indexes[1]
                              else:
                                  return i,num
                          else:
                               print(str(nums[i])+"未匹配到"+str(list[j]))
                   # if nums[i]<len(nums):
                   #   nums.remove(nums[i])

      def find_all_indices(self,lst, value):
          return [i for i, x in enumerate(lst) if x == value]


if __name__ == '__main__':
      nums = [2,7,11,15]
      target=9
      res=Solution().twosum(nums,target)
      print(res)