#Cafe order project

menu = {
    'Pizza': 150,
    'Buff-Momo': 120,
    'Chik-Momo': 150,
    'Burger': 100,
    "Coffie": 50,
}

print(menu)

#greed 
print("Welcome to Your Restaurant")
print (" Pizza: Rs150 \n Biff-Momo: Rs120 \n Chik-Momo: Rs150 \n Burger: Rs100\n Coffie: Rs50")

order_total = 0

item_1 = input("Enter any item name that you like to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to order")
else:
    print("Your order iteam {iteam_1} is not avaiable yet.")

another_order = input("Do you like to order item? (Yes/No) = ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Iteam {item_2} has be added in order")
    else:
        print("Order iteam {item_2} is not avaiable!")
    
print(f"The total amount of item, you have to pay is {order_total}")
