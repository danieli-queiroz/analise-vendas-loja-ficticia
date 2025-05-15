import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

print(data.head())
print(data.info())


data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])
data['Month'] = data['ORDERDATE'].dt.month
data['Year'] = data['ORDERDATE'].dt.year
data['DayOfWeek'] = data['ORDERDATE'].dt.dayofweek

formatador = mtick.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.'))


monthly_sales = data.groupby('Month').agg({'SALES': 'sum'}).reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x='Month', y='SALES', data=monthly_sales, palette='Blues_d')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas Totais')
plt.gca().yaxis.set_major_formatter(formatador)
plt.show()

top_products = data.groupby('PRODUCTCODE').agg({'SALES': 'sum'}).reset_index().sort_values(by='SALES', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='SALES', y='PRODUCTCODE', data=top_products, palette='coolwarm')
plt.title('Top 10 Produtos Mais Vendidos')
plt.xlabel('Vendas Totais')
plt.ylabel('Código do Produto')
plt.gca().xaxis.set_major_formatter(formatador)
plt.show()

ticket_medio = data.groupby('CUSTOMERNAME').agg({'SALES': 'sum'}).reset_index()
media_ticket = ticket_medio['SALES'].mean()
print(f'Ticket médio por cliente: ${media_ticket:,.2f}'.replace(',', '.'))

status_sales = data.groupby('STATUS').agg({'SALES': 'sum'}).reset_index().sort_values(by='SALES', ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x='SALES', y='STATUS', data=status_sales, palette='Set2')
plt.title('Vendas por Status do Pedido')
plt.xlabel('Vendas Totais')
plt.ylabel('Status')
plt.gca().xaxis.set_major_formatter(formatador)
plt.show()

country_sales = data.groupby('COUNTRY').agg({'SALES': 'sum'}).reset_index().sort_values(by='SALES', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='SALES', y='COUNTRY', data=country_sales, palette='mako')
plt.title('Top 10 Países com Mais Vendas')
plt.xlabel('Vendas Totais')
plt.ylabel('País')
plt.gca().xaxis.set_major_formatter(formatador)
plt.show()

territory_sales = data.groupby('TERRITORY').agg({'SALES': 'sum'}).reset_index().sort_values(by='SALES', ascending=False)
plt.figure(figsize=(10,6)) 
ns.barplot(x='SALES', y='TERRITORY', data=territory_sales, palette='rocket')
plt.title('Vendas por Território')
plt.xlabel('Vendas Totais')
plt.ylabel('Território')
plt.gca().xaxis.set_major_formatter(formatador)
plt.show()

top_customers = data.groupby('CUSTOMERNAME').agg({'SALES': 'sum'}).reset_index().sort_values(by='SALES', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='SALES', y='CUSTOMERNAME', data=top_customers, palette='cool')
plt.title('Top 10 Clientes Mais Lucrativos')
plt.xlabel('Vendas Totais')
plt.ylabel('Cliente')
plt.gca().xaxis.set_major_formatter(formatador)
plt.show()

dias_semana = {0: 'Seg', 1: 'Ter', 2: 'Qua', 3: 'Qui', 4: 'Sex', 5: 'Sáb', 6: 'Dom'}
data['DiaSemana'] = data['DayOfWeek'].map(dias_semana)
weekday_sales = data.groupby('DiaSemana').agg({'SALES': 'sum'}).reindex(['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'])
plt.figure(figsize=(10,6))
sns.barplot(x=weekday_sales.index, y='SALES', data=weekday_sales.reset_index(), palette='viridis')
plt.title('Vendas por Dia da Semana')
plt.xlabel('Dia')
plt.ylabel('Vendas Totais')
plt.gca().yaxis.set_major_formatter(formatador)
plt.show()