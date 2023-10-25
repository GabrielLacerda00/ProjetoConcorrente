import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo csv
df = pd.read_csv('results.csv', delimiter=';', decimal=',')

# Converter a coluna 'Tempo de Execução' para segundos
df['Tempo de Execução'] = df['Tempo de Execução'].apply(lambda x: int(x.split('m')[0])*60 + float(x.split('m')[1].replace('s','').replace(',', '.')))

plt.figure(figsize=(10,6))
plt.plot(df['N'], df['Tempo de Execução'], marker='o')
plt.title('Gráfico do Tempo de Execução')
plt.xlabel('N')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)

# Adicionando anotações para cada ponto
for i in range(len(df['N'])):
    plt.annotate(df['N'][i], (df['N'][i], df['Tempo de Execução'][i]))

plt.show()