// Go's linker flags?
package main

import (
	"log"
	"net/http"
	"os"
)

var Version = "1.0.0"
var db = os.Getenv("DB")

func main() {

	log.Print("simplehttp")
	http.HandleFunc("/healthz", StatusHandler)
	http.HandleFunc("/info", InfoHandler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}

func StatusHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("alive"))
}

func InfoHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	response := map[string]string{
		"version": Version,
		"db":      db,
	}
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"version":"` + response["version"] + `", "db":"` + response["db"] + `"}`))
}