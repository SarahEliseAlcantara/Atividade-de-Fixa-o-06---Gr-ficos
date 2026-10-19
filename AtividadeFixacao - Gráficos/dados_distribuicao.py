import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_distribuicao.csv')

col_num = df.select_dtypes(include=['number']).columns[0]

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x=col_num, kde=True, color='skyblue')
plt.title(f'Distribuição de Frequência de {col_num}')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico_distribuicao.png')
plt.show()
