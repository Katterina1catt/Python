# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
# из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() 

import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем словарь для one-hot представления
one_hot_dict = {val: [1 if v == val else 0 for v in lst] for val in set(lst)}

# Создаем DataFrame на основе словаря
data = pd.DataFrame(one_hot_dict)

# Переименовываем столбцы, чтобы они соответствовали оригинальным значениям
data.columns = list(set(lst))

data.head()