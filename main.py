from typing import Optional
import random, sys, logging
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
		return {"Show": "Root Page"}


@app.get("/items/{count}")
def read_item(count: int, q: Optional[str] = None):
	totalSets = int()
	finalSet = []
	setCounter = 0
	gameType = q

	if count > 1:
		totalSets = int(count)
		print(f"Printing {totalSets} of {gameType} numbers")
		while setCounter < totalSets:
			finalSet.append( generator(gameType) )
			setCounter += 1

	else:
		print(f"Printing 1 set of {gameType} numbers")
		finalSet.append( generator(gameType) )

	# resultSet = {"gameType": q}
	resultSet = []
	dict = {}

	for key, i in enumerate(finalSet):
		# resultSet[f"numset_{key+1}"] = i
		# resultSet["gameType"]= q
		# resultSet[f"numset_{key}"] = i
		dict = {"gameType" : q,f"numset_{key+1}" : i}
		resultSet.append(dict)

	return resultSet

# Functions
def generator(drawtype):
	counter = 0
	numSet = []
	n = int()
	# powerball 69-26
	# mega millions 70-25
	maxWhtNum = 69
	maxRedNum = 25

	if drawtype == 'power_ball':
		maxWhtNum = 69
		maxRedNum = 26
	elif drawtype == 'mega_millions':
		maxWhtNum = 70
		maxRedNum = 25

	try:
		while counter < 5:
			n = random.randint(1,69)
			if n not in numSet:
				numSet.append(n)
				counter += 1
			if len(numSet) == 5:
				r = random.randint(1,26)
				numSet.append(r)
		
		return numSet
	except:
		e_msg = f"Unable to generate {drawtype} numbers"
		logging.critical(e_msg)
		return e_msg