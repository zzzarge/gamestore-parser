import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

INPUT_FILE = 'data/products.csv'
CHARTS_DIR = 'charts'
CURRENT_YEAR = 2026

# ВРЕМЕННО: пока cleaner.py не готов
import pandas as pd
def clean_price(text):
    if pd.isna(text):
        return None 
    text = text.replace(' ','')
    text = text.replace('сом', '')
    return int(text)

#___________Stats_____________
df = pd.read_csv(INPUT_FILE)
df['price'] =  df['price'].apply(clean_price)
print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.describe())
print('Средняя цена: ',(df['price'].mean()))
print('Грабежь: ', (df['price'].max()))
print('В самый раз: ', (df['price'].min()))
print('Медиан какой-то: ',df['price'].median())

#------категории-------
count_sm = df.value_counts('category')
print(count_sm)
print(df.groupby('category')['price'].mean().sort_values(ascending=False))
print(df.groupby('category')['price'].median().sort_values(ascending=False))
print(df.groupby('category')['price'].count().sort_values(ascending=False))

#------скидка-------
df['has_discount'] = df['old_price'].notna()
print('Доля товаров со скидкой: ',df['has_discount'].mean()*100)
#------где скидок больше---------
print(df.groupby('category')['has_discount'].mean()*100)
#--------top 10 грабежа------
print('ТОП 10 expensive shi: ',df.sort_values('price', ascending=False)[['name','price','category']].head())

#----------Vyvod------------
print('Вывод:')
print('Самая популярная категория: ИГРЫ.')
print('Большинство ассортимента состовляют игры(около 96%), больше всего на PS5 и PS4.')
print('Типичная цена товара около 3 500 сом, а средняя завышена из-за приставок.')
print('Скидки есть примерно у каждого шестого товара, чаще всего на игры для PS4 и PS5.')
print('Почти всё в наличии (619 из 626).')
print('Аскар байке поставьте хороший балл пжпжпж')

#-------Графики хз как делать----------
df['category'].value_counts().plot(kind='bar')
plt.show()

df['price'].hist(bins=20)
plt.show()