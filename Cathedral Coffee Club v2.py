#Variables/Dictionary Established
cartvalue = 0
order = "nothing"
cartlist = []
sugar = ""
coffees = {
    "Long Black": 2.50,
    "Short Black": 2.00,
    "Latte": 3.50,
    "Flat White": 3.00,
    "Cappachino": 3.00,
    "Decaf": 3.00,
    "Hot Chocolate": 4.00,
}
def sugars ():
    global sugar
    sugar = input(("Would you like sugar in your drinks? "))
    if sugar == "yes" or sugar == "Yes" or sugar == "YES":
        cartlist.insert(1, "")
        cartlist.insert(1, "All with sugar")
    elif sugar == "no" or sugar == "NO" or sugar == "No":
        print("PAYMENT!")
    else:
        print("Your input wasn't recognised")
        print("Please enter yes or no")
        sugars()
def firstorder ():
    global cartlist
    global coffees
    global cartvalue
    order = input(("What would you like to order today? "))
    if order == "Long Black" or order == "long black" or order == "LONG BLACK" or order == "Long black":
        cartvalue = cartvalue + 2.5
        cartlist.insert(1, "Long Black")
    elif order == "SHORT BLACK" or order == "Short Black" or order == "Short black" or order == "short black":
        cartvalue = cartvalue + 2
        cartlist.insert(1, "Short Black")
    elif order == "Latte" or order == "LATTE" or order == "latte":
        cartvalue = cartvalue + 3.5
        cartlist.insert(1, "Latte")
    elif order == "FLAT WHITE" or order == "Flat White" or order == "flat white" or order == "Flat white":
        cartvalue = cartvalue + 3
        cartlist.insert(1, "Flat White")
    elif order == "CAPPACHINO" or order == "Cappachino" or order == "cappachino":
        cartvalue = cartvalue + 3
        cartlist.insert(1, "Cappachino")
    elif order == "DECAF" or order == "Decaf" or order == "decaf":
        cartvalue = cartvalue + 3
        cartlist.insert(1, "Decaf")
    elif order == "HOT CHOCOLATE" or order == "Hot Chocolate" or order == "hot chocolate" or order == "Hot chocolate":
        cartvalue = cartvalue + 4
        cartlist.insert(1, "Hot Chocolate")
    else:
        print("")
        print("The drink you entered was not recognised")
        print("please enter one drink at a time.")
        cartlist = cartlist
        firstorder()
    print("")
    cartlist = cartlist
    print("Current Cart Items:")
    for i in range(0, len(cartlist)):
        print(cartlist[i])
    print("Total: $", cartvalue)
    print("")
    test = input(("Would you like to order anymore dirnks? "))
    if test == "yes" or input == "Yes" or input == "YES":
        firstorder()
    elif test == "NO" or test == "No" or test == "no":
        sugars()
#Introduction
print("")
print("Kia Ora, welcome to the Cathedral Coffee Club.")
print("We offer a wide range of both caffinated and")
print("hot drinks/beverages.")
print("-----------------------------------")
print("Please enter the name of the beverage you")
print("would like to purchase with correct spelling.")
print("-----------------------------------")
print(f"{'Coffees:':<20}{'Prices:':<5}")
for x, prices in coffees.items():
    print(f"{x:<20}{prices:<6}")
print("-----------------------------------")
firstorder()


