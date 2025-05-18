#include <stdio.h>
#include <string.h>

void process_input(const char *input) {
    char buffer[32];
    size_t len = strlen(input);

    // Copy only up to buffer size - 1 to leave space for null terminator
    if (len >= sizeof(buffer)) {
        len = sizeof(buffer) - 1;
    }

    // Use memcpy or strncpy safely
    memcpy(buffer, input, len);
    buffer[len] = '\0';

    printf("Zpracovany vstup: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Pouziti: %s <vstup>\n", argv[0]);
        return 1;
    }

    process_input(argv[1]);
    return 0;
}