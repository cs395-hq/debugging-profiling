#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void leak_example() {
    int *ptr = (int *)malloc(sizeof(int) * 1000000); // Allocate memory
    // Forget to free the memory
}

int main() {
    printf("Starting program...");
    for (int i = 0; i < 10; i++) {

	printf("Iteration %d\n", i+1);
        leak_example();
	// system("free");
	sleep(1);
    }
    return 0;
}
