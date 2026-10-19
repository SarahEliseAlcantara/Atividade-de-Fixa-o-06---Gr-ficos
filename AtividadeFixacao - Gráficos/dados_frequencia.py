import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_frequencia.csv')

col_cat = df.select_dtypes(include=['object', 'category']).columns[0]

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x=col_cat, palette='pastel', order=df[col_cat].value_counts().index)
plt.title(f'Frequência de Ocorrências por {col_cat}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_frequencia.png')
plt.show()
