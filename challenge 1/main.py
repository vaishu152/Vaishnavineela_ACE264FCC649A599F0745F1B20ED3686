#python 3 program to find
#factorial of given number 
def factorial(n):

    # single line to fine factorial
       return 1 if (n==0 or n==1)else n*factorial(n-1)
  
#Driver code
number=int(input("enter a value"))
  
print("factorial of",number,"is",factorial(number))