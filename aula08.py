import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_turma1 = {'Aluno': ['Dâmarys', 'Yarin', 'Victor'], 'Nota': [9, 7, 'A']}
dados_turma2 = {'Aluno': ['Diana', 'Thina', 'Gleuber'], 'Nota': [6, 'B', 8]}
dados_turma3 = {'Aluno': ['Gustavo', 'Laines', 'Joyce'], 'Nota': ['C', 10, 5]}

df1 = pd.DataFrame(dados_turma1)
df2 = pd.DataFrame(dados_turma2)
df3 = pd.DataFrame(dados_turma3)

def converter_nota(nota):
    if nota == 'A':
        return 10
    elif nota == 'B':
        return 8
    elif nota == 'C':
        return 6
    else:
        return int(nota)

df1['Nota'] = df1['Nota'].apply(converter_nota)
df2['Nota'] = df2['Nota'].apply(converter_nota)
df3['Nota'] = df3['Nota'].apply(converter_nota)
df_combined = pd.concat([df1, df2, df3])
df_combined['Nota'] = df_combined['Nota'].apply(lambda x: x if 0 <= x <= 10 else (x/10)*10)

print(df_combined.describe())
plt.figure(figsize=(10, 6))
sns.barplot(x=df_combined['Aluno'], y=df_combined['Nota'])
plt.title('Dispersão das notas por Aluno')
plt.xlabel('Aluno')
plt.ylabel('Nota')
plt.show()