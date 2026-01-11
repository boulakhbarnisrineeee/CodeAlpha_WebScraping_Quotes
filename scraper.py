import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com"
page_url = "/page/1/"

quotes_data = []

while True:
    url = base_url + page_url
    print("Scraping:", url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    if len(quotes) == 0:
        break

    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]

        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    next_btn = soup.find("li", class_="next")
    if next_btn:
        page_url = next_btn.find("a")["href"]
    else:
        break

df = pd.DataFrame(quotes_data)
df.to_csv("data/quotes.csv", index=False)

print("Done! Total quotes scraped:", len(df))
