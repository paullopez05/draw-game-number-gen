import random, sys, json, logging
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
		return {"Show": "Root Page"}


@app.get("/items/{count}", response_class=HTMLResponse)
def read_item(request: Request, count: int, q: Optional[str] = None):
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

	resultSet = []
	dict = {}

	for key, i in enumerate(finalSet):
		dict = {"gameType" : q, "numset" : i}
		resultSet.append(dict)

	return templates.TemplateResponse("item.html", {"request": request, "results": resultSet})

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