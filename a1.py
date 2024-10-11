print("Select your option")
print("1.Bike")
print("2.Car")
user= int(input("Choose your ride : "))
if (user==1):
    print("What type of bike?")
    print("3.Motorcycle")
    print("4.Vespa")
    choice2= int(input("Choose the type : "))  
    if (choice2==3) :
        print("You have chosen Motorcycle")
    elif choice2==4:
        print("You have chosen Vespa")
    else :
        print("wrong choice!")
elif (user==2) :
    print("What type of car?")
    print("5.BMW")
    print("6.Ferrari")
    choice3= int(input("Choose the type : "))
    if(choice3==5) :
        print("You have chosen BMW")
    elif choice3==6 :
        print("You have chosen Ferrari")
    else:
        print("wrong choice!")

else :
    print("wrong choice!")