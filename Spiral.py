n = [[1,2,3],[4,5,6],[7,8,9]]

def spiral(n):
    i = 0
    j = 0
    l = len(n)
    while j<l:
        print(n[i][j],end =" ")
        j = j+1
    i = i+1
    while i<l-1:
        print(n[i][j],end =" ")
        i = i +1
    j = j-1
    while j>=0:
        print(n[i][j],end =" ")
        j =j -1
    i = i-1
    while i>0:
        print(n[i][j],end = " ")
        i = i-1
    
print(spiral(n))    