# Count Words in a String - Counts the number of individual words in a string. 
# For added complexity read these strings in from a text file and generate a summary.

import re

#function to clear string from non alphabetical symbols
def return_non_alphabetical(str):
    # Use regular expression to match only alphabetical characters
    alpfabetical = ''.join(re.findall(r'[a-zA-Z ]',str))
    return alpfabetical

#another way to clear string from non alphabetical symbols
def another_non_alphabetical(str):
    alphabetical_str = ''
    for char in str:
        if char.isalnum() or char == ' ':
            alphabetical_str += char
    return alphabetical_str
    
#function to sum words in a string
def count_words(str):
    word_list = str.split(' ')
    return len(word_list)

# ask user to enter a name of file , for example = WordsCount.txt
file_name = input("Enter name of your txt file in format name.txt: ")
f = open(file_name,'r')
text = f.read()

#call function to clear string from non alphabetical symbols
alphabetical_str = return_non_alphabetical(text)

#call function to sum words in the string
word_sum = count_words(alphabetical_str)

print(f'Number of words in file {file_name} = {word_sum}')

f.close()


if __name__ == '__main__':
    main()
