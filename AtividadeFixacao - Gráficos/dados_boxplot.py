import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_boxplot.csv', sep=None, engine='python')

cols_num = df.select_dtypes(include=['number']).columns
cols_cat = df.select_dtypes(include=['object', 'category']).columns

plt.figure(figsize=(10, 6))

if len(cols_num) > 0:
    col_y = cols_num[0]
    
    if len(cols_cat) > 0:
        col_x = cols_cat[0]
        sns.boxplot(data=df, x=col_x, y=col_y, palette='Set2')
        plt.title(f'Boxplot de {col_y} por {col_x}')
    else:
        sns.boxplot(data=df, y=col_y, palette='Set2')
        plt.title(f'Boxplot de {col_y}')
else:
    print("Erro: Nenhuma coluna numérica foi encontrada no arquivo para gerar o Boxplot.")
    sns.boxplot(data=df, palette='Set2')
    plt.title('Boxplot dos Dados')

plt.tight_layout()
plt.savefig('grafico_boxplot.png')
plt.show()
