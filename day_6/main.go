package main

import (
	"fmt"
	"os"
	"strings"
)

const (
	PacketMarkerSize  = 4
	MessageMarkerSize = 14
)

type Set map[rune]bool

func newSet(input string) Set {
	set := make(Set)

	for _, r := range input {
		set[r] = true
	}

	return set
}

func getFirstStart(buffer string, markerSize int) int {
	for offset := 0; offset < len(buffer)-markerSize; offset++ {
		limit := offset + markerSize
		set := newSet(buffer[offset:limit])
		if len(set) == markerSize {
			return limit
		}

	}
	return 0
}

func main() {
	data, _ := os.ReadFile("input.txt")
	buffer := strings.TrimRight(string(data), "\n")
	fmt.Println(getFirstStart(buffer, PacketMarkerSize))
	fmt.Println(getFirstStart(buffer, MessageMarkerSize))
}
