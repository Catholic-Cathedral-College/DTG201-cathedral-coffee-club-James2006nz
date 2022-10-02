#Variables/Dictionary Established
from pickle import FALSE


cartvalue = 0
order = "nothing"
cartlist = []
sugar = ""
incomplete = True
order1 = False
coffees = {
    "Long Black": 2.50,
    "Short Black": 2.00,
    "Latte": 3.50,
    "Flat White": 3.00,
    "Cappachino": 3.00,
    "Decaf": 3.00,
    "Hot Chocolate": 4.00,
}
#Function-Firstorder
def firstorder ():
    global cartlist
    global coffees
    global cartvalue
    global more
    global order1
    while order1 == False:
        order = input(("What would you like to order today? "))
        if order == "Long Black" or order == "long black" or order == "LONG BLACK" or order == "Long black":
            cartvalue = cartvalue + 2.5
            cartlist.insert(1, "Long Black")
            order1 = True
        elif order == "SHORT BLACK" or order == "Short Black" or order == "Short black" or order == "short black":
            cartvalue = cartvalue + 2
            cartlist.insert(1, "Short Black")
            order1 = True
        elif order == "Latte" or order == "LATTE" or order == "latte":
            cartvalue = cartvalue + 3.5
            cartlist.insert(1, "Latte")
            order1 = True
        elif order == "FLAT WHITE" or order == "Flat White" or order == "flat white" or order == "Flat white":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Flat White")
            order1 = True
        elif order == "CAPPACHINO" or order == "Cappachino" or order == "cappachino":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Cappachino")
            order1 = True
        elif order == "DECAF" or order == "Decaf" or order == "decaf":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Decaf")
            order1 = True
        elif order == "HOT CHOCOLATE" or order == "Hot Chocolate" or order == "hot chocolate" or order == "Hot chocolate":
            cartvalue = cartvalue + 4
            cartlist.insert(1, "Hot Chocolate")
            order1 = True
        else:
            print("")
            print("The drink you entered was not recognised")
            print("please enter one drink at a time.")
            cartlist = cartlist
            firstorder()
        cartlist = cartlist
        print("Current Cart Items:")
        for i in range(0, len(cartlist)):
            print(cartlist[i])
        print("Total: $", cartvalue)
        print("")
        more()
#Function-drink
def more ():
    global firstorder
    global sugars
    global payment 
    test = input(("Would you like to order anymore drinks? "))
    if test == "yes" or input == "Yes" or input == "YES":
        firstorder()
    elif test == "NO" or test == "No" or test == "no":
        sugars()
    else:
        more()
#Function-Sugars
def sugars ():
    global sugar
    global payment
    sugar = input(("Would you like sugar in your drinks? "))
    if sugar == "yes" or sugar == "Yes" or sugar == "YES":
        cartlist.insert(1, "All with sugar")
        payment()
    elif sugar == "no" or sugar == "NO" or sugar == "No":
        payment()
    else:
        print("Your input wasn't recognised")
        print("Please enter yes or no")
        sugars()
#Function-Payment
def payment ():
    global cartlist
    print("")
    print("Checkout:")
    print("--------------------")
    print("Current Cart Items:")
    for i in range(0, len(cartlist)):
        print(cartlist[i])
    print("Total: $", cartvalue)
    print("SUPPORTED PAYMENT METHODS:")
    print("'cash', 'eftpos', 'contactless', 'voucher' (or coupon)")
    paymentmethod = input(("How do you wish to complete this transaction? "))
    if paymentmethod == "cash" or paymentmethod == "CASH" or paymentmethod == "Cash" or paymentmethod == "eftpos" or paymentmethod == "Eftpos" or paymentmethod == "EFTPOS" or paymentmethod == "contactless" or paymentmethod == "CONTACTLESS" or paymentmethod == "Contactless" or paymentmethod == "voucher" or paymentmethod == "VOUCHER" or paymentmethod == "Voucher":
        print(".")
        print(".")
        print(".")
        print(".")
    else:
        print("")
        print("")
        print("The payment method you have selected")
        print("is either spelt incorrectly or is")
        print("unsupported currently, please try again.")
        payment()
    incomplete = False
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
while incomplete == True:
    firstorder()
while incomplete == False:
    print("DONE")