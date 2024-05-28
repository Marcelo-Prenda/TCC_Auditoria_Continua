import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar uma lista de CPFs únicos
def gerar_lista_cpfs_unicos(n):
    cpfs_unicos = set()
    while len(cpfs_unicos) < n:
        cpf = [random.randint(0, 9) for _ in range(9)]
    
        # Calculando os dígitos verificadores
        s = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
        d1 = (s * 10) % 11
        cpf.append(d1 if d1 < 10 else 0)
        
        s = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
        d2 = (s * 10) % 11
        cpf.append(d2 if d2 < 10 else 0)
        
        # Formatar o CPF
        cpf_str = ''.join(map(str, cpf))
        cpf_formatado = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
        
        cpfs_unicos.add(cpf_formatado)
    
    return list(cpfs_unicos)



# Lista de nomes e sobrenomes fictícios
nomes = ['João', 'Marcelo','Maria', 'Pedro', 'Ana', 'José', 'Irani', 'Carlos', 'Rosimeri', 'Gabriel', 'Priscila', 'Igor', 'Leticia', 'Telma', 'Noemi', 'Alexandre', 'Daniel', 'Gloria', 'Fatima', 'Augusto', 'Samuel']
sobrenomes = ['Silva', 'Prenda','Santos', 'Oliveira', 'Souza', 'Costa', 'Pereira', 'Rodrigues', 'Cristina', 'Cunha', 'Ferreira',"Sant' Anna", 'Maia', 'Albernaz','Matos'] 

# Criando a lista de CPFs únicos
cpfs_unicos = gerar_lista_cpfs_unicos(1000000)

# Criando a base de dados
dados = []
for _ in range(1000000):
    nome = random.choice(nomes) + ' ' + random.choice(sobrenomes) + ' ' + random.choice(sobrenomes)
    idade = random.randint(18, 80)
    valor_emprestimo = random.randint(20000, 150000)
    cpf = cpfs_unicos.pop()
    dados.append([nome, idade, valor_emprestimo, cpf])

# Criando o DataFrame com os dados
df = pd.DataFrame(dados, columns=['NOME', 'IDADE', 'VALOR_EMPRESTIMO', 'CPF'])

# Criando a coluna de datas
data_atual = datetime.now()
primeiro_dia_mes_atual = data_atual.replace(day=1)
datas = [primeiro_dia_mes_atual + timedelta(days=random.randint(0, (data_atual - primeiro_dia_mes_atual).days)) for _ in range(len(df))]
df['DATA'] = datas
df['DATA'] = df['DATA'].dt.date

prazos_anos = [random.randint(1, 10) for _ in range(len(df))]

# Convertendo os prazos de anos para meses
prazos_meses = [ano * 12 for ano in prazos_anos]

# Adicionando a coluna de prazos em meses ao DataFrame
df['PRAZO'] = prazos_meses

df['PARCELA'] = ((df['VALOR_EMPRESTIMO'] * 0.0097 * df['PRAZO'] + df['VALOR_EMPRESTIMO']).round(2) / df['PRAZO']).round(2)