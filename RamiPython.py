Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input("Enter the number of children to be registered \n"))#int allows only integer input type

if(n<0): #Condition 1

print(" Invalid input \n");

elif(n==0): # condition 2

sum=0

print(" Total amount due is $",sum)

else:

sum=65+50*(n-1)

print(" Total amount due is $",sum)

Indentation
SyntaxError: multiple statements found while compiling a single statement
>>> 