#%%
## Extract
import pandas as pd
import sqlite3
df = pd.read_csv('./data/data.csv', encoding='latin1') 
print(df.head())
# %%

## -- Transform
df = df.dropna() 
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) 
df['month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
df['TotalPrice'] = df['UnitPrice'] * df['Quantity']

sales_by_month = df.groupby('month')['TotalPrice'].sum().reset_index()
sales_by_month



# %%
## -- Load
conn = sqlite3.connect('sales_database.db')
sales_by_month.to_sql('sales_by_month', conn, if_exists='replace', index=False)
conn.close()

print("Vendas por mês salvas no banco!")
# %%
