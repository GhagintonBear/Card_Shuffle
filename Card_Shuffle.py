import random


def definePilesList(X):
	pileHeight = (52//X) + 1
	pilesList = []
	for i in range(X):
		pilesList.append([])
	return pilesList

def myOrderedShuffleX(X, deck):
	pilesList = definePilesList(X)
	newPile = []
	for i in range(52):
		pilesList[i%X].append(deck[i])
	for i in range(X):
		pileSize = len(pilesList[i])
		for j in range(pileSize):
			newPile.append(pilesList[i][j])
	return (newPile)

def myUnorderedShuffleX(X, deck):
	pilesList = definePilesList(X)
	newPile = []
	for i in range(52):
		whichPile = random.randint(0,X-1)
		pilesList[whichPile].append(deck[i])
	# this bit of code will: 
	# randomCardDraw = list(range(52))
	# for i in range(52):
		# randomCard = random.choice(randomCardDraw)
		# pilesList[i%X].append(randomCard)
		# randomCardDraw.remove(randomCard)

	for i in range(X):
		pileSize = len(pilesList[i])
		for j in range(pileSize):
			newPile.append(pilesList[i][j])
	return (newPile)
	
def basicShuffle():
	#this shuffle will take out chunck of the cards leaving a random number of cards between [1,3] on the top and the bottom. The new order will be chunk, top few, bottom few.
	#note: bottom card will always remain on the bottom.
	
def logPosisition(deck):
	#After shuffle is complete, deck is passed here to log the final position of each card. 
	#format: after N Shuffles; rows - shuffleNumber, cols - final position in deck

orderedShuffle3 = myOrderedShuffleX(3, range(52))		
# orderedShuffle5 = myOrderedShuffleX(5)

# unorderedShuffle3 = myUnorderedShuffleX(3)
# unorderedShuffle5 = myUnorderedShuffleX(5)

