def fivo(a):
    if a==1 or a==2:
        return 1
    else:
        return fivo(a-2)+fivo(a-1)
print(fivo(10))