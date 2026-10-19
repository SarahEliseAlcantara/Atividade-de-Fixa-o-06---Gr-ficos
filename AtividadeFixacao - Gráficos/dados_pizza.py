import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados_pizza.csv')

col_label = df.select_dtypes(include=['object', 'category']).columns[0]
col_value = df.select_dtypes(include=['number']).columns[0]

plt.figure(figsize=(8, 8))
plt.pie(df[col_value], labels=df[col_label], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title(f'Distribuição Percentual - {col_label}')
plt.tight_layout()
plt.savefig('grafico_pizza.png')
plt.show()
