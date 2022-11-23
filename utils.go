package main
import (
	"regexp"
	"strconv"
	"fmt"
	"bufio"
	"os"
	"log"
	"strings"
)

func convertStringToInt(str string) (int, error) {
	nonAlphanumericRegex := regexp.MustCompile(`[^a-zA-Z0-9 ]+`)
	num, err := strconv.Atoi(nonAlphanumericRegex.ReplaceAllString(str, ""))
	
	if err != nil{
		return -1, err
	}
	
	return num, nil
}

func convertStringToFloat(str string) (float64, error) {
	nonAlphanumericRegex := regexp.MustCompile(`[^a-zA-Z0-9. ]+`)
	num, err := strconv.ParseFloat(nonAlphanumericRegex.ReplaceAllString(str, ""), 64)
	
	if err != nil{
		return -1, err
	}
	
	return num, nil
}

func fileScanner(prompt string) *bufio.Scanner{
	reader := bufio.NewReader(os.Stdin)
	fmt.Println(prompt)

	path, _ := reader.ReadString('\n')
	path = path[:len(path)-2]
	pathContents, err := os.Open(path)

	if err != nil {
        log.Fatalf("%v", err)
    }

	return bufio.NewScanner(pathContents)
}

func parseLine(line string, inputNodes int, outputNodes int) (inputs []float64, outputs []int){
	var xs []float64
	var ys []int
	
	data := strings.Split(line, " ")
	if len(data) == inputNodes + outputNodes {
		for in := 0; in < inputNodes; in++ {
			weight, _ := convertStringToFloat(data[in])
			xs = append(xs, weight)
		}

		for out := 0; out < outputNodes; out++ {
			weight, _ := convertStringToInt(data[out])
			ys = append(ys, weight)
		}
	}

	return xs, ys
}