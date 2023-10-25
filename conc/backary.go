package main

import (
	"fmt"
	"sync"
)

const N = 4 // número de goroutines

type Bakery struct {
	choosing [N]bool
	ticket   [N]int
}

func max(arr [N]int) int {
	m := 0
	for _, value := range arr {
		if value > m {
			m = value
		}
	}
	return m
}

func (b *Bakery) lock(id int) {
	b.choosing[id] = true
	b.ticket[id] = max(b.ticket) + 1
	b.choosing[id] = false

	for j := 0; j < N; j++ {
		for b.choosing[j] { // Espera se j está escolhendo
		}
		for b.ticket[j] != 0 && (b.ticket[j] < b.ticket[id] || (b.ticket[j] == b.ticket[id] && j < id)) {
		} // Espera se j tem um ticket menor ou tem o mesmo ticket mas um ID menor
	}
}

func (b *Bakery) unlock(id int) {
	b.ticket[id] = 0
}

func main() {
	bakery := &Bakery{}

	var wg sync.WaitGroup

	for i := 0; i < N; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			for k := 0; k < 1000; k++ {
				bakery.lock(id)
				// região crítica vazia
				bakery.unlock(id)
			}
		}(i)
	}

	wg.Wait()
	fmt.Println("Todas as goroutines completaram.")
}
