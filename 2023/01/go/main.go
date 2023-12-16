package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const fromLeft bool = true
const fromRight bool = false

func main() {
	file, err := os.ReadFile("./input")
	if err != nil {
		log.Fatalf("error reading file: %v\n", err)
	}

	inputContent := string(file[:])
	eachLineOfInput := strings.Split(inputContent, "\n")

	sum := 0
	for _, line := range eachLineOfInput {
		lineSum := ""
		for _, direction := range []bool{fromLeft, fromRight} {
			found := parseDigits(direction, &line)
			if found != "" {
				lineSum += found
			}
		}
		tmp, err := strconv.Atoi(lineSum)
		if err != nil {
			log.Fatalf("failure to convert %v to int\n", lineSum)
		}
		sum += tmp
	}

	fmt.Printf("The total sum is: %v\n", sum)

}

// jank
func parseDigits(startFromLeft bool, orig *string) string {
	s := *orig
	if startFromLeft {
		for idx := 0; idx < len(s); idx++ {
			c, err := strconv.Atoi(string(s[idx]))
			if err != nil {
				continue
			}
			return fmt.Sprint(c)
		}
	} else {
		for idx := len(s) - 1; idx >= 0; idx-- {
			c, err := strconv.Atoi(string(s[idx]))
			if err != nil {
				continue
			}
			return fmt.Sprint(c)
		}
	}
	return ""
}
