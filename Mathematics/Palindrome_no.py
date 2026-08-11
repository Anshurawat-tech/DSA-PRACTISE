class Solution:
  def ispalindrome(self,n):
    n=int(input("enter the no."))
    n1=0
    m=n
    while m>0:
      n1=n1*10 +(m%10)
      m=m//10
    if n1=n :
      return True
    else:
      False
    
