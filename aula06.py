import pandas as pd
import numpy as np

# Dados de entrada fornecidos por vocês mesmo
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [28, 34, 29, None, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Belo Horizonte'],
    'Vendas': [150, 200, 300, 400, None]
}

# 1. Criar DataFrame
df = pd.DataFrame(dados)

# 4. Substituir valores faltantes na coluna Cidade por 'Desconhecido'
df['Cidade'].fillna('Desconhecido', inplace=True)

# 3. Calcular a média de idade dos clientes
media_idade = df['Idade'].mean()

# Substituir valores faltantes na coluna Idade pela média de idade pra não prejudicar nas análises
df['Idade'].fillna(media_idade, inplace=True)

# Substituir valores faltantes na coluna Vendas por 0 pra não prejudicar nas análises
df['Vendas'].fillna(0, inplace=True)

# 2. Filtrar clientes com mais de 30 anos
clientes_acima_30 = df[df['Idade'] > 30]

# 5. Calcular a soma total das vendas
soma_vendas = df['Vendas'].sum()

print("Clientes com mais de 30 anos:")
print(clientes_acima_30)
print("\nMédia de idade dos clientes:", media_idade)
print("\nDataFrame com valores faltantes substituídos:")
print(df)
print("\nSoma total das vendas:", soma_vendas)