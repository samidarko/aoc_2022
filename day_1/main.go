package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, _ := os.ReadFile("input.txt")

	elves := strings.Split(string(data), "\n\n")

	maxLoad := 0
	elvesLoad := make([]int, 0)

	for _, elf := range elves {
		sumLoad := 0
		for _, value := range strings.Split(elf, "\n") {
			load, _ := strconv.Atoi(value)
			sumLoad += load
		}
		maxLoad = max(sumLoad, maxLoad)
		elvesLoad = append(elvesLoad, sumLoad)

	}

	fmt.Println(maxLoad)

	sort.Slice(elvesLoad, func(a, b int) bool { return elvesLoad[a] > elvesLoad[b] })

	topMaxLoad := 0
	for _, load := range elvesLoad[:3] {
		topMaxLoad += load
	}
	fmt.Println(topMaxLoad)
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
