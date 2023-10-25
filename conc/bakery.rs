use std::sync::{Arc, Mutex, Barrier};
use std::thread;

const N: usize = 1000;  // número de threads

struct Bakery {
    choosing: [bool; N],
    ticket: [usize; N],
}

impl Bakery {
    fn new() -> Self {
        Bakery {
            choosing: [false; N],
            ticket: [0; N],
        }
    }

    fn max(&self, arr: [usize; N]) -> usize {
        *arr.iter().max().unwrap()
    }

    fn lock(&mut self, id: usize) {
        self.choosing[id] = true;
        self.ticket[id] = self.max(self.ticket) + 1;
        self.choosing[id] = false;

        for j in 0..N {
            while self.choosing[j] {}  // Espera se j está escolhendo
            while self.ticket[j] != 0 && (self.ticket[j] < self.ticket[id] || (self.ticket[j] == self.ticket[id] && j < id)) {}
            // Espera se j tem um ticket menor ou tem o mesmo ticket mas um ID menor
        }
    }

    fn unlock(&mut self, id: usize) {
        self.ticket[id] = 0;
    }
}

fn main() {
    let bakery = Arc::new(Mutex::new(Bakery::new()));
    let barrier = Arc::new(Barrier::new(N));

    let handles: Vec<_> = (0..N).map(|i| {
        let bakery = Arc::clone(&bakery);
        let barrier = Arc::clone(&barrier);

        thread::spawn(move || {
            barrier.wait();  // Espera até que todas as threads estejam prontas
            for _ in 0..1000 {
                let mut bakery = bakery.lock().unwrap();
                bakery.lock(i);
                // região crítica vazia
                bakery.unlock(i);
            }
        })
    }).collect();

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Todas as threads completaram.");
}
