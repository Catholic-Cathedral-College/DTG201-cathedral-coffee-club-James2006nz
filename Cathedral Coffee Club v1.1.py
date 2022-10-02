#Variables/Dictionary Established
cartvalue = 0
order = "nothing"
coffees = {
    "Long Black": 2.50,
    "Short Black": 2.00,
    "Latte": 3.50,
    "Flat White": 3.00,
    "Cappachino": 3.00,
    "Decaf": 3.00,
    "Hot Chocolate": 4.00,
}
def firstorder ():
    global coffees
    print(f"{'Coffees:':<20}{'Prices:':<5}")
    for x, prices in coffees.items():
        print(f"{x:<20}{prices:<6}")
    print("-----------------------------------")
    order = input(str("What would you like to order today? "))
    if order == "Long Black" or "long black" or "LONG BLACK" or "Long black":
        order = 1
    elif order == "SHORT BLACK" or "Short Black" or "Short black" or "short black":
        order = 2
    elif order == "Latte" or "LATTE" or "latte":
        order = 3
    elif order == "FLAT WHITE" or "Flat White" or "flat white" or "Flat white":
        order = 4
    elif order == "CAPPACHINO" or "Cappachino" or "cappachino":
        order = 5
    elif order == "DECAF" or "Decaf" or "decaf":
        order = 6
    elif order == "HOT CHOCOLATE" or "Hot Chocolate" or "hot chocolate" or "Hot chocolate":
            order = 7
    else:
            print("Please enter the name of the beverage you")
            print("would like to purchase with correct spelling.")
            input("What would you like to order today? ")
    print(order)
#Introduction
print("")
print("Kia Ora, welcome to the Cathedral Coffee Club.")
print("We offer a wide range of both caffinated and")
print("hot drinks/beverages.")
print("-----------------------------------")
firstorder()
