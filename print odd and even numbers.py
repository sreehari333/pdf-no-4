#Python program to print even numner from 1 to n
max=int(input("Please Enter the Maximum value: "))
for num in range(1, max+1):
    if(num % 2 == 0):
        print("{0}".format(num))

#Python program to print odd numner from 1 to n
max=int(input("Please Enter the Maximum value: "))
for num in range(1, max+1):
    if(num % 2 != 0):
        print("{0}".format(num))