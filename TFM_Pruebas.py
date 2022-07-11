
import pandasql as ps
import pandas as pd
DatosPrueba = pd.read_csv(r'C:\Users\benja\Downloads\full_data.csv')
print(DatosPrueba.head(2))
describe = DatosPrueba.describe()
print(describe)