#!/bin/bash

# Cria o arquivo CSV e escreve o cabeçalho
echo "N;Tempo de Execução" > bakery.csv

for ((N=2; N<=2048; N*=2)); do
    echo "Running with N=$N"
    
    # Executa o programa Go e mede o tempo de execução
    duration=$( (time go run bakery.go -N $N) 2>&1 | grep real | awk '{print $2}' )

    # Adiciona a linha ao arquivo CSV
    echo "$N;$duration" >> bakery.csv
done
