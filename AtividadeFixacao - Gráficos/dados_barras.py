import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_barras.csv')

col_x = df.select_dtypes(include=['object', 'category']).columns[0]
col_y = df.select_dtypes(include=['number']).columns[0]

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x=col_x, y=col_y, palette='viridis')
plt.title(f'Gráfico de Barras - {col_y} por {col_x}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_barras.png')
plt.show()
