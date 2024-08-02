# CoinMarketCap-Parser
The project on data parsing from the web page about crypto market tokens.
## Goal
Program aplies user to parse https://coinmarketcap.com/ html and extracts base tokens` info.
## Params
pages: int - count of top pages user is interested in
## Skills Required:
- Object-Oriented Programming
- Python
- Selenium tools
- Programmable browser using
- BeautifulSoup4
## Output
A JSON file includes tokens` data. There are Name, Symbol, Link, CoinMarketCap ID, Market Cap object`s propetry. By default the data is sorted by Market Cap.
## Understanding Page Source
![HTML Data Positions](https://github.com/the2roock/CoinMarketCap-Parser/blob/main/Understanding%20Page%20Source.png?raw=true)
## Usage
### 1. Import json for data writing into JSON and CoinMarketCapParser class from parser.py module for parser initialization.
```
import json
from parser import CoinMarketCapParser
```
### 2. Init pages cound and parser object.
```
pages = 10
parser = CoinMarketCapParser()
```
### 3. Extract data using parser object and storage in tokens list.
```
tokens = list()
for page in range(1, pages+1):
    parser.open_page(page)
    tokens.extend(parser.get_list_of_tokens())
tokens[:5]
```
[{'name': 'Bitcoin',
  'symbol': 'BTC',
  'link': '/currencies/bitcoin/',
  'coinmarketcap_id': 1,
  'market_cap': 1271211507374.0},
 {'name': 'Ethereum',
  'symbol': 'ETH',
  'link': '/currencies/ethereum/',
  'coinmarketcap_id': 1027,
  'market_cap': 378710168994.0},
 {'name': 'Tether',
  'symbol': 'USDT',
  'link': '/currencies/tether/',
  'coinmarketcap_id': 825,
  'market_cap': 114414783872.0},
 {'name': 'BNB',
  'symbol': 'BNB',
  'link': '/currencies/bnb/',
  'coinmarketcap_id': 1839,
  'market_cap': 83346363029.0},
 {'name': 'Solana',
  'symbol': 'SOL',
  'link': '/currencies/solana/',
  'coinmarketcap_id': 5426,
  'market_cap': 76318859105.0}]
### 4. Save data in file.
```
with open("data/top_tokens_by_marketcap.json", "wt") as file:
    json.dump(tokens, file, indent=4)
    
print(f"Parsing ends. There are {len(tokens)} tokens.")
```
Parsing ends. There are 999 tokens.
