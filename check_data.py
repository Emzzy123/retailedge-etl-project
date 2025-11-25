import pandas as pd

customers = pd.read_csv("data/raw/customers_large.csv")
print(customers.head())
print(customers.info())