menu = {
    'Veg. Pizza':180,
    'Non-Veg. Pizza':240,
    'Veg. Rice':120,
    'Non-Veg. Rice':170,
    'Samosha':40,
    'Veg. Burger':60,
    'Non-Veg. Burger':100,
    'Tea':50,
    'Coffee':100,
    'Pasta':90,
    'Half-Noodls':70,
    'full-noodls':130,
}
#Greet

print("\n Welcome to SR Restaurant \n ")
print("Veg.Pizzz: 180 Rs\nNon-Veg. Pizza: 240 Rs\nVeg. Rice: 120 Rs\nNon-Veg. Rice: 170 Rs\nSamosha: 40 Rs\nVeg. Burger: 60 Rs\nNon-Veg. Burger: 100 Rs\nTea: 50 Rs\nCoffee: 100 Rs\nPasta: 90 Rs\nHalf-Noodls: 70 Rs\nfull-noodls: 130 Rs\n")
order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order ")
else:
    print("Order item {item_1} is not available yet! ")
another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order ")
    else:
        print(f"ordered item {item_2} is not available ")
print(f"the total amount of items to pay is {order_total} ")