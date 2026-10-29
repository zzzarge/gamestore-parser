import pandas as pd

# 1. Загрузка сырых данных от парсера
df = pd.read_csv("data/products.csv")

# 2. Цены из текста "3 690сом" в число 3690.0
df["price"] = df["price"].str.replace(r"\D", "", regex=True).astype(float)
df["old_price"] = df["old_price"].str.replace(r"\D", "", regex=True).astype(float)

# 3. Удаление дублей (один товар в двух категориях)
df = df.drop_duplicates(subset="link")

# 4. Проверки
sale = df[df["old_price"].notna()]
print("Товаров со скидкой:", len(sale))
print("Ошибочных скидок:", (sale["old_price"] <= sale["price"]).sum())
print("Дублей осталось:", df["link"].duplicated().sum())

# 5. Сохранение
df.to_csv("data/products_clean.csv", index=False, encoding="utf-8-sig")
print("Сохранено:", len(df), "товаров")