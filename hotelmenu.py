#define the menu of restaurant.
menu = {
    
    'Pasta' : 45,
    'Burber': 35,
    'Coffee': 20,
    'Salad' : 30,
    'Pizza' : 60,
}
#Greet
print("Welcome To our Arizona Restaurant")
print("Pizza:$60\nPasta:$45\nBurger:$35\nCoffee:$20\nSalad:$30\n")

order_total = 0
item_1 =input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1}has been in your odered")
else:
    print(f"Your item{item_1} is not avaiable yet")

another_order = input("Do you want to add another item?(Yes/No)")
if another_order == "Yes":
    item_2 =input("Enter the name of  second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item{item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"The total amount of ordered items to pay is {order_total}")



