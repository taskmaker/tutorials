# Chapter 2 Problem 3 - Petrol price increases 
dieselPrice = 1.47
#remember variable names cannot begin with a digit
petrol95Price = 2.17
petrol91Price = 2.06
print("Initial price:")
print("Diesel price $" + str(dieselPrice))
print("95 price $" + str(petrol95Price))
print("91 unleaded price $" + str(petrol91Price))
dieselPrice = dieselPrice * 1.1
petrol95Price = petrol95Price * 1.1
petrol91Price = petrol91Price * 1.1
#or alternative calculations e.g. price + price * 0.1 or price + price * 10/100 etc.
print("Price increase of 10%:")
print("Diesel price $" + str(dieselPrice))
print("95 price $" + str(petrol95Price))
print("91 unleaded price $" + str(petrol91Price))