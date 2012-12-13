import time, random #time module is required for timing sorts, random module is required for generating the unsorted lists.

smallList = [10,3,9,2,8,4,6,7,5] #a small list for students to check that the sorting alorithm is working
numbersList_Quick = [] #used to store a list of 5000 numbers between 1 and 100
lettersList_Quick = [] #used to store a list of 5000 uppercase letters A..Z
wordsList_Quick = [] #used to store a list of 10000 random words from an english dictionary

numbersList_Bubble = [] #used to store a list of 5000 numbers between 1 and 100
lettersList_Bubble = [] #used to store a list of 5000 uppercase letters A..Z
wordsList_Bubble = [] #used to store a list of 10000 random words from an english dictionary

numbersList_Insertion = [] #used to store a list of 5000 numbers between 1 and 100
lettersList_Insertion = [] #used to store a list of 5000 uppercase letters A..Z
wordsList_Insertion = [] #used to store a list of 10000 random words from an english dictionary

#this procedure will create data for numbersList
def createNumbersList():
  for i in range(5000):
		numbersList_Quick.append(random.randint(1,100))
	#create copies of this list to compare speed of bubble and insertion sorts
	global numbersList_Bubble, numbersList_Insertion
	numbersList_Bubble = numbersList_Quick[:]
	numbersList_Insertion = numbersList_Quick[:]

#this procedure will create data for lettersList
def createLettersList():
	letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for i in range(5000):
		lettersList_Quick.append(letters[random.randint(0,len(letters)-1)])
	#create copies of this list to compare speed of bubble and insertion sorts
	global lettersList_Bubble, lettersList_Insertion
	lettersList_Bubble = lettersList_Quick[:]
	lettersList_Insertion = lettersList_Quick[:]

#this procedure will create data for wordsList
def createWordsList():
	f = open('wordsEn.txt', 'r+')
	dictionaryList = []
	for line in f:
		dictionaryList.append(line[0:-1])
	random.shuffle(dictionaryList)
	for index in range(10000):
		wordsList_Quick.append(dictionaryList[index])
	#create copies of this list to compare speed of bubble and insertion sorts
	global wordsList_Bubble, wordsList_Insertion
	wordsList_Bubble = wordsList_Quick[:]
	wordsList_Insertion = wordsList_Quick[:]

def quickSort(aList):
	quickSortHelper(aList,0,len(aList)-1)

def quickSortHelper(aList,first,last):
	if first<last:
		splitPoint = partition(aList, first, last)
		
		quickSortHelper(aList,first,splitPoint-1)
		quickSortHelper(aList,splitPoint+1,last)
	
def partition(aList,first,last):
	pivotValue = aList[first]
	
	leftMark = first+1
	rightMark = last
	
	done = False
	while not done:
		while leftMark <= rightMark and aList[leftMark] <= pivotValue:
			leftMark = leftMark+1
		
		while aList[rightMark] >= pivotValue and rightMark >= leftMark:
			rightMark = rightMark-1
		
		if rightMark < leftMark:
			done = True
		else:
			temp = aList[leftMark]
			aList[leftMark] = aList[rightMark]
			aList[rightMark] = temp
	temp = aList[first]
	aList[first] = aList[rightMark]
	aList[rightMark] = temp
	
	return rightMark

def testQuickSort():
	#code to carry out a timed sort for numbersList and print out the time
	startTime = time.time() #store the start time
	quickSort(numbersList_Quick) #quick sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for quick sort on numbersList (5000 numbers 1..100) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for lettersList and print out the time
	startTime = time.time() #store the start time
	quickSort(lettersList_Quick) #quick sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for quick sort on lettersList (5000 letters) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for wordsList and print out the time
	startTime = time.time() #store the start time
	quickSort(wordsList_Quick) #quick sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for quick sort on wordsList (10,000 words) is %.2f seconds"%timeTaken)

def BubbleSort(aList):
	exchanges = True
	passnum = len(aList) - 1
	while passnum > 0 and exchanges == True:
		exchanges = False
		for index in range(0,passnum):
			if aList[index] > aList[index+1]:
				exchanges = True
				temp = aList[index]
				aList[index] = aList[index+1]
				aList[index+1] = temp
			#print(aList) #to see the resulting list after every comparison in the bubble sort
		passnum = passnum - 1
		#print(aList) #to see the resulting list after each pass of the bubble sort


def testBubbleSort():
	#code to carry out a timed sort for numbersList and print out the time
	startTime = time.time() #store the start time
	BubbleSort(numbersList_Bubble) #bubble sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for bubble sort on numbersList (5000 numbers 1..100) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for lettersList and print out the time
	startTime = time.time() #store the start time
	BubbleSort(lettersList_Bubble) #bubble sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for bubble sort on lettersList (5000 letters) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for wordsList and print out the time
	startTime = time.time() #store the start time
	BubbleSort(wordsList_Bubble) #bubble sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for bubble sort on wordsList (10,000 words) is %.2f seconds"%timeTaken)



def InsertionSort(aList):
	for index in range(0,len(aList)):
		currentValue = aList[index]
		position = index

		while position > 0 and aList[position-1] > currentValue:
			aList[position] = aList[position-1]
			position = position -1
			
		aList[position] = currentValue


def testInsertionSort():
	#code to carry out a timed sort for numbersList and print out the time
	startTime = time.time() #store the start time
	InsertionSort(numbersList_Insertion) #insertion sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for insertion sort on numbersList (5000 numbers 1..100) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for lettersList and print out the time
	startTime = time.time() #store the start time
	InsertionSort(lettersList_Insertion) #insertion sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for insertion sort on lettersList (5000 letters) is %.2f seconds"%timeTaken)

	#code to carry out a timed sort for wordsList and print out the time
	startTime = time.time() #store the start time
	InsertionSort(wordsList_Insertion) #insertion sort the numbersList
	timeTaken = time.time() - startTime #calculate the time taken using the current time and start time
	print("Time taken for insertion sort on wordsList (10,000 words) is %.2f seconds"%timeTaken)


#code to call procedures to create the unsorted lists for testing/timing
createNumbersList()
createLettersList()
createWordsList()

#code to call the procedure to test the quick sort algorithm
print("\n\nBubble Sort\n")
testBubbleSort()
print("\n\nInsertion Sort\n")
testInsertionSort()
print("\n\nQuick Sort\n")
testQuickSort()


