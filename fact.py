#program to find factorial of a number
print("Program to find the factorial of given number \n")
n1= int(input("enter the number : "))
factorial =1
if(n1<0):
  print("oops! the factorial of a negative number doesnot exist")

elif(n1==0):
  print("the factorial of 0 is ",1)

else:
  for i in range(1,n1+1):
    factorial= factorial*i
  print("the factorial of ", n1, " is : " ,factorial)
  
  
 
  
#python program to find the factorial of a number using recursion function
  
def recursive_func(n):
  if(n==1 or n==0):
    return 1
  else:
    return n*recursive_func(n-1)

number=int(input('enter the number of which you want to find the factorial :')) 
recursive_func(number)
