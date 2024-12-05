#basic factorial programs by looping
# How to find factorial of any number
num=int(input("Enter your number: ")) #Enter the number you want to find factorial of
#We are using while loop

def factorial(): #defining function
    i=1
    F=1 #try putting F=0 you will find why I did put F=1
    while(i<=num):
        F=F*i
        i+=1 #increment value of i by 1

    print("Factorial of given number: ",F)
factorial() #calling function
