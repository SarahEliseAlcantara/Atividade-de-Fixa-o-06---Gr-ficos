import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_regressao.csv')

cols_num = df.select_dtypes(include=['number']).columns
x_col, y_col = cols_num[0], cols_num[1]

plt.figure(figsize=(10, 6))
sns.regplot(data=df, x=x_col, y=y_col, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title(f'Tendência e Regressão Linear: {y_col} vs {x_col}')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico_regressao.png')
plt.show()
