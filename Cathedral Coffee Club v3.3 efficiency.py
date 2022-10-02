#Variables/Dictionary Established
from pickle import FALSE
name = "patricia"
cartvalue = 0
order = "nothing"
cartlist = []
sugar = ""
incomplete = True
coffees = {
    "Long Black": 2.50,
    "Short Black": 2.00,
    "Latte": 3.50,
    "Flat White": 3.00,
    "Cappuccino": 3.00,
    "Decaf": 3.00,
    "Hot Chocolate": 4.00,
}
#Function - ordering process, input for orders, adding drinks to list/total calculations and boundary cases
def orders ():
    global cartlist
    global cartvalue
    global more
    run = False 
    while run == False:
        order = input(("What would you like to order today? ")).lower().strip()
        if order == "long black":
            cartvalue = cartvalue + 2.5
            cartlist.insert(1, "Long Black")
            run = True
        elif order == "short black":
            cartvalue = cartvalue + 2
            cartlist.insert(1, "Short Black")
            run = True
        elif order == "latte":
            cartvalue = cartvalue + 3.5
            cartlist.insert(1, "Latte")
            run = True
        elif order == "flat white":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Flat White")
            run = True
        elif order == "cappuccino":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Cappuccino")
            run = True
        elif order == "decaf":
            cartvalue = cartvalue + 3
            cartlist.insert(1, "Decaf")
            run = True
        elif order == "hot chocolate":
            cartvalue = cartvalue + 4
            cartlist.insert(1, "Hot Chocolate")
            run = True
        elif order == "hot chocy" or order == "hot choccy":
            print("Child detected")
            print("Child Discount applied")
            cartvalue = cartvalue + 3.9
            cartlist.insert(1, "Hot Choccy")
            run = True
        else:
            print("")
            print("The drink you entered was not recognised")
            print("please enter one drink at a time.")
            cartlist = cartlist
        cartlist = cartlist
        print("Current Cart Items:")
        for i in range(0, len(cartlist)):
            print(cartlist[i])
        print("Total: $", cartvalue)
        print("")
        more()
#Function-drink
def more ():
    global orders
    run = False
    global sugars
    global payment 
    while run == False:
        test = input(("Would you like to order anymore drinks? "))
        if test == "yes" or input == "Yes" or input == "YES":
            run = True
            orders()
        elif test == "NO" or test == "No" or test == "no":
            run = True
            sugars()
        else:
            print("code being mean")
#Function-Sugars
def sugars ():
    global sugar
    global payment
    run = False
    while run == False:
        sugar = input(("Would you like sugar in your drinks? "))
        if sugar == "yes" or sugar == "Yes" or sugar == "YES":
            cartlist.insert(1, "All with sugar")
            run = True
            payment()
        elif sugar == "no" or sugar == "NO" or sugar == "No":
            run = True
            payment()
        else:
            print("Your input wasn't recognised")
            print("Please enter yes or no")
            sugars()
#Function-Payment
def payment ():
    global cartlist
    global name
    run = False
    while run == False:
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
        if paymentmethod == "cash" or paymentmethod == "CASH" or paymentmethod == "Cash" or paymentmethod == "eftpos" or paymentmethod == "Eftpos" or paymentmethod == "EFTPOS" or paymentmethod == "contactless" or paymentmethod == "CONTACTLESS" or paymentmethod == "Contactless" or paymentmethod == "voucher" or paymentmethod == "VOUCHER" or paymentmethod == "Voucher" or paymentmethod == "Coupon" or paymentmethod == "COUPON" or paymentmethod == "coupon":
            run = True
            incomplete = False
            print("")
            print("Transaction Complete!")
            print("Thank you for shopping at")
            print("the Cathedral Coffee Club.")
            print("Have a nice day, ", name)
        else:
            print("")
            print("")
            print("The payment method you have selected")
            print("is either spelt incorrectly or is")
            print("unsupported currently, please try again.")
            payment()
#Introduction
print("")
print("Kia Ora, welcome to the Cathedral Coffee Club.")
print("We offer a wide range of both caffinated and")
print("hot drinks/beverages.")
print("-----------------------------------")
print("Please enter the name of the beverage you")
print("would like to purchase with correct spelling.")
print("-----------------------------------")
name = input("What was the name for your order today? ")
print("-----------------------------------")
print(f"{'Coffees:':<20}{'Prices:':<5}")
for x, prices in coffees.items():
    print(f"{x:<20}{prices:<6}")
print("-----------------------------------")
while incomplete == True:
    orders()
while incomplete == False:
    print("DONE")