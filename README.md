# draw-game-number-gen

## Dependency

The API that serves the generated number sets runs off of FastAPI and needs uvicorn to be installed.
Command to set this up is:

### FastAPI & Uvicorn

```
pip install fastapi
pip install "uvicorn[standard]"
```

### Run Uvicorn

Once uvicorn is installed run the following command to serve the FastAPI app:

```
python -m uvicorn
```

### ToDo's left for this app

- [x] create api to serve mega millions and powerball number sets
- [] decide on jinja or a reactive framework to build front-end
- [] create front end to pick game type and total number sets
- [] add more options to for the other state based draw games

## API Usage

### Url Query Parameters

```
http://[url_address]/items/4?q=power_ball
```

The first number after items (4 in this example) is how many number sets are to be generated.
To pick the game type (currently only Powerball or Mega Millions), send either ?q=power_ball or ?q=mega_millions
This will return and array of objects:

```
[
  {
    "gameType": "power_ball",
    "numset_1": [
      53,
      69,
      14,
      4,
      68,
      19
      ]
  },
  {
    "gameType": "power_ball",
    "numset_2": [
      7,
      18,
      12,
      10,
      13,
      19
    ]
  },
  {
    "gameType": "power_ball",
    "numset_3": [
      24,
      47,
      17,
      42,
      15,
      15
    ]
  },
  {
    "gameType": "power_ball",
    "numset_4": [
      62,
      58,
      11,
      65,
      9,
      1
    ]
  }
]
```
