#Write a Python script that reads a text file, counts the number of words in it, and writes the count to a new file.

def count_words(file_path):
    f = open(file_path)
    f_text = f.read()
    lst=f_text.split()
    f.close()
    
    f_count = open('count_words.txt',mode='w')
    text_write = str(len(lst))
    f_count.write(text_write)
    f_count.close()

count_words('textFile.txt')

if __name__ == '__main__':
    main()
