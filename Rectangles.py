n=int(input())
import math
i=int(math.sqrt(n))
sum=0
for s in range(1,i+1):
    add=n//s-s+1
    sum=sum+add
print(sum)
