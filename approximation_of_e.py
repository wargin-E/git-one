import math
def expo(n):
    approx=(1+1/n)**n
    return approx
n=2
cont=int(input("The approximation of e is "+str(expo(n))+". press 0 to finish or press 1 for more precise estimate:"))
print("="*200)
while True:
    if cont==0:
        break
    elif cont==1:
        n=n+1
        cont = int(input("The approximation of e is " + str(expo(n)) + ". press 0 to finish, press 1 for more precise estimate, 2 for a jump:"))
        print("="*200)
    elif cont==2:
        n=n+100
        cont = int(input("The approximation of e is " + str(expo(n)) + ". press 0 to finish, press 1 for more precise estimate, 2 for a jump:"))
        print("="*200)
    else:
        break