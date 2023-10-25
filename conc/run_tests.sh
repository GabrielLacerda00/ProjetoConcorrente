#!/bin/bash

# Aceita N como um argumento de linha de comando
N=$1

echo "Running with N=$N"

# Executa o programa Go
go run bakery.go -N $N

