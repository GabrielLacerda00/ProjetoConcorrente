# ProjetoConcorrente
Alunos: Carlos ALberto Pamplona Filho / Gabriel Rodrigues Oliveira Lacerda

# Metodologia
O objetivo deste trabalho, referente à disciplina de programação concorrente do período de 2023-1, consiste em entender a execução de programas de maneira concorrente na linguagem RUST, e, a partir disso, avaliar a diferença de performance entre algoritmo de backary e o uso de semáforos como estratégias de implementação das travas, em problemas com diferentes tamanhos de entrada.
Para avaliar o desempenho, a partir de também diferentes números de threads. A partir disso, analisamos os tempos de execução do código, monitorando sua performance.

# Análise dos resultados

## Para macOS M2
- Processador CPU de 8 núcleos (4 de desempenho e 4 de eficiência)
- 8 gb RAM
- 512 gb dísco (ssd)

### Bakery
| Número de Threads | Tempo de execução |
| -- | -- |
| 2 |   0m0.139s  |
| 4 |   0m0.133s  |
| 6 |   0m0.134s  |
| 16|   0m0.127s  |
| 32|   0m0.132s  |
| 64|   0m0.143s  |
|128|   0m0.209s  |
|256|   0m0.373s  |
|512|   0m1.369s  |
|1024|  0m3.999s  |

### Semáforo



## Para Intel© Core™ i5-10300H CPU @ 2.50GHz
- Processador com quatro núcleos físicos e 8 núcleos lógicos.
- 16 GB de memória RAM 
- 768.2 GB de disco (ssd)

### Bakery

| Número de Threads | Tempo de execução |
| -- | -- |
| 2 | 0m0,001s |
| 4 | 0m0,001s |
| 8 | 0m0,002s |
| 16| 0m0,003s |
| 32|0m0,007s  |
| 64|0m0,019s  |
|128|0m0,054s  |
|256|0m0,104s  |
|512|0m0,346s  |
|1024|0m1,302s |

### Semáforo

| Número de Threads | Tempo de execução |
| -- | -- |
| 2 | 0m0,001s |
| 4 | 0m0,001s |
| 8 | 0m0,002s |
| 16| 0m0,003s |
| 32|0m0,007s  |
| 64|0m0,020s  |
|128|0m0,056s  |
|256|0m0,100s  |
|512|0m0,352s  |
|1024|0m1,316s |

| Gráfico de comparação entre resultados |
|--|
|![grafico](./conc/assets/i5-bakery-vs-semaforo.png)

# Conclusão
