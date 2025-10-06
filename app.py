import requests
from bs4 import BeautifulSoup


rates = {
    "USD": 1.25,
    "KES": 160.0,
    "EUR": 1.15,
    "INR": 104.0
}

url = "https://books.toscrape.com/"


target = input("Enter target currency (USD, KES, EUR, INR): ").upper()
exchange_rate = rates.get(target)

if not exchange_rate:
    print(" Unsupported currency. Choose from:", ", ".join(rates.keys()))
    exit()

r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")

print(f"\n Book Prices (GBP → {target})\n")

for item in soup.select(".product_pod")[:10]:
    title = item.h3.a["title"]
    price_text = item.select_one(".price_color").text
    price_clean = price_text.encode("ascii", "ignore").decode().replace("£", "").strip()
    price_gbp = float(price_clean)
    price_target = round(price_gbp * exchange_rate, 2)
    print(f"{title[:40]:40} | £{price_gbp:<6} → {target} {price_target}")

