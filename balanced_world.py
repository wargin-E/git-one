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
    for k in range(0,l-1):
        if a[k]=="(" and a[k+1]==")":
            a[k+1]=0
            a[k]=0
            break
    while 0 in a:
        a.remove(0)
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
def termedium(a):
    l=len(a)
    before=len(a)
    for k in range(0,l-1):
        if a[k]=="{" and a[k+1]=="}":
            a[k+1]=0
            a[k]=0
            break
    while 0 in a:
        a.remove(0)
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
def terbig(a):
    l=len(a)
    before=len(a)
    for k in range(0,l-1):
        if a[k]=="[" and a[k+1]=="]":
            a[k+1]=0
            a[k]=0
            break
    while 0 in a:
        a.remove(0)
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
def remove_brackets(s):
    before=len(s)
    while "(" in s and ")" in s:
        if s[0] == ")":
            break
        else:
            tersmall(s)
            if tersmall(s) == 0:
                break
    while "{" in s and "}" in s:
        if s[0] == "}":
            break
        else:
            termedium(s)
            if termedium(s) == 0:
                break
    while "[" in s and "]" in s:
        if s[0] == "]":
            break
        else:
            terbig(s)
            if terbig(s) == 0:
                break
    after=len(s)
    if before==after:
        return 0
for k in sen_list:
    simple_sen_list.append(erase(k))
for s in simple_sen_list:
    while remove_brackets(s)!=0:
        remove_brackets(s)

for k in simple_sen_list:
    if len(k)==0:
        print("yes")
    else:
        print("no")





