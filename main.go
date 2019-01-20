package main

import (
	"fmt"
	"time"

)

var pings = make(chan int) // send amount to deposit
var pongs = make(chan int) // receive balance

var countPing int
var countPong int


func sendPing() {

  for i := 0; i < 10000000 ; i++ {
    countPing += 1
    receiver1  :=  <- pongs
    pings <- (receiver1 + 1)
  }
  fmt.Printf("countPing %d  \n", countPing)
}


func main() {
  go sendPing()
  //start the process of ping/pongs
  pongs <- 1
  
  //Pong
  for i := 0; i < 10000000 - 1; i++ {
    countPong += 1
    receiver2 := <-pings
    pongs <- (receiver2 + 1)
  }
  // receive last ping
  <-pings
  fmt.Printf("countPong4 %d   \n", countPong)
  
  //give sendPIng time to finish up
  time.Sleep(100 * time.Millisecond)
}