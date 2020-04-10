def tersmall(a):
    l=len(a)
    before=len(a)
    for f in range(0,l-1):
        if a[f]=="(" and a[f+1]==")":
            a.remove(a[f+1])
            a.remove(a[f])
            break
    after=len(a)
    if before==after:
        return 0
    else:
        return 1
k=['(','[','(','(','[','(','[',']',')','(',')','(','(',')',')',']',')',')',']',')']
while True:
    tersmall(k)
    if tersmall(k)==0:
        break
print(k)
#([ (([( [ ] ) ( ) (( ))] )) ]): input
#the output should be ([(([([])]))])