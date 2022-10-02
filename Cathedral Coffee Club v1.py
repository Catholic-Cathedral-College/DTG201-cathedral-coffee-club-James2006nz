#Variables/Dictionary Established
cartvalue = 0
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
    print("")
    input("What would you like to order today? ")
#Introduction
print("")
print("Kia Ora, welcome to the Cathedral Coffee Club.")
print("We offer a wide range of both caffinated and")
print("hot drinks/beverages.")
print("-----------------------------------")
firstorder()

