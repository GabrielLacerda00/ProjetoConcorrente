import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo csv
df = pd.read_csv('results.csv', delimiter=';', decimal=',')

# Converter a coluna 'Tempo de Execução' para segundos
df['Tempo de Execução'] = df['Tempo de Execução'].apply(lambda x: int(x.split('m')[1].split(',')[0])/60 + int(x.split('m')[1].split(',')[1].replace('s','')))

# Gerar o gráfico
plt.figure(figsize=(10,6))
plt.plot(df['N'], df['Tempo de Execução'], marker='o')
plt.title('Gráfico do Tempo de Execução')
plt.xlabel('N')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)
plt.show()
