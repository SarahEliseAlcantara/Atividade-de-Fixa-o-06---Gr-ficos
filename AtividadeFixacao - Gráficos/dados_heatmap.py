import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_heatmap.csv')

if df.select_dtypes(include=['object']).shape[1] == 1:
    df = df.set_index(df.columns[0])

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(axis=1, how='all')
df = df.loc[:, df.nunique() > 1]

plt.figure(figsize=(10, 8))

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)

plt.title('Mapa de Calor (Heatmap) de Correlação')
plt.tight_layout()
plt.savefig('grafico_heatmap.png')
plt.show()
