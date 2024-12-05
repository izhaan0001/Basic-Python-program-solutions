#basic factorial programs by looping
# How to find factorial of any number
num=int(input("Enter your number: ")) #Enter the number you want to find factorial of

#We are using for loop
F=1 #try putting F=0 you will find why I did put F=1
for i in range(1,num+1):
    F=F*i

print("Factorial of given number: ",F)