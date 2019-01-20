#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>
#define LOOPCOUNT 10000000
//RAN in 30 seconds.
//So 330,000 round trips per second, comparied with go ping piong (exercise 9-5 of gopl) of 2.5mill per second.
//So go about 10 times faster. 
sem_t pingsem, pongsem;


void * ping(void *arg) 
{
  int i; 
    for (i = 0 ; i < LOOPCOUNT;i++) {
        sem_wait(&pingsem);
        //printf("ping\n");
        sem_post(&pongsem);
    }
}


void * pong(void *arg) 
{
    int i; 
    for (i = 0 ; i < LOOPCOUNT;i++) {
        sem_wait(&pongsem);
        //printf("pong\n");
        sem_post(&pingsem);
    }
}

int main(void) 
{
    sem_init(&pingsem, 0, 0);
    sem_init(&pongsem, 0, 1);
    pthread_t ping_thread, pong_thread; 
    pthread_create(&ping_thread, NULL, ping, NULL);
    pthread_create(&pong_thread, NULL, pong, NULL);
    pthread_join(ping_thread, NULL);
    pthread_join(pong_thread, NULL);
    printf("finished 3\n");
    return 0;
}

