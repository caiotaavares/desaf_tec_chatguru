package main

import (
	"log"
	"net/http"
)

func main() {
	log.Print("simplehttp: Enter main()")
	http.HandleFunc("/healthz", StatusHandler)
	// http.HandleFunc("/info", InfoHandler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}

func StatusHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("alive"))
}