import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from utils import create_driver


class CoinMarketCapParser():
    def __init__(self) -> None:
        """Initialize browser driver and default URL."""
        self.driver = create_driver()
        self.url_template = "https://coinmarketcap.com/?page={page}"

    def open_page(self, page: int) -> bool:
        """Open the specified page number.

        Args:
            page (int): Page number to open.

        Returns:
            bool: True if page opened successfully, False otherwise.
        """
        try:
            self.driver.get(self.url_template.format(page=page))
            self.driver.implicitly_wait(2)
            return True
        except Exception as e:
            print(f"Failed to open page: {self.url_template.format(page=page)}. Error: {e}")
            return False
    
    def get_list_of_tokens(self) -> list:
        """Scrape tokens` data from the currently opened page.

        Returns:
            list: List of token dictionaries
        """
        # Scroll down for page loading
        for _ in range(10):
            self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
            
        # Extract page HTML
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        
        # Extract table content
        table = soup.find('table', attrs={"class": "cmc-table"}).find("tbody")
        if not table:
            return []
        
        tokens = list()
        
        # Parse tokens
        for tr in table.find_all('tr'):
            token_td = tr.find_all("td")[2]
            try:
                name = token_td.find('p').text.strip()
            except:
                continue
            try:
                symbol = token_td.find('p', attrs={"class": "coin-item-symbol"}).text.strip()
            except:
                continue
            try:
                link = token_td.find('a', attrs={"class": "cmc-link"}).get("href")
            except:
                continue
            try:
                cmc_id = int(token_td.find('img', attrs={"class": "coin-logo"}).get("src").split("/")[-1].split(".")[0])
            except:
                continue
            
            market_cap_td = tr.find_all("td")[7]
            try:
                market_cap = float(market_cap_td.find_all("span")[-1].text.strip().lstrip("$").replace(",", ""))
            except:
                continue
            
            token = {
                "name": name,
                "symbol": symbol,
                "link": link,
                "coinmarketcap_id": cmc_id,
                "market_cap": market_cap
            }
            tokens.append(token)

        return tokens        


if __name__ == "__main__":
    pages = 10
    parser = CoinMarketCapParser()
    tokens = list()
    
    for page in range(1, pages+1):
        if parser.open_page(page):
            tokens.extend(parser.get_list_of_tokens())
        else:
            print(f"Skipping page {page} due to error.")
        
    # Save tokens to JSON file
    filename = "data/top_tokens_by_marketcap.json"
    with open(filename, "wt") as file:
        json.dump(tokens, file, indent=4)
        
    print(f"Parsing completed. Total tokens parsed: {len(tokens)}.")
