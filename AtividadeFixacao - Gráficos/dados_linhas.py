import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_linhas.csv')

cols_num = df.select_dtypes(include=['number']).columns

plt.figure(figsize=(10, 6))
if len(cols_num) > 1:
    x_col = cols_num[0]
    for y_col in cols_num[1:]:
        sns.lineplot(data=df, x=x_col, y=y_col, marker='o', label=y_col)
else:
    sns.lineplot(data=df, marker='o')

plt.title('Gráfico de Linhas / Tendência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_linhas.png')
plt.show()
