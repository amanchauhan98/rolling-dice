import random
# list1 = [1,2,3,4,5,6]
# list2 = [1,2,3,4,5,6]
# a = random.choice(list1)
# b = random.choice(list2)
# print(f"1st dice roller number is {a}")
# print(f"2nd dice roller number is {b}")
# print(f"the sum of two dice roller is {a+b}")
 
# dice project

def dice1(choice1) :
    list1 = [1,2,3,4,5,6]
    a = random.choice(list1)
    print(a)
    if a == 6 :
        a = random.choice(list1)
        print("again the value is",a)
    else :
        exit(0)    

    return a

def dice2(choice2) :
    list2 = [1,2,3,6,6,6]
    b = random.choice(list2)
    print(b)
    if b == 6 :
        b = random.choice(list2)
    else :
        exit(0)    
    
    return b

def dice3(choice3) :
    list3 = [1,2,2,2,5,1]
    c = random.choice(list3)
    print(c)
    if c == 6 :
        c = random.choice(list3)
    else :
        exit(0)    
    return c

i = 1
while(i<=6) :

    num = int(input("Enter the choice of your dice\n"))
    if num == 1 :
        dice1(num)
    elif num == 2:
        dice2(num)
    elif num == 3 :
        dice3(num)  
i = i + 1              

