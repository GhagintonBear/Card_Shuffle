import os
import struct
import random
import numpy


def createRandomDeck():
	deck = []
	checkList = list (range(1,53))
	for i in range(52):
		randomCard = random.choice(checkList)
		deck.append(randomCard)
		checkList.remove(randomCard)
	return deck

def cardGuess(shuffledDeck):
	correctGuess = 0
	checkList = list (range(1,53))
	for i in range(52):
		thisCard = shuffledDeck[i]
		randomCard = random.choice(checkList)
		if(randomCard == thisCard):
			correctGuess += 1
		checkList.remove(thisCard)
	return correctGuess
		
def generateRandom52():
	randNum = 0
	while (randNum < 1 or randNum > 52):
		randNum = struct.unpack('I', os.urandom(4))[0] % 100
	return randNum
	
def trialRun(deck):
	output = []
	for i in range(100):
		output.append(cardGuess(deck))
	return list(output)

orderedDeck = trialRun(range(1,53))
randomDeck = trialRun(createRandomDeck())


print("Summary stats on the correct guesses on a new deck:", "Mean =", numpy.mean(orderedDeck), "and Variance =", numpy.var(orderedDeck))
print("Summary stats on the correct guesses on a random deck:","Mean =", numpy.mean(randomDeck), "and Variance =", numpy.var(randomDeck))