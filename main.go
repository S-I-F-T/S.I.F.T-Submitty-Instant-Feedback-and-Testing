package main
import "fmt"
import "unicode/utf8"

/* Algo to check if number is prime in O(n) */
func is_prime(x int) bool {
	var d int = x / 2
	for i := 1; i <= d; i++ {
		if (x % i == 0) {
			return false
		}
	}
	return true 
}

func output_primality(prime_test1 int) {
	if is_prime(prime_test1) == true {
		fmt.Print(prime_test1)
		fmt.Print(" is prime!\n")
	} else {
		fmt.Print(prime_test1)
		fmt.Print(" is not prime!\n")
	}
}

func main() {
	/* Everything used in go
	must actullay be used
	otherwise wee have comp error */

	fmt.Println("Hello World!")
	var intNum int = 4
	fmt.Println(intNum)

	var myString string = "My Name Is Steven"

	// Prints string obv
	fmt.Println(myString)

	// Should be 17
	fmt.Println(len(myString))

	// Should be 2
	fmt.Println(len("γ"))

	/* should be one, mostly for fancy
	strings with weird chars. below for
	ex is gamma. */
	fmt.Println(utf8.RuneCountInString("γ"))

	var prime_test1 int = 113
	var prime_test2 int = 91

	// 113 is prime!
	output_primality(prime_test1)

	// 91 is not prime!
	output_primality(prime_test2)
}