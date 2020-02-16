## write a program that prints out all the elements of the list that are less than 5.

a = [7, 5, 10, 2, 4, 6, 12, 17, 1, 1, 8, 3]
b = int(5)

for i in a:
    if i<b:
        print(i)


##modify the application to ask a user for a number and print numbers less that the given number

a = [7, 5, 10, 2, 4, 6, 12, 17, 1, 1, 8, 3]
b = int(input("enter a number: "))

for i in a:
    if i<b:
        print(i)
