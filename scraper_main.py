import requests
from bs4 import BeautifulSoup

def scrape_stock_data():
    url = f'https://www.investing.com/equities/sri-lanka'
    response = requests.get(url)
    
    
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find(id="cross_rate_markets_stocks_1")
        table_headings = table.find_all('th')
        table_data = table.find_all('td')
        #table_data.sort(key=lambda tag: tag.text)

        for row in table_data:
            print(row.text)

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
    
scrape_stock_data()