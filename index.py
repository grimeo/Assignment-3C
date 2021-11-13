# Assignment 3C
# Redo the programs on assignment2 but now with functions


money = int(input("Enter the amount of money you have: "))
apple_Price = int(input("Enter the price of an apple: "))

apples_quantity = 0
incremented_money = 0

if money < 0 or apple_Price < 0:
    print("Price or amount is out of bounds.")
else :
    while incremented_money <= money - apple_Price:
        apples_quantity += 1
        incremented_money += apple_Price
    print("You can buy " +str(apples_quantity)+ " apples and your change is "+ str(money - incremented_money)+" pesos.")