

main:  main.c
	gcc -Wall -g main.c -o main -lpthread -lrt 
	
	
clean:
	rm -f main.o
	rm -f main
