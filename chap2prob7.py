# Chapter 2 Problem 7 - iTunes balance
initialBalance = 100.0
SHORT_TRACK = 1.79
MEDIUM_TRACK = 2.5
LONG_TRACK = 4.5
numShort = 3
numMedium = 4
numLong = 2
endBalance = initialBalance - (SHORT_TRACK * numShort + 
   MEDIUM_TRACK * numMedium + LONG_TRACK * numLong)
print("Initial balance $"+ str(initialBalance))
print("Purchased",numShort," short tracks at ", SHORT_TRACK)
print("Purchased",numMedium," medium tracks at ", MEDIUM_TRACK)
print("Purchased",numLong," long tracks at ", LONG_TRACK)
print("Final balance $" + str(endBalance))