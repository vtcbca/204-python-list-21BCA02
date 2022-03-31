a=int(input("enter a value = "))
sum=0
temp=a
while(a>0):
    x=a%10
    sum=sum*10+x
    a=a//10
if(temp==sum):
    print("{} is a palimdrome number".format(temp))
else:
    print("{} is a not palimdrome number".format(temp))
