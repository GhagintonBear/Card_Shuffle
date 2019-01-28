# testing 'the randomness' of the cards placed in rank1 out of 52
# def ksTest():
	# d = []
	# for i in range(52):
		# thisCol = numpy.divide(sorted(getThisCol(data, i )), 100)
		# dMinus = calculateDminus(thisCol)
		# dPlus = calculateDplus(thisCol)
		# d.append(max(max(dMinus), max(dPlus)))
	# return d
	
# def getThisCol(data,index):
	# thisCol = []
	# rowSize = len(data)
	# for i in range(rowSize):
		# thisCol.append(data[i][index])
	# return thisCol

# def calculateDplus(thisCol):
	# n = len(thisCol)
	# dPlus = []
	# for i in range(n):
		# dPlus.append((i/n) - thisCol[i])
	# return dPlus
	
# def calculateDminus(thisCol):
	# n = len(thisCol)
	# dMinus = []
	# for i in range(n):
		# dMinus.append(thisCol[i] - ((i-1)/n))
	# return dMinus

 ### orderByNum(data): takes 520x52 array where each row is the outcome of a shuffle. The function will reorder the array
 ##  to an 52*520 array where each row represents a card and each element of each row represents the position it appreared
 ##	 in each shuffle. The function will return the re-ordered array.
 ###
def orderByNum(data):
	ordered = []
	for i in range(1,53):	
		ordered.append([])
		for j in range(0,520):
			thisRow = list(data[j])
			ordered[i-1].append(thisRow.index(i)+1)
	return ordered
	
 ### howManyOcc(data): takes 1x520 array (a row from the re-ordered array) to count how many occurances 
 ##	 of each number between 1:52 appeared in the array. It will return a 1x52 array where each index
 ##	 represents a card and the element at each index represents the number of occurances. The purpose
 ##	 of this function is to simplify the calculations required to make the Empircal Distribution. 
 ###
def howManyOcc(thisRow):
	groupBy = []
	for i in range(52):
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
	for i in range(1,52):
		empDist.append((empDist[i-1] + groupBy[i]))
	return numpy.divide(empDist, bigN)
	
 ### makeCumUniDist(noCards): given the number of cards in your deck, this function will return an 1x52
 ##	 array of values of the uniform cummulative probabilites between 1:52
 ###
def makeCumUniDist(noCards):
	cumUniDist = range(1,noCards + 1)
	return numpy.divide(cumUniDist, noCards)
 ### ksTest(data): The Kolmogorov-Smirnov one-sample test. Given raw data (520x52) this function will,
 ##	 for each row, calculate the test statistic d = max( abs( (empDist(x) - cumDist(x)) ) ).
 ##	 The function will return 1x52 array where each index represents a card and each element represents
 ##	 the test statistic for said card. 
 ###
def ksTest(data):
	d = []
	ordered = orderByNum(data)
	numpy.savetxt("orderedRandData.csv", ordered, delimiter = ',')
	cumUniDist = makeCumUniDist(52)
	for i in range(52):
		thisRow = ordered[i]
		empDist = makeEmpDist(thisRow)
		d.append(max(numpy.abs(empDist - cumUniDist)))
	return d

def check(d):
	sigLevel = 0.07148022857352288099968307352592
	bool = False
	for i in range(52):
		if (d[i] > sigLevel):
			bool = True
	return bool
	
# alpha = 0.01 sig level -> 0.07148022857352288099968307352592
filename = "RandCardDist.csv"
data = numpy.genfromtxt(filename, delimiter = ',', names = True, dtype = None)
d = ksTest(data)

print(check(d), max(d))