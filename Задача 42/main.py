# Задача 42: Узнать какая максимальная households в зоне минимального 
# значения population.

import pandas as pd

# Чтение данных из CSV файла
file_path = 'sample_data/california_housing_train.csv'
data = pd.read_csv(file_path)

# Найдем минимальное значение population
min_population = data['population'].min()

# Отфильтруем данные для зоны с минимальным значением population
zone_with_min_population = data[data['population'] == min_population]

# Найдем максимальное значение households в этой зоне
max_households = zone_with_min_population['households'].max()

print(f"Максимальное количество households в зоне с минимальным значением population: {max_households}")
