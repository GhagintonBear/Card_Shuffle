import numpy
# Global Variables: 
filename = "RandCardDist.csv"
data = numpy.genfromtxt(filename, delimiter = ',', names = True, dtype = None)
numOfShuffles = len(data)
for i in range(numOfShuffles):
	fuse = False
	if(len(data[0]) != len(data[i])):
		print("input data inconsistent size at index:", i)
		numOfCards = -1
		fuse = True
	if(fuse == False):
		numOfCards = len(data[0])
criticalLevel = 87.968
# alpha = 0.01 sig level -> 0.07148022857352288099968307352592

 ### orderByNum(data): takes 520x52 array where each row is the outcome of a shuffle. The function will reorder the array
 ##  to an 52*520 array where each row represents a card and each element of each row represents the position it appreared
 ##	 in each shuffle. The function will return the re-ordered array.
 ###
def orderByNum(data):
	ordered = []
	for i in range(1,numOfCards + 1):	
		ordered.append([])
		for j in range(numOfShuffles):
			thisRow = list(data[j])
			ordered[i-1].append(thisRow.index(i)+1)
	return ordered
	
 ### howManyOcc(data): takes 1x520 array (a row from the re-ordered array) to count how many occurances 
 ##	 of each number between 1:52 appeared in the array. It will return a 1x52 array where each index
 ##	 represents a card and the element at each index represents the number of occurances.  
 ###
def howManyOcc(thisRow):
	groupBy = []
	for i in range(numOfCards):
		groupBy.append(thisRow.count(i+1))
	return groupBy
	
 ### makeEmpDist(thisRow): given a row from the re-ordered array, this function will calculate the 
 ##	 the empircal distribution for each row. Which, to me, is like an evidence based cumulative 
 ##	 distribution. i.e. the probability(x=2) = (numOfOcc(1)+numOfOcc(2))/(totalNumOfObservations)
 ###
def makeEmpDist(thisRow):
	groupBy = howManyOcc(thisRow)
	bigN = sum(groupBy)
	empDist = []
	empDist.append(groupBy[0])
	for i in range(1,numOfCards):
		empDist.append((empDist[i-1] + groupBy[i]))
	return numpy.divide(empDist, bigN)
	
 ### makeCumUniDist(noCards): given the number of cards in your deck, this function will return an 1x52
 ##	 array of values of the uniform cummulative probabilites between 1:52
 ###
def makeCumUniDist():
	cumUniDist = range(1,numOfCards + 1)
	return numpy.divide(cumUniDist, numOfCards)
 ### ksTest(data): The Kolmogorov-Smirnov one-sample test. Given raw data (520x52) this function will,
 ##	 for each row, calculate the test statistic d = max( abs( (empDist(x) - cumDist(x)) ) ).
 ##	 The function will return 1x52 array where each index represents a card and each element represents
 ##	 the test statistic for said card. 
 ###
def ksTest(data):
	d = []
	ordered = orderByNum(data)
	numpy.savetxt("orderedRandData.csv", ordered, delimiter = ',')
	cumUniDist = makeCumUniDist()
	for i in range(numOfCards):
		thisRow = ordered[i]
		empDist = makeEmpDist(thisRow)
		d.append(max(numpy.abs(empDist - cumUniDist)))
	return d

def check(d, criticalLevel):
	failedBucket = []
	for i in range(numOfCards):
		if (d[i] > criticalLevel):
			failedBucket.append(i+1)
	return failedBucket

def chiSqTest(data):
	ordered = orderByNum(data)
	numpy.savetxt("orderedRandData.csv", ordered, delimiter = ',')
	chiSqSums = []
	cardVar = []
	for i in range(numOfCards):
		thisRow = ordered[i]
		cardVar.append(numpy.var(thisRow))
		chiSqSums.append(chiSq(thisRow))
	return chiSqSums, cardVar

def chiSq(thisRow):
	groupBy = howManyOcc(thisRow)
	expFreq = numOfShuffles/numOfCards
	chi = []
	for i in range(numOfCards):
		chi.append( ((groupBy[i] - expFreq)**2)/expFreq )
	return sum(chi)

# d = ksTest(data)
chiSqTestData, cardVar = chiSqTest(data)
hypTest = check(chiSqTestData, criticalLevel)
print(numpy.mean(cardVar), hypTest)
for i in range(len(hypTest)):
	print("Failed Bucket:",hypTest[i], "	chi sq value:", chiSqTestData[hypTest[i]-1], "		Bucket Variance: ", cardVar[hypTest[i]-1])