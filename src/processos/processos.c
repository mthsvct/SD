#include <unistd.h>
#include <stdio.h>

void main(){
    int x = 0;
    int p;

    p = fork();

    if(p == 0){
        while(0==0){
            x++;
            printf("\nSou o filho, x = %i", x);
            sleep(1);
        }
    } else {
        while(0==0){
            x++;
            printf("\nSou o pai, x = %i", x);
            sleep(1);
        }
    }
}