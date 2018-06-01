
# coding: utf-8

# In[ ]:


n = int(input())

def cal(n):
    if n<=1:
        print(int(n),end ="")
        return
    if n%2 ==0:
        print(int(n)," ",end="")
        cal(n/2)
    elif n%2 !=0:
        print(int(n)," ",end="")
        cal(3*n+1)
cal(n)

