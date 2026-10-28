import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

categories = {
    'PS5 Игры': 'https://gamestore.kg/product-category/sony-playstation/pristavki-ps5/games-ps5/',
    'PS4 Игры': 'https://gamestore.kg/product-category/sony-playstation/sony-ps4/ps4/',
    'Xbox Игры': 'https://gamestore.kg/product-category/microsoft-xbox/igry-xbox/',
    'Switch Игры': 'https://gamestore.kg/product-category/nintendo/ns-game/',
    'Switch 2 Игры': 'https://gamestore.kg/product-category/nintendo/ns2-games/',

    'PS5 Приставки': 'https://gamestore.kg/product-category/sony-playstation/pristavki-ps5/pristavki-ps5-pristavki-ps5/',
    'PS4 Приставки': 'https://gamestore.kg/product-category/sony-playstation/sony-ps4/pristavki-ps4/',
    'Xbox Приставки': 'https://gamestore.kg/product-category/microsoft-xbox/xbox-console/',
    'Nintendo Приставки': 'https://gamestore.kg/product-category/nintendo/nintendo-nintendo/',
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9",
}

products = []

for category, base_url in categories.items():
    print("=== Категория:", category)

    for page in range(1, 100):
        if page == 1:
            url = base_url
        else:
            url = base_url + "page/" + str(page) + "/"

        print("Страница", page, url)

        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print("Страница не открылась")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select("div.wd-product")
        if len(cards) == 0:
            print("Карточек нет")
            break

        for card in cards:
            title_el = card.select_one("h3.wd-entities-title a")

            price_el = card.select_one("span.price ins .woocommerce-Price-amount")
            if price_el is None:
                price_el = card.select_one("span.price .woocommerce-Price-amount")

            old_price_el = card.select_one("span.price del .woocommerce-Price-amount")
            if old_price_el is None:
                old_price = None
            else:
                old_price = old_price_el.get_text(strip=True)

            name = title_el.get_text(strip=True)
            link = title_el.get("href")
            price = price_el.get_text(strip=True)
            in_stock = "instock" in card.get("class", [])

            product = {
                "name": name,
                "price": price,
                "old_price": old_price,
                "category": category,
                "in_stock": in_stock,
                "link": link,
            }
            products.append(product)

        time.sleep(1)

df = pd.DataFrame(products)
print(df.head())
print(df["category"].value_counts())

df.to_csv("data/products.csv", index=False, encoding="utf-8-sig")
print("Сохранено в data/products.csv")