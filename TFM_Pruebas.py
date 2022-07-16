
import pandasql as ps
import pandas as pd
DatosPrueba = pd.read_csv(r'C:\Users\benja\Downloads\full_data.csv')
print(DatosPrueba.head(2))
describe = DatosPrueba.describe()
print(describe)

import zipfile
with zipfile.ZipFile(r'C:\Users\benja\Downloads\ashrae-energy-prediction.zip', 'r') as zip_ref:
    zip_ref.extractall(r'C:\Users\benja\Downloads\data')
print("a")