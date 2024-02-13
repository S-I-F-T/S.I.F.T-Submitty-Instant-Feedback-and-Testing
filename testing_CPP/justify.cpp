/*  Created: 01/19/2023
    Program takes an input file of words, writes those word to an output file 
    with a certain width, and certain justification method. 
    The files, the width, and the flush methods are taken via commandline arguments.
*/
#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
using std::cout;

// Seperates a long word into multiple lines using hyphens
void long_word(const std::string &word, int width, std::ofstream &out_file, 
                    std::string &words_in_line) 
{
    // Store a version of the word that fits into the line
    std::string shorter_word = word.substr(0, width - 1);

    // Stores the left over word after shortening it
    std::string next_word = word.substr(shorter_word.length(), word.length() - 1);

    out_file << shorter_word << "- |" << std::endl;

    // Runs until all the words are shortened enough to fit into their own lines
    while (int(next_word.length()) > width)
    {
        out_file << "| ";

        // Shorten the next word so that it fit on the line
        shorter_word = next_word.substr(0, width - 1);

        // Left over word 
        next_word = next_word.substr(shorter_word.length(), width - 1);

        out_file << shorter_word << "- |" <<std::endl;

    }

    // Add the last shortened word to the line variable 
    // since more words might be able to fit on the line
    out_file << "| ";
    words_in_line = "";
    words_in_line += next_word + " ";
}

// Takes in width(address) provided, output and input file
// Prints to the output file the words from input file left justified
void left_just(const int &width, std::ifstream &in_file, 
                std::ofstream &out_file) 
{

    std::string word;
    std::string words_in_line = "";
    
    while (in_file >> word)
    {
        if (int(word.length()) > width)
        {
            
            // Words that are already stored in the line need to be written to the file 
            // if the next word is really long
            if (int(words_in_line.length()) > 0)
            {
                const std::string space(width - words_in_line.length(), ' ');
                out_file << words_in_line << space << " |" << std::endl;
                out_file << "| ";

                // Remove the words in the string and add the current word to it
                words_in_line = "";
                words_in_line += word + " ";
            }

            long_word(word, width, out_file, words_in_line);

        }

        else if  (int(words_in_line.length() + word.length()) > width)
        
        {
            
            const std::string space(width - words_in_line.length(), ' ');
            out_file << words_in_line << space << " |" << std::endl;
            out_file << "| ";

            // Remove the words in the string and add the current word to it
            words_in_line = "";
            words_in_line += word + " ";

        }
        
        else 
        {
            // If the next word makes the line equal to the given width
            // Do not add the space at the end else word will be place on new line
            if (int(words_in_line.length() + word.length()) == width)
                words_in_line += word; 

            else
                words_in_line += word + " ";
            
        }
    }
    
    // Since the last line does not get printed out in the loop
    // Do that here with proper spacing
    const std::string space2(width - words_in_line.length(), ' ');
    out_file << words_in_line << space2 << " |" << std::endl;

}

// Right justified version
void right_just(const int &width, std::ifstream &in_file, 
                std::ofstream &out_file) 
{

    std::string word;
    std::string words_in_line = "";
    
    while (in_file >> word)
    {

        if (int(word.length()) > width)
        {
            
            // Words that are already stored in the line need to be written to the file 
            // if the next word is really long
            if (int(words_in_line.length()) > 0)
            {
                // Number of extra spaces is equal to  
                // the length of the current line subtracted from the width
                const std::string space(width - words_in_line.length(), ' ');
                out_file << space << words_in_line << " |" << std::endl;
                out_file << "| ";

                // Remove the words in the string and add the current word to it
                words_in_line = "";
                words_in_line += " " + word; 
            }

            long_word(word, width, out_file, words_in_line);

        }
        
        // Print a new line if the next will make the line longer than the width
        else if (int(words_in_line.length() + word.length()) > width)
        
        {
            // Number of extra spaces is equal to  
            // the length of the current line subtracted from the width
            const std::string space(width - words_in_line.length(), ' ');
            out_file << space << words_in_line << " |" << std::endl;
            out_file << "| ";

            // Remove the words in the string and add the current word to it
            words_in_line = "";
            words_in_line += " " + word; 

        }
        
        else 
        {
            // If the next word makes the line equal to the given width
            // Do not add the space at the end because then word will be place on new line
            if (int(words_in_line.length() + word.length()) == width)
                words_in_line += word; 

            else
                words_in_line += " " + word; 
            
        }
    }
    
    // Since the last line does not get printed out in the loop
    // Do that here with proper spacing
    const std::string space2(width - words_in_line.length(), ' ');
    out_file << space2 << words_in_line << " |" << std::endl;

}

void full_just(const int &width, std::ifstream &in_file, std::ofstream &out_file) 
{   

    std::string word;
    std::string words_in_line = "";
    int x = 1;
    int i = 0;

    while (in_file >> word)
    {   
         
        // If the whole word is greater than the word itself, add hyphens to seperate each line
        if (int(word.length()) > width) 
        {
            // Sometimes there is a line in here that needs to be outputted left justified
            // Since the really long word can't fit on the line
            if (words_in_line.length() > 0) 
            {
                // Left justify the word if only one word in line
                    const std::string space(width - words_in_line.length(), ' ');
                    out_file <<  words_in_line << space << " |" << std::endl;
                    out_file << "| ";
                    words_in_line = "";
                    words_in_line += word + " "; 
            }
            long_word(word, width, out_file, words_in_line);

        }

        else if (int(words_in_line.length() + word.length()) > width)
        {   
            
            // Don't need the space at the end of the last word for full_just
            if (words_in_line[words_in_line.length() - 1] == ' ') 
            {
                words_in_line.pop_back();

                // .find returns std::string::npos if char is not found
                // https://stackoverflow.com/questions/43629363/how-to-check-if-a-string-contains-a-char
                if (words_in_line.find(' ') == 0)
                {
                    // Left justify the word if only one word in line
                    const std::string space(width - words_in_line.length(), ' ');
                    out_file <<  words_in_line << space << " |" << std::endl;
                    out_file << "| ";
                    words_in_line = "";
                    words_in_line += word + " ";  
                }

            }
            
            // Loop through each character in the line
            while (int(words_in_line.length()) < width)
            {   
                // If the char at this index is a space, add another one after it
                if (words_in_line[i] == ' ')
                {
                    words_in_line.insert(i + 1, " ");

                    // Since the next index will be the space we just added, 
                    // need to increment here so that it indexes the character after the space
                    i += x;
                    
                }

                // Set index back to the start when end is reached
                if (i >= int(words_in_line.length() - 1)) {
                    i = 0;
                    // Since we keep adding spaces, the increment value for i needs to keep going up
                    x++;
                }

                i++;
            }

            out_file << words_in_line << " |" << std::endl;
            out_file << "| ";
            
            // Remove the words in the string and add the current word to it
            words_in_line = "";
            words_in_line += word + " ";

            // Set i back to zero for the next line
            i = 0;
        }
        
        else 
        {
            // If the next word makes the line equal to the given width
            // Do not add the space at the end else word will be place on new line
            if (int(words_in_line.length() + word.length()) == width)
                words_in_line += word; 

            else
                words_in_line += word + " ";
            
        } 

    }

    // Since the last line does not get printed out in the loop
    // Do that here with proper spacing
    const std::string space2(width - words_in_line.length(), ' ');
    out_file << words_in_line << space2 << " |" << std::endl;
    
}

// Mainly for error checking and calling other functions
int main(int argc, char* argv[]) 
{

    // Print error message if 4 arguments were not provided
    // argc - 1 to disregard the compiled file as part of the arguments
    if (argc != 5)
    {
        std::cerr << "Program Requires 4 Arguments: " 
                    << argc - 1 << " Provided" << std::endl;
    }

    // Print error if input file was not succesfully opened
    std::ifstream in_file(argv[1]);
    if (!in_file.good()) 
    {

        std::cerr << "Cant open " << argv[1] << " to read" << std::endl;
        exit(1);
    }

    // Print error if output file was not succesfully opened
    std::ofstream out_file(argv[2]);
    if (!out_file.good()) 
    {

         std::cerr << "Cant open " << argv[2] << " to write" << std::endl;
         exit(2);

    }

    if (atoi(argv[3]) <= 1)
    {
        std::cerr << "Enter a width greater than 1" << std::endl;
        exit(3);
    }

    // Print error if invalid type is provided
    std::string just_type = argv[4];
    if ( (just_type != "flush_left") && (just_type != "flush_right") &&
            (just_type != "full_justify") )
    {
        std::cerr << "Invalid Justification Method" << std::endl;
        exit(4);
    }
    
    int width = atoi(argv[3]);
    // Print dashes equal to the width entered + 4
    const std::string dash(width + 4, '-');
    out_file << dash << std::endl;
    out_file << "| ";

    
    if (just_type == "full_justify")
    {
        full_just(width, in_file, out_file);
    }
    
    
    else if (just_type == "flush_left")
    {
        left_just(width, in_file, out_file);
    }
    
    else if (just_type == "flush_right")
    {
        right_just(width, in_file, out_file);
    }
    
    out_file << dash;
    
}

