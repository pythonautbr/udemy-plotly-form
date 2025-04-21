import pandas as pd

ecom_sales = pd.read_csv('data/ecom_sales.csv')
# O que a linha abaixo faz? Resposta:
# Agrupa os dados por país e soma o valor de cada venda
ecom_sales_new = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='TotalSales (R$)')
print(ecom_sales_new)
