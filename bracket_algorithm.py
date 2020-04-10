t=int(input())
b_list=[]
def ter(a):
    l=len(a)
    for s in range(0,l-1):
        if a[s]=="(":
            if a[s+1]==")":
                a.remove(a[s+1])
                a.remove(a[s])
                return 0
for s in range(0,t):
    bracket=input()
    b_list.append(bracket)
for k in b_list:
    k=list(k)
    while "(" in k and ")" in k:
        if k[0]=="(":
            ter(k)
        elif k[0]==")":
            break
        elif k[len(k)-1]=="(":
            break
    if len(k)==0:
        print("YES")
    else:
        print("NO")


