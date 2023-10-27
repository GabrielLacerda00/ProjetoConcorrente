# ProjetoConcorrente
Alunos: Carlos ALberto Pamplona Filho / Gabriel Rodrigues Oliveira Lacerda

# Metodologia
O objetivo deste trabalho, referente à disciplina de programação concorrente do período de 2023-1, consiste em entender a execução de programas de maneira concorrente na linguagem RUST, e, a partir disso, avaliar a diferença de performance entre algoritmo de backary e o uso de semáforos como estratégias de implementação das travas, em problemas com diferentes tamanhos de entrada.
Para avaliar o desempenho, a partir de também diferentes números de threads. A partir disso, analisamos os tempos de execução do código, monitorando sua performance.

# Análise dos resultados

## Bakery para macOS M2
- Processador CPU de 8 núcleos (4 de desempenho e 4 de eficiência)
- 8 gb RAM
- 512 gb dísco (ssd)

Tempo de execução com 2 threads: 0m0.139s

Tempo de execução com 4 threads: 0m0.133s

tempo de execução com 8 threads: 0m0.134s

Tempo de execução com 16 threads: 0m0.127s

Tempo de execução com 32 threads: 0m0.132s

Tempo de execução com 64 threads: 0m0.143s

Tempo de execução com 128 threads: 0m0.209s

Tempo de execução com 256 threads: 0m0.373s

Tempo de execução com 512 threads: 0m1.369s

Tempo de execução com 1024 threads: 0m3.999s

## Para Intel© Core™ i5-10300H CPU @ 2.50GHz
- Processador com quatro núcleos físicos e 8 núcleos lógicos.
- 16 GB de memória RAM 
- 768.2 GB de disco (ssd)

### Para Bakery

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

### Para Semáforo

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



# Conclusão
