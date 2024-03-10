#z字形
class Solution(object):

    def change(self,s,rows):
          if rows==1:
               return s
          size=len(s)
          #创建数组
          arrays=[]
          for  i  in  range(rows):
                  array=[]
                  arrays.append(array)
          #斜边的字符
          center=rows-2
          #总共有多少个
          num=size//(rows+center)
          #分段
          char_list=[]
          offset=0
          for i in range(num):
              list=s[offset:offset+(rows + center)]
              char_list.append(list)
              offset+=(rows + center)
          if offset < size:
              # 剩下的长度
              last=s[offset:]
              char_list.append(last)
          #对每个分段进行装配
          for  i in range(len(char_list)):
              new_char=char_list[i][:rows]
              for j in range(len(new_char)):
                   arrays[j].append(new_char[j])
              #斜着的需要大于0
              if center>0:
                  xie_list=char_list[i][rows:rows+center]
                  if len(xie_list)>0:
                      for i in range(len(xie_list)):
                           # if i==0 or i == len(arrays)-1:
                           #     continue
                           # else:
                              arrays[len(arrays)-i-2].append(xie_list[i])
                              for k in range(len(arrays)):
                                  if k != len(arrays)-2-i:
                                     arrays[k].append(" ")
          output=[]
          for  j in range(len(arrays)):
                str=" ".join(arrays[j])
                str=str+"\n"
                output.append(str)
                # for i in range(len(arrays[j])):
                #     output+=arrays[j][i]
          print("".join(output))
          return output

if __name__=='__main__':
    Solution().change("khauhadsuhaadadsaddasshddsadasdsadsadsadsakasdasjsadbjkbnjkasjkddohjqwhqwuehah",5)