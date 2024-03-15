
#动态组合查询子串  从大往小  双指针
class  DynamicArray:
     #查询组合
     def  longestPalindrome(self,s):
             if len(s)==1:
                 return s
             #获取所有字符
             exiest_array=[]
             for  i in  range(len(s)):
                 if s[i] not in exiest_array:
                         exiest_array.append(s[i])
             #对字符进行动态组合
             tmp =None
             for  i in range(len(exiest_array)):
                    array_list=self.find_all_indices(s,exiest_array[i])
                    size=len(array_list)
                    for j in range(size):
                        #两个相同数之间的距离
                        num=size-j
                        #两个数之间如果距离为1，则为自己本身 根据业务逻辑视情况而定
                        if num>1:
                          res= self.get_list(num,array_list,s)
                          if res is not None:
                             if tmp is None:
                                tmp=res
                             else:
                                 if len(res)>len(tmp):
                                   tmp=res
                             break
             if tmp is None:
               return s[0]
             return tmp



     #进行从大往小范围收缩
     def     get_list(self,size,array_list,s):
         tmp=None
         for  i in range(len(array_list)):
                 if i+size>len(array_list):
                     break
                 else:
                     str= s[array_list[i]:array_list[i+size-1]+1]
                     res = self.verification_str(str)
                     if res is not None:
                         if tmp is  None:
                             tmp = res
                         else:
                           if len(res) > len(tmp):
                                tmp = res
         if tmp is not None:
            return tmp
         return None
     def find_all_indices(self, lst, value):
         return [i for i, x in enumerate(lst) if x == value]


     def   verification_str(self,str):
         new_sub_list = str[1:len(str) - 1]
         # 等于空表示两个相同数之间没有数
         if len(new_sub_list) == 1 or len(new_sub_list) == 0:
              return str
         size = len(new_sub_list) // 2
         # 中心对称
         if len(new_sub_list) % 2 == 0:
             sub_size = new_sub_list[:size]
             surplus = new_sub_list[size:]
         else:
             sub_size = new_sub_list[:size]
             surplus = new_sub_list[size + 1:]
         # 收缩范围
         for i in range(len(sub_size)):
             # 判断对应数量
             res = self.find_all_indices(sub_size, sub_size[i])
             other_res = self.find_all_indices(surplus, sub_size[i])
             if len(res) != len(other_res):
                 continue
             else:
                 # 对称回文串
                 surplus_list = []
                 for i in range(len(surplus)):
                     ss = surplus[len(surplus) - i - 1]
                     surplus_list.append(ss)
                 otehr_str = "".join(surplus_list)
                 sub_str = "".join(sub_size)
                 if sub_str == otehr_str:
                     return str
         return None



     def dynamic_portfolio_list(self, s):
         size = len(s)
         tmp=None
         for i in range(len(s)):
             if size > 0:
                 num = size - i
                 #双指针同时扩散
                 for j in range(len(s)):
                     if j + num > len(s):
                         break
                     else:
                         # #如果子指针的tmp大于动态长度
                         # if tmp is not None:
                         #    if len(tmp)>=num:
                         #        return tmp
                         #最长母指针
                         last = j + num
                         str = s[j:last]
                         # #对应的子指针
                         # if j!=0 and last !=size:
                         #     #在中间
                         #     str1=s[0:j]
                         #     str2=s[last:]
                         # elif j==0 and last!=size:
                         #        str1=s[last:]
                         # elif j!=0 and last==size:
                         #      str1=s[0:j]

                         if s[j + num - 1] != s[j]:
                             continue
                         print(str)
                         res=self.verification_str(str)
                         if res is not None:
                                return res
         return s[0]



     def     tmp_long_compare(self,str,tmp):
               if tmp is None:
                    tmp=str
               else:
                    if len(str) > len(tmp):
                        tmp=str

if __name__=='__main__':
    res=DynamicArray().dynamic_portfolio_list("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
    print(res)