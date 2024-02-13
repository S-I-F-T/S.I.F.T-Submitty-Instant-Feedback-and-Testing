#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iterator>

using namespace std;

/* This program takes in four command line arguments (an input file, output
   file, box length, and text justification option) and prints out a box
   with the contents of the given input file inside of it, at the given box
   length. The user is able to select whether they want the text from the 
   input file is left justified, right justified, or full justified within
   the box. */

/* Function that takes in a vector of individual words from the file,
   the user's desired box length, and the justification option, and
   prints out a box with the words inside, with the correct
   justification */
void print_box(vector<string> words, unsigned int box_len, string option, string out_file){
    
    // Vector which holds each line to be printed in the box
    vector<string> lines;

    // 2D vector to hold all the individual words in each line
    vector<vector<string>> words_in_line;

    // Vector which holds the number of words in each line
    vector<int> line_num_words;

    // Opening output file to write to
    ofstream output(out_file);
    if (!output){
        cerr << "File not found" << endl;
    }


    /* Loop that goes through every word from the file and then constructs
       a string that can fit on one line using the box length. It then
       adds this string to a vector called lines, which will be called
       later to print out each line in the box */
    for (unsigned int i = 0; i < words.size(); i++){
        string curr_line = words[i];
        vector<string> curr_words;
        curr_words.push_back(words[i]);
        unsigned int line_len = curr_line.length();
        int line_words = 1;

        /* This loop runs while the length of the current line that has been
           formed is less that the box length. If this is the case, it will
           check if the length of the line is still less than the box length
           if the next word is added. If it is, it will add the word to the
           line, otherwise, it will break out of the loop and add the line
           as it is to the lines vector (the lines vector is only used for
           left and right justified, full justified has a different line
           generation process)*/ 
        while (line_len < box_len){
            if ((i+1 < words.size()) && ((line_len + words[i+1].length() + 1) <= box_len)){
                curr_line = curr_line + " " + words[i+1];
                curr_words.push_back(words[i+1]);
                line_words++;
                line_len = curr_line.length();
                i++;
            }
            else{
                break;
            }
        }

        /* Adding the current word to the words_in_line vector, the 
           number of words in the line to the line_num_words vector
           and the final line to the lines vector */
        words_in_line.push_back(curr_words);
        line_num_words.push_back(line_words);
        lines.push_back(curr_line);


    }

    // Prints out top line of box
    for (unsigned int i = 0; i < box_len + 4; i++){
        output << "-";
    }
    output << endl;

    // Prints out the lines with left justification
    if (option == "flush_left"){
        for (string line : lines){
            output << "| " << line;
            for (unsigned int i = 0; i < ((box_len + 1) - line.length()); i++){
                output << " ";
            }
            output << "|" << endl;
        }
    }

    // Prints out the lines with right justification
    else if (option == "flush_right"){
        for (string line : lines){
            output << "|";
            for (unsigned int i = 0; i < ((box_len + 1) - line.length()); i++){
                output << " ";
            }
            output << line << " |" << endl;
        }
    }

    // Prints out the lines with full justification
    else if (option == "full_justify"){

        // Vector to hold each line of words that is full justified
        vector<string> full_lines;
        
        /* Variables to keep track of the number of spaces to add in
           between each word */
        unsigned int default_space = 0;
        unsigned int remaining_space = 0;

        /* Variables to keep track of the index and if the following loop was 
           broken */
        unsigned int index = 0;
        bool broken = false;

        // For loop that goes through each vector of words per line
        for (vector<string> words_in_full_line : words_in_line){
            
            /* Setting the broken variable to true if the index variable is equal
               to the length of a word and breaking out of the loop */
            if (index == (words_in_line.size() - 1)){
                broken = true;
                break;
            }
            index++;
            int line_len = 0;

            // Adds the lengths of the words to the line to keep track of its length
            for (string word : words_in_full_line){
                line_len += word.length();
            }

            /* Setting the spaces to 0 if there is only one word in a line
               effectively left justifying it */
            if (words_in_full_line.size() == 1){
                default_space = 0;
                remaining_space = 0;
            }

            /* Otherwise, the default space and remaining space variables are set to
               the necessary amounts based on the box length, line length, and
               how many words are in the line */
            else{
                default_space = (box_len - line_len) / (words_in_full_line.size() - 1);
                remaining_space = (box_len - line_len) % (words_in_full_line.size() - 1);
            }

            /* Goes through each word in the line and adds the words to a string. 
               It will put the default number of spaces in between each word, 
               and adds the remaining spaces one by one to the left-most word, 
               then the one to the right, and so on until all the remaining spaces
                are used up */
            string curr_line;
            for (unsigned int i = 0; i < (words_in_full_line.size() - 1); i++){
                curr_line += words_in_full_line[i];
                unsigned int num_spaces = default_space;
                if (i < remaining_space){
                    num_spaces++;
                }
                for (unsigned int j = 0; j < num_spaces; j++){
                    curr_line += " ";
                }
            }
            
            /* Adding the final word to the line after the main loop has finished 
               and then adding it to the full_lines vector so it can be printed 
               later */
            curr_line += words_in_full_line[words_in_full_line.size() - 1];
            full_lines.push_back(curr_line);
        }

        /* Adding the final line to the full lines vector if the variable "broken"
           is true */
        if (broken){
            full_lines.push_back(lines[lines.size() - 1]);
        }

        // Printing 
        for (string line : full_lines){
            output << "| " << line;
            for (unsigned int i = 0; i < ((box_len + 1) - line.length()); i++){
                output << " ";
            }
            output << "|" << endl;
        }        
    }

    // Printing out error if invalid justification option is given
    else{
        cerr << "Enter a valid justification option" << endl;
    }

    // Prints out bottom line of box
    for (unsigned int i = 0; i < box_len + 4; i++){
        output << "-";
    }
    output << endl;

    // Closing the output file after we're done using it
    output.close();
}

// Main function of program, taking in comand line arguments
int main(int argc, char* argv[]){
    
    // Checking if all 4 command line arguments have been filled
    if (argc != 5){
        cerr << "Not all arguments filled" << endl;
        return 0;
    }
    
    // Setting the inputs for command line arguments to variables
    string in_file = argv[1];
    string out_file = argv[2];
    int box_len = atoi(argv[3]);
    string option = argv[4];

    // Throwing error if given box length is an invalid number
    if (box_len <= 1){
        cerr << "Box length too small, choose a larger length" << endl;
        return 0;
    }

    // Opening input file and throwing error if file isn't found
    ifstream file_data(in_file);
    if (!file_data){
        cerr << "Input file not found" << endl;
        return 0;
    }

    // Vector to hold all the individual words from the file
    vector<string> file_words;
    
    /* Vector to hold all individual words, as well as split up words if 
       they are longer than the given box length, which will be passed
       to the print_box function */
    vector<string> final_words;

    /* Reading in the data from the file and splitting it on all whitespace
       characters and then putting the individual words into the file_words
       vector */
    ifstream file(in_file);
    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string word;
        while (ss >> word) {
            file_words.push_back(word);
        }
    }

    /* Going through every word in the vector of individual words and 
       checking if a word is longer than the box length. If it isn't
       the word is simply added to the final_words vector. If it is,
       the word will be cut off at the letter that is equal to the box
       length, have that letter replaced with a hyphen, and have the 
       rest of the word put into the final words vector on its own. If
       the remaining part of the word is still longer, the process will
       repeat until the remaining parts are shorter than the box length*/
    for (string word : file_words){
        if (word.size() <= box_len){
            final_words.push_back(word);
        }
        else{
            int split_len = box_len - 1;
            string curr_split;
            for (unsigned int i = 0; i < word.size(); i++){
                if (curr_split.size() == split_len){
                    final_words.push_back(curr_split + "-");
                    curr_split = "";
                }
                curr_split.push_back(word[i]);
            }
            if (curr_split.size()){
                final_words.push_back(curr_split);
            }
        }
    }

    // Calling the print box function
    print_box(final_words, box_len, option, out_file);

    return 0;

}

