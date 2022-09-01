import random
x="y"
print("This is a dice simulator")

while(x=="y"):
 x=random.randint(1,6)
 if(x==1):
    print("----------")
    print("|        |")
    print("|        |")
    print("|    *   |")
    print("|        |")
    print("|        |")
    print("----------")
 elif(x==2):
    print("----------")
    print("| *      |")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|      * |")
    print("----------")
 elif(x==3):
    print("----------")
    print("|      * |")
    print("|        |")
    print("|    *   |")
    print("|        |")
    print("| *      |")
    print("----------")
 elif(x==4):
    print("----------")
    print("|  *  *  |")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|  *  *  |")
    print("----------")
 elif(x==5):
    print("----------")
    print("|  *  *  |")
    print("|        |")
    print("|    *   |")
    print("|        |")
    print("|  *  *  |")
    print("----------")
 elif(x==6):
    print("----------")
    print("|  *  *  |")
    print("|        |")
    print("|  *  *  |")
    print("|        |")
    print("|  *  *  |")
    print("----------")
 x=input("Do you want to roll again? (y/n)")
 
