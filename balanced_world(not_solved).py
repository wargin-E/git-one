sen_list=[]
simple_sen_list=[]
while True:
    a=input()
    if a==".":
        break
    else:
        sen_list.append(a)
def erase(a):
    a=list(a)
    bracket_list=["(",")","{","}","[","]"]
    temp_list=[]
    for k in a:
        if k in bracket_list:
            temp_list.append(k)
    a=temp_list
    return a
def tersmall(a):
    l=len(a)
    before=len(a)
    for f in range(0,l-1):
        if a[f]=="(" and a[f+1]==")":
            a.remove(a[k+1])
            a.remove(a[k])
            break
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
def termedium(a):
    l=len(a)
    before=len(a)
    for s in range(0,l-1):
        if a[s]=="{":
            if a[s+1]=="}":
                a.remove(a[s])
                a.remove(a[s])
                break
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
def terbig(a):
    l=len(a)
    before=len(a)
    for s in range(0,l-1):
        if a[s]=="[":
            if a[s+1]=="]":
                a.remove(a[s])
                a.remove(a[s])
                break
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
for k in sen_list:
    simple_sen_list.append(erase(k))
for s in simple_sen_list:
    while "(" in s and ")" in s:
        if s[0]==")":
            break
        else:
            tersmall(s)
            if tersmall(s)==0:
                break
    while "{" in s and "}" in s:
        if s[0]=="}":
            break
        else:
            termedium(s)
            if termedium(s)==0:
                break
    while "[" in s and "]" in s:
        if s[0]=="]":
            break
        else:
            terbig(s)
            if terbig(s)==0:
                break


for k in simple_sen_list:
    print(k)





