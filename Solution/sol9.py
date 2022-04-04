#write a script to enter any number and print it sum og digit
a=int(input("Enter Number :"))
sum=0
while(a!=0):
  sum=sum+a%10
  a=a//10
print("SUM OF It:",sum)  
  
