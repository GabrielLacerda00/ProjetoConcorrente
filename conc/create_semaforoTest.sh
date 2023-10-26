#!/bin/bash

# Cria o arquivo CSV e escreve o cabeçalho
echo "N;Tempo de Execução" > semaforo.csv

for ((N=2; N<=1024; N*=2)); do
    echo "Generating code with N=$N"
    
    # Gera o código Rust com N como parâmetro
    ./generate_semaforoCode.sh $N
    
    echo "Compiling Rust code "
    
    # Compila o programa Rust
    rustc -O semaforo.rs -o semaforo
    
    echo "Running with N=$N"
    
    # Executa o programa Rust e mede o tempo de execução
    duration=$( (time ./semaforo) 2>&1 | grep real | awk '{print $2}' )
    
    # Adiciona a linha ao arquivo CSV
    echo "$N;$duration" >> semaforo.csv
done