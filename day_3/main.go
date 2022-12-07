package main

import (
	"fmt"
	"os"
	"strings"
)

func getValuesMap() map[rune]int {
	result := map[rune]int{}
	// upper case are before lower case: 'A' < 'a' == true
	value := 1
	for l := 'a'; l <= 'z'; l++ {
		result[l] = value
		value++
	}
	for l := 'A'; l <= 'Z'; l++ {
		result[l] = value
		value++
	}
	return result
}

// Set type here.
type Set map[rune]bool

// New returns a new Set
func New() Set {
	return Set{}
}

// NewFromSlice returns a new Set from slice
func NewFromSlice(elems []rune) Set {
	set := New()
	for _, elem := range elems {
		set.Add(elem)
	}
	return set
}

// Add a new element to set
func (s Set) Add(elem rune) {
	s[elem] = true
}

// Has returns true if element belongs to Set
func (s Set) Has(elem rune) bool {
	return s[elem]
}

func (s Set) ToList() (list []rune) {
	for item, _ := range s {
		list = append(list, item)
	}
	return
}

// Intersection returns a Set with elements contained in s1 and s2
func Intersection(s1, s2 Set) Set {
	set := New()
	if len(s2) < len(s1) {
		s1, s2 = s2, s1
	}
	for elem := range s1 {
		if s2.Has(elem) {
			set.Add(elem)
		}
	}
	return set
}

func getPrioritiesSumPartOne(data []string) int {
	valuesMap := getValuesMap()
	prioritiesSum := 0
	for _, line := range data {
		middle := len(line) / 2
		compartmentA, compartmentB := line[:middle], line[middle:]
		setA := NewFromSlice([]rune(compartmentA))
		setB := NewFromSlice([]rune(compartmentB))
		commonItems := Intersection(setA, setB)
		letter := commonItems.ToList()[0]
		prioritiesSum += valuesMap[letter]
	}

	return prioritiesSum
}

func getPrioritiesSumPartTwo(data []string) int {
	const groupSize = 3
	valuesMap := getValuesMap()
	prioritiesSum := 0

	for offset := 0; offset <= len(data)-groupSize; offset += groupSize {
		group := data[offset : offset+groupSize]
		sackA, sackB, sackC := group[0], group[1], group[2]
		setA := NewFromSlice([]rune(sackA))
		setB := NewFromSlice([]rune(sackB))
		setC := NewFromSlice([]rune(sackC))
		commonItems := Intersection(Intersection(setA, setB), setC)
		if len(commonItems.ToList()) != 1 {
			panic("ouch")
		}
		letter := commonItems.ToList()[0]
		prioritiesSum += valuesMap[letter]
	}

	return prioritiesSum
}

func main() {
	data, _ := os.ReadFile("input.txt")
	lines := strings.Split(strings.TrimRight(string(data), "\n"), "\n")
	fmt.Println(getPrioritiesSumPartOne(lines))
	fmt.Println(getPrioritiesSumPartTwo(lines))
}
