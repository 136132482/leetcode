#去重
class StringSub(object):

     def lengthOfLongestSubstring(self, s):
                string_list=[]
                for i in range(len(s)):
                      if not s[i] in string_list:
                         string_list.append(s[i])
                ss="".join(string_list)
                print(ss)


if __name__ == '__main__':
      StringSub().lengthOfLongestSubstring("oijknmxkjjasjisajlk")