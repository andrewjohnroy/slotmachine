#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int retNum(){
    return rand() % 10;
}

int main(){
    srand(time(NULL));
    for (int i = 0; i < 3; i++){
        printf("%d%d%d\n",retNum(),retNum(),retNum());
    }
    return 0;
}
