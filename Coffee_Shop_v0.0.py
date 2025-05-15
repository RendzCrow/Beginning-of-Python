"""
The programme should welcome the user to the coffee shop.
It should ask the user if they want coffee, then establish how many numbers of coffees the user will be ordering. 
The number of coffees ordered should be stored in a variable: no_of_coffee.
Maths
Variables: 
Coffee_price = 30
total_price = no_of_coffee * Coffee_price
print the results.

"""

print("Welcome to My Coffee Shop: The Rendz Caffee.\n")
buy = input("Would you like to buy coffee? (y/n): ")

if buy == "y":
    no_of_coffee = int(input("\nHow many do you want to order today: "))
else: 
    print("Thank you for coming!")

coffee_price = 30
total_price = coffee_price * no_of_coffee

print(f"\nThank you for ordering with Rendz Caffee your Total price is R{total_price}.")