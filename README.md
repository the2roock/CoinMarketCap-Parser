# CoinMarketCap-Parser

The project focuses on parsing data from the CoinMarketCap website about cryptocurrency tokens.

## Goal

Program aplies user to parse https://coinmarketcap.com/ html and extracts base tokens` info.

## Parameters

- `pages`: `int` - number of top pages the user is interested in
  
## Skills Required

- Object-Oriented Programming
- Python
- Selenium tools
- Programmable browser using
- BeautifulSoup4
  
## Output
The output is a JSON file that includes token data sorted by Market Cap. Each token includes:
- Name
- Symbol
- Link
- CoinMarketCap ID
- Market Cap

## Understanding Page Source

![HTML Data Positions](https://github.com/the2roock/CoinMarketCap-Parser/blob/main/Understanding%20Page%20Source.png?raw=true)

## Usage

### 1. Import json for data writing into JSON and CoinMarketCapParser class from parser.py module for parser initialization.
```python
import json
from parser import CoinMarketCapParser
```

### 2. Init pages cound and parser object.
```python
pages = 10
parser = CoinMarketCapParser()
```

### 3. Extract data using parser object and storage in tokens list.
```python
tokens = list()
for page in range(1, pages+1):
    parser.open_page(page)
    tokens.extend(parser.get_list_of_tokens())
print(tokens[:5]) # Displaying the first 5 tokens for preview
```

### 4. Save data in file.
```python
with open("data/top_tokens_by_marketcap.json", "wt") as file:
    json.dump(tokens, file, indent=4)
    
print(f"Parsing ends. There are {len(tokens)} tokens.")
```
Parsing ends. There are 999 tokens.
