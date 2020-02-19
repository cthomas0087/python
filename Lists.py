##spacing commands when printing a list:
a = [1,2,3,4,5]
print(a)

a = [1,2,3,4,5]
print(*a)

a = [1,2,3,4,5]
print(*a, sep = ", ")

a = [1,2,3,4,5]
print(*a, sep = "\n")


##printing select items from a list:
li = [1,2,3,4,5]
for i in [1,3]:
    print(li[i])

    
##printing a range:
for index in range(10):
    print(index)
    

##printing numbers between index positons from a range:
for index in range(2,11):
    print(index)
    

##printing individual letters from a word:
for letter in "hello":
    print(letter)
    

##printing all items in a list:
shopping = ["Bananas", "Apples", "Coffee", "Cereal"]
for items in shopping:
    print(items)
    

##printing index positions of all items from a list:
shopping = ["Bananas", "Apples", "Coffee", "Cereal"]
for index in range(len(shopping)):
    print(index)

 
##printing specific item from a list:
shopping = ["Bananas", "Apples", "Coffee", "Cereal"]
print(shopping[2])


##printing specific items from a list...

##will print everything starting after index positon 0 (aka "Bananas"):
shopping = ["Bananas", "Apples", "Coffee", "Cereal"]
print(shopping[1:])

##will print everyhthing between index positon 1 and 5 (inc 1, not 5):
shopping = ["Bananas", "Apples", "Steak", "Milk", "Newspapers", "Fish"]
print(shopping[1:5])


##modify list value without modifying the original list:
shopping = ["Bananas", "Apples", "Steak", "Milk", "Newspapers", "Fish"]
shopping[1]="Grapes"
print(shopping[1:5])


