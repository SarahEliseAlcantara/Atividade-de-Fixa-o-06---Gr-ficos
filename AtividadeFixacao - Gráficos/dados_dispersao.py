import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_dispersao.csv')

cols_num = df.select_dtypes(include=['number']).columns
x_col, y_col = cols_num[0], cols_num[1]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.7)
plt.title(f'Gráfico de Dispersão: {y_col} vs {x_col}')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('grafico_dispersao.png')
plt.show()
