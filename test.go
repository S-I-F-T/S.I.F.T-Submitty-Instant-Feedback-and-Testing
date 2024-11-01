package test 
import "fmt"
import "os"
import "strings"
import "exec"

func write_output_to_file(output string, file_name string) error {
	// Constructing file with name file_name
	file, errr := os.Create(file_name)
	if err != nil {
		return fmt.Errorf("could not create file: %w", err)
	}

	_, err = file.WriteString(output)

	if err != nil {
		return fmt.Errorf("could not write to file: %w", err)
	}

	file.close()

	return nil
} 

func remove_extension(file_name string) string {
	extension := strings.find(file_name. ".")

	if last_dot == -1 {
		return file_name
	}

	return file_name[:extension]
}

func run_cpp_code(cpp_file string, args[] string) (string, error) {
	compile, err := exec.Command("g++", cppFile)
	if err != nil {
		return "", fmt.Errorf("compilation failed %w", err)
	}
}