from random import *
n=int(input("select the number of points:"))
in_circle=0
total=0
for s in range(0,n):
    x=random()
    y=random()
    if (x*x+y*y<1):
        in_circle=in_circle+1
print("points in the circle:",in_circle)
print("total number of points:",n)
print("approximation of pi:",in_circle*4/n)