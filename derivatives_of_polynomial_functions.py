print("="*200)
print("This program can find the derivative function from polynomial functions")
print("="*200)
n=int(input("select the power of the highest order in the function:"))
print("="*200)
print("type in",n+1,"coefficients from high to low order.")
coeff_list=[]
for s in range(0,n):
    while s==0:
        coeff_list.append(int(input("first coefficient : ")))
        if coeff_list[0]==0:
            coeff_list.remove(0)
            print("C'mon, not zero!")
        else:
            break
    if s==0:
        coeff_list.append(int(input("second coefficient : ")))
    else:
        coeff_list.append(int(input(str(s+2)+"th coefficient : ")))
x=float(input("Give a value of x:"))
new_coeff=[]
for k in range(0,len(coeff_list)):
    new_coeff.append(coeff_list[k]*(len(coeff_list)-1-k))
new_coeff.pop()
final_coeff=[]
for k in range(0,len(new_coeff)):
    final_coeff.append(new_coeff[k]*x**(len(new_coeff)-1-k))
sum=0
for s in final_coeff:
    sum=sum+s
print("The differential coefficient at x=",x," is ",sum)