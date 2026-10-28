import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://gamestore.kg/product-category/sony-playstation/pristavki-ps5/games-ps5/'

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9",
}

products = []
for page in range(1, 4):
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

        product = {
            "name": name,
            "price": price,
            "old_price": old_price,
            "link": link,
        }
        products.append(product)

    time.sleep(1)


print("Всего товаров: ", len(products))
print(products[1])
print(products[-1])