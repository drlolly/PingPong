from thread import  allocate_lock
import threading 

#ran in 30 seconds with count = 2 000 000. So about 66,000 round trip per second.
#Compared with  330,000 round trips per second for c (cf. PinPongInC
#comparied with go ping piong (exercise 9-5 of gopl) of 2.5mill per second.
#cf. labhaswork...ComparePingPong.xlsx 
lock = allocate_lock()
num_pings = 0
num_pongs = 0


def ping_f(a):
    global num_pings
    global semPing
    global semPong
    
    #for i in range(1,4):
    while num_pings < 20:
      semPing.acquire()
      num_pings += 1
      semPong.release() # increments the counter    
    return 

def pong_f(a):
    global num_pongs
    global semPing
    global semPong
    
    #for i in range(1,4):
    while num_pongs < 20:
      semPong.acquire()
      num_pongs += 1
      semPing.release() # increments the counter    
    return 

if __name__== "__main__":
    semPing = threading.Semaphore(0)
    semPong = threading.Semaphore(1)

    ping = threading.Thread(target=ping_f, args = (1,))
    ping.start()

    pong = threading.Thread(target=pong_f, args = (1,))
    pong.start()
    
    ping.join()
    pong.join()
    print ("num_pings  %d num_pongs %d " % (num_pings, num_pongs))
    #the program finishes with pong =1. It consumes all the ping releases except the last one.
    print ("semPing  %d semPong %d " % (semPing._Semaphore__value, semPong._Semaphore__value))
