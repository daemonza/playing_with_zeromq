package main

import (
	"fmt"
	"log"

	"github.com/zeromq/goczmq"
)

func main() {

	server := "tcp://127.0.0.1:9988"
	prefix := "worker2"
	socket, err := goczmq.NewSub(server, prefix)
	if err != nil {
		log.Fatal(err.Error())
	}

	for {
		message, err := socket.RecvMessage()
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println(string(message[0]))
	}

}
