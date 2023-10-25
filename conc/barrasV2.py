import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ler os arquivos csv
df1 = pd.read_csv('bakery.csv', delimiter=';', decimal=',')


# Converter a coluna 'Tempo de Execução' para segundos
df1['Tempo de Execução'] = df1['Tempo de Execução'].apply(lambda x: int(x.split('m')[0])*60 + float(x.split('m')[1].replace('s','').replace(',', '.')))


bar_width = 0.35
r1 = np.arange(len(df1['N']))

plt.figure(figsize=(10,6))

# Criar as barras
plt.bar(r1, df1['Tempo de Execução'], color='b', width=bar_width, edgecolor='grey', label='bakery.csv')
#plt.bar(r1 + bar_width, df2['Tempo de Execução'], color='r', width=bar_width, edgecolor='grey', label='atomic.csv')

# Adicionar legendas
plt.xlabel('N', fontweight='bold')
plt.ylabel('Tempo de Execução (s)', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(df1['N']))], df1['N'])

plt.legend()
plt.show()
