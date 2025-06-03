import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuração geral dos gráficos
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 10

# Leitura dos dados
df = pd.read_csv("dados_abastecimento_agua_brasil.csv")

## GRÁFICO 1: Comparação entre Cobertura Total e Urbana por Estado/Região
plt.figure(figsize=(14, 8))

# Dados para o gráfico
estados = df["Estado"]
cobertura_total = df["CoberturaTotal (%)"]
cobertura_urbana = df["CoberturaUrbana (%)"]
x = np.arange(len(estados))
width = 0.35

# Plotagem
bars1 = plt.bar(x - width/2, cobertura_total, width, label='Cobertura Total', color='#1f77b4', edgecolor='black')
bars2 = plt.bar(x + width/2, cobertura_urbana, width, label='Cobertura Urbana', color='#2ca02c', edgecolor='black')

# Customização
plt.title('Comparação entre Cobertura Total e Urbana por Estado/Região (2021-2022)', fontweight='bold', pad=20)
plt.ylabel('Percentual de Cobertura (%)', fontweight='bold')
plt.xticks(x, estados, rotation=45, ha='right')
plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando valores nas barras
for bar in bars1 + bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom', fontsize=9)

plt.legend(loc='upper right', frameon=True)
plt.tight_layout()
plt.show()

## GRÁFICO 2: Evolução da Cobertura de Água e Esgoto no Brasil (2014-2022)
# Dados extraídos do PDF
anos = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
agua = [83, 83, 83, 84, 84, 84, 84, 84, 85]
esgoto = [50, 50, 52, 52, 53, 54, 55, 56, 56]

plt.figure(figsize=(14, 7))

# Plotagem
plt.plot(anos, agua, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=8, label='Cobertura de Água')
plt.plot(anos, esgoto, marker='s', linestyle='--', color='#ff7f0e', linewidth=2.5, markersize=8, label='Cobertura de Esgoto')

# Customização
plt.title('Evolução da Cobertura de Água e Esgoto no Brasil (2014-2022)', fontweight='bold', pad=20)
plt.xlabel('Ano', fontweight='bold')
plt.ylabel('Percentual de Cobertura (%)', fontweight='bold')
plt.xticks(anos)
plt.yticks(np.arange(45, 90, 5))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right', frameon=True)

# Adicionando valores nos pontos
for i, txt in enumerate(agua):
    plt.annotate(f"{txt}%", (anos[i], agua[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(esgoto):
    plt.annotate(f"{txt}%", (anos[i], esgoto[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()

## GRÁFICO 3: Formas de Abastecimento de Água no Brasil (2016-2022)
# Dados extraídos do PDF
categorias = ['Rede geral', 'Poço profundo', 'Poço raso', 'Fonte/nascente', 'Outra']
dados_2016 = [85.8, 7.1, 2.9, 2.0, 2.2]
dados_2019 = [85.5, 7.1, 3.2, 2.1, 2.0]
dados_2022 = [85.5, 7.8, 2.8, 2.0, 1.8]

x = np.arange(len(categorias))
width = 0.25

plt.figure(figsize=(14, 7))

# Plotagem
bars1 = plt.bar(x - width, dados_2016, width, label='2016', color='#1f77b4', edgecolor='black')
bars2 = plt.bar(x, dados_2019, width, label='2019', color='#2ca02c', edgecolor='black')
bars3 = plt.bar(x + width, dados_2022, width, label='2022', color='#d62728', edgecolor='black')

# Customização
plt.title('Distribuição das Formas de Abastecimento de Água no Brasil (2016-2022)', fontweight='bold', pad=20)
plt.xlabel('Tipo de Abastecimento', fontweight='bold')
plt.ylabel('Percentual de Domicílios (%)', fontweight='bold')
plt.xticks(x, categorias)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando valores nas barras
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1f}%',
                 ha='center', va='bottom', fontsize=9)

plt.legend(title='Ano', loc='upper right', frameon=True)
plt.tight_layout()
plt.show()

## GRÁFICO 4: Cobertura por Rede Geral nas Grandes Regiões (2022)
# Dados extraídos do PDF
regioes = ['Brasil', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
total = [85.5, 60.0, 80.3, 93.3, 93.3, 93.3]  # Valores aproximados do gráfico
urbana = [93.3, 69.9, 89.7, 96.0, 96.0, 96.0]  # Valores aproximados do gráfico

x = np.arange(len(regioes))
width = 0.35

plt.figure(figsize=(14, 7))

# Plotagem
bars1 = plt.bar(x - width/2, total, width, label='Total', color='#1f77b4', edgecolor='black')
bars2 = plt.bar(x + width/2, urbana, width, label='Urbana', color='#ff7f0e', edgecolor='black')

# Customização
plt.title('Cobertura por Rede Geral nas Grandes Regiões do Brasil (2022)', fontweight='bold', pad=20)
plt.xlabel('Região', fontweight='bold')
plt.ylabel('Percentual de Cobertura (%)', fontweight='bold')
plt.xticks(x, regioes)
plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando valores nas barras
for bar in bars1 + bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom', fontsize=9)

plt.legend(title='Tipo de Cobertura', loc='upper right', frameon=True)
plt.tight_layout()
plt.show()