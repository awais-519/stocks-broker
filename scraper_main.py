import requests
from bs4 import BeautifulSoup
import re


def remove_emojis(text):
    # Remove emojis and other non-ASCII characters using regex
    return re.sub(r'[^\x00-\x7F]+', '', text)


def scrape_stock_data():
    url = f'https://www.investing.com/equities/sri-lanka'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find(id="cross_rate_markets_stocks_1")
        table_headings = table.find_all('th')
        table_rows = table.find_all('tr')

        for heading in table_headings:
            cleaned_heading = remove_emojis(heading.text)
            print(cleaned_heading, end=" " + " ")

        print("\n")

        for row in table_rows:
            # Skip the table header row
            if row == table.find('tr'):
                continue

            # Extract and clean the data from each cell in the row
            cells = row.find_all(['th', 'td'])
            cleaned_cells = [remove_emojis(cell.text) for cell in cells]

            # Print the cleaned row data
            print("  ".join(cleaned_cells))

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


scrape_stock_data()
