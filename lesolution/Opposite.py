
#最长汇文子串
class Solution(object):

    def longestPalindrome(self,s):
         size=len(s)
         tmp=None
         r_tmp=None
         strngs=[]
         reverse=[]
         for i in range(len(s)):
           for j in range(i+1,len(s)):
             if tmp==None or r_tmp==None:
                 str=s[i]+s[j]
                 tmp=str
                 strngs.append(str)
                 r_str=s[size-i-1]+s[size-j-1]
                 r_tmp=r_str
                 reverse.append(r_str)
             else:
                 str=tmp+s[j]
                 strngs.append(str)
                 r_str=r_tmp+s[size-j-1]
                 tmp=str
                 r_tmp=r_str
                 reverse.append(r_str)
           tmp=None
         res=[]
         for s in strngs:
               r_s=[]
               for i in  range(len(s)):
                    r_s.append(s[len(s)-i-1])
               r_ss="".join(r_s)
               res.append(r_ss)
         reslut=[]
         for s in strngs:
            if any( s==r for r in res):
                  if len(s)==2:
                      if s[0]==s[1]:
                           reslut.append(s)
                  else:
                     reslut.append(s)
         return reslut

if  __name__=='__main__':
      s=Solution()
      res= s.longestPalindrome("ashdashdashdashhjwuiqwhbkbqwuyqwhasdihqwekb")
      print(res)