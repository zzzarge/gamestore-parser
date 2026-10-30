import pandas as pd
import numpy as np

df = pd.read_csv('data/products_clean.csv')

games = df[df['category'].str.contains('Игры')]
prices = games['price'].to_numpy()

print('Игр: ', len(games))
print('Средняя цена: ', np.mean(prices))
print('Медиана: ', np.median(prices))
print('Максимум: ', np.max(prices))
print('Минимум: ', np.min(prices))
print('Стандартное отклонение', np.std(prices))