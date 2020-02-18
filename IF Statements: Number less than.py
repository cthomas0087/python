## write a program that prints out all the elements of the list that are less than 5:
n = [7, 5, 10, 2, 4, 6, 12, 17, 1, 1, 8, 3]
for i in n:
    if i<5:
        print(i)

##adjust the program to take user input to create the list:
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))
list = (n1, n2, n3, n4)

output = list
for i in list:
    if i <= 5:
        print(i)
        
