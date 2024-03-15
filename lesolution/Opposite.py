
#最长汇文子串  范围收缩  中心动态扩展  空间转换  倒转对称
class Solution(object):

    #中心扩散比对
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        Substring=[]
        child_char = self.find_all_indices(s, s[0])
        if len(child_char) ==len(s):
            return s
        # for i in range(len(s)):
        #     if not s[i] in char_list:
        #         char_list.append(s[i])
        #     else:
        #         # 中心扩散
        #         child_char = self.find_all_indices(char_list, s[i])
        #         char_list.append(s[i])
        # 收缩范围
        exisit_list=[]
        for j in range(len(s)):
            if not s[j] in exisit_list:
               child_char = self.find_all_indices(s, s[j])
               if len(child_char)>=len(s)//2 and len(child_char)>100:
                for i in range(len(s)):
                   if child_char[i]!=i:
                       if child_char[i]>=len(s)//2:
                          return s[:i]
                       else:
                          break
               self.iteration_char(s, j,Substring)
               exisit_list.append(s[j])
               if len(Substring)>0:
                 if len(Substring) == len(s):
                   return Substring[0]
        if len(Substring)==0:
               return s[0]
        # for i in range(len(Substring) - 1):
        #     for j in range(i + 1, len(Substring)):
        #         if len(Substring[i]) < len(Substring[j]):
        #             Substring[i], Substring[j] = Substring[j], Substring[i]
        print(Substring)
        return Substring[0]

    # 收缩范围 递归   第二种方法： 翻转变换 直接对称比对
    def iteration_char(self, char_list, index, Substring):
        # 确认相同下标位置
        total_all = self.find_all_indices(char_list, char_list[index])
        # if len(total_all) == len(char_list):
        #      Substring.append(char_list)
        # index_list=[]
        for  k in range(len(total_all)-1):
          for  j in range(1,len(total_all)-k):
            # print(f"当前开始下标：{str(i)}遍历：" + str(total_all[i]))
            # print(f"当前结束下标:" + str(total_all[j]))
            # if total_all[j]+1 == len(char_list):
            #      sub=char_list[total_all[k]:]
            # else:
            end_size=total_all[len(total_all) - j]+1
            sub=char_list[total_all[k]:end_size]
            if len(Substring) > 0:
                if len(Substring[0]) == len(char_list):
                    return
                if len(Substring[0]) >= len(char_list[k:]):
                    return
                if len(Substring[0])>=len(sub):
                    break
            conversion_list = sub
            # if len(sub)==2:
            #     self.list_append(Substring, conversion_list, index_list)
            #     return
            #如果子串的都为一样的时候直接跳过
            child_char = self.find_all_indices(conversion_list, conversion_list[0])
            if len(child_char) == len(conversion_list):
                self.list_append(Substring, conversion_list)
                continue
            #最大距离数如果存在，则后续不需要遍历了
            # if len(index_list)>0:
            #     return
            new_sub_list = sub[1:len(conversion_list)-1]
            #等于空表示两个相同数之间没有数
            if len(new_sub_list) == 1 or len(new_sub_list)==0 :
                self.list_append(Substring, conversion_list)
                continue
            size = len(new_sub_list) // 2
            # 中心对称
            if len(new_sub_list) % 2 == 0:
                sub_size = new_sub_list[:size]
                surplus = new_sub_list[size:]
            else:
                sub_size = new_sub_list[:size]
                surplus = new_sub_list[size+1:]
            # 收缩范围
            flag=True
            for i in range(len(sub_size)):
                #判断对应数量
                res=self.find_all_indices(sub_size,sub_size[i])
                other_res=self.find_all_indices(surplus,sub_size[i])
                if len(res)!=len(other_res):
                      flag =False
                      break
                else:
                    # 对称回文串
                    surplus_list=[]
                    for i in range(len(surplus)):
                            ss=surplus[len(surplus)-i-1]
                            surplus_list.append(ss)
                    otehr_str="".join(surplus_list)
                    str="".join(sub_size)
                    if str == otehr_str:
                        self.list_append(Substring, conversion_list)
                        flag = False
                        break

                    # 对称相同字符对应下标
                    # if sub_size[i] != new_sub_list[len(new_sub_list) - 1 - i]:
                    #     flag = False
                    #     break


    def   list_append(self,Substring,conversion_list):
        # 回文串
        if len(Substring) == 0:
            Substring.append(conversion_list)
        else:
            if len(conversion_list) > len(Substring[0]):
                Substring.remove(Substring[0])
                Substring.append(conversion_list)

    def find_all_indices(self, lst, value):
         return [i for i, x in enumerate(lst) if x == value]

     #直接全部比对
    def longestPalindrometwo(self,s):
         size=len(s)
         tmp=None
         reslut=[]
         r_tmp=None
         strngs=[] #正向子串的所有集合
         reverse=[] #反向子串的所有集合
         for i in range(len(s)-1):
           tmp=None
           for j in range(i+1,len(s)):
              if tmp==None:
                 str=s[i]+s[j]
                 tmp=str
                 r_s = []
                 # 倒转进行获取
                 for i in range(len(tmp)):
                     r_s.append(tmp[len(tmp) - i - 1])
                 r_ss = "".join(r_s)
                 if tmp==r_ss:
                    reslut.append(tmp)
                 # r_str=s[size-i-1]+s[size-j-1]
                 # r_tmp=r_str
                 # reverse.append(r_str)
              else:
                 tmp=tmp+s[j]
                 r_s = []
                 # 倒转进行获取
                 for i in range(len(tmp)):
                     r_s.append(tmp[len(tmp) - i - 1])
                 r_ss = "".join(r_s)
                 if tmp == r_ss:
                     reslut.append(tmp)
                 # r_str=r_tmp+s[size-j-1]
                 # r_tmp=r_str
                 # reverse.append(r_str)
         # res=[]
         # #将正向子串和反向子串做对比 找出相同的
         # for s in strngs:
         #    if any( s==r for r in res):
         #          if len(s)==2:
         #              if s[0]==s[1]:
         #                   reslut.append(s)
         #          else:
         #             reslut.append(s)
         if len(reslut)==0:
              return  s[0]
         if len(reslut)==1:
              return reslut[0]
         for i in range(len(reslut)-1):
             for j in range(i+1,len(reslut)):
               if len(reslut[i])<len(reslut[j]):
                   reslut[i],reslut[j]=reslut[j],reslut[i]
         return reslut[0]


if  __name__=='__main__':
      s=Solution()
      res= s.longestPalindrome("qkajbumzdzkiplmbcpnhbzweoevrvbptpozhtrfntszvnwbdahvkykmezrwruhvvslngruvwqebudtfxgpbmwefczwrecpqjegxkqknpobzkemmtruidulnxgntjxcmxtwmlxhzmbqfqylwvzjyojhfawwuupiipvxjiyxkqvsxbhgzzegfkdihizvjoxzrmeorikzsdyphbujaqmykrfblneqmwwxsoonzsgvligqxrrumspylfvquklbanjhkudlprwoycpxdsueokruoofyubirbhbyfuvgllijywuqmkcsfjttbnmelrylivkefllepgxnoeummujbaoyvryukyoumvuxezegpwgmwsupjuaarvbtbfmisrifjadqjypmzipvjysgakvjhfeaqwpsqijvqibshctuabwqqsjwotjopahoaptmxkwerkjkmwiodgblhtnhykzjuaoluoyokroxuvqtkpggfanzabgjejdfsgybhxbscubdpufywbxgutheskuhixasnksoayjngvhfoxxclykfobrwxjwgefarzczvptlfrgrtrjcemaeihpukhbeoezgvrwxgyhpkkfvmfvquwtswkdwqqgrgasopladdnteulqofmjhewpghkibbrewnhdllfppctgkfkoedoiwqocnpvfviochrokrgrzthrvyhqfsrzyyvqwkhuzsrkfaympcdodkwaojnghzytkhf")
      print(res)