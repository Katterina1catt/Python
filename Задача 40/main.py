# Задача 40: Работать с файлом california_housing_train.csv, который 
# находится в папке sample_data. Определить среднюю стоимость дома, 
# где кол-во людей от 0 до 500 (population).

import pandas as pd

# Чтение данных из CSV файла
file_path = 'sample_data/california_housing_train.csv'
data = pd.read_csv(file_path)

# Фильтрация данных по количеству людей от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости домов в отфильтрованных данных
average_house_value = filtered_data['median_house_value'].mean()

print(f"Средняя стоимость дома с населением от 0 до 500: ${average_house_value:.2f}")