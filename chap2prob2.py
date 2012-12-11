# Problem 2 - Booksellers giftcard
balance = 50.00
bookPurchase1 = 35.00
print("Initial Card Balance $" + str(balance))
# note we are updating the balance, not creating a new variable
# the initial balance needs to be displayed before the update alters it
balance = balance - bookPurchase1
print("Book Purchase $" + str(bookPurchase1))
print("New Card Balance $" + str(balance))