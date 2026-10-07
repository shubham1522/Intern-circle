import requests
from bs4 import BeautifulSoup
import json
import csv

URL = "https://quotes.toscrape.com"

def scrape_quotes():
    try:
        print("Fetching data...")

        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes_data = []

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)

            quotes_data.append({
                "author": author,
                "quote": text
            })

        # Save as JSON
        with open("quotes.json", "w", encoding="utf-8") as json_file:
            json.dump(quotes_data, json_file, indent=4, ensure_ascii=False)

        # Save as CSV
        with open("quotes.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Author", "Quote"])

            for item in quotes_data:
                writer.writerow([item["author"], item["quote"]])

        # Save as TXT
        with open("quotes.txt", "w", encoding="utf-8") as txt_file:
            for i, item in enumerate(quotes_data, start=1):
                txt_file.write(
                    f"{i}. {item['author']}\n"
                    f"   {item['quote']}\n\n"
                )

        print(f"\nSuccessfully scraped {len(quotes_data)} quotes.")
        print("Files created:")
        print("✓ quotes.json")
        print("✓ quotes.csv")
        print("✓ quotes.txt")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    scrape_quotes()