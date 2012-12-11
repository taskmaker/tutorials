#Chapter 2 Problem 6 - price of meal
MAIN_PRICE = 12.5
DESSERT_PRICE = 6
DRINK_PRICE = 3.55
numMains = 2
numDesserts = 2
numDrinks = 5
mainTotal = numMains * MAIN_PRICE
dessertTotal = numDesserts * DESSERT_PRICE
drinkTotal = numDrinks * DRINK_PRICE
totalPrice = mainTotal + dessertTotal + drinkTotal
print(numMains,"mains at", MAIN_PRICE,"is", mainTotal)
print(numDesserts,"mains at", DESSERT_PRICE,"is", dessertTotal)
print(numDrinks,"drinks at", DRINK_PRICE,"is", drinkTotal)
print("Price of meal: $" + str(totalPrice))