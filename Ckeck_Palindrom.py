# Check if Palindrome - Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar”

def check_palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
word = input("Enter word: ")
result = check_palindrom(word)
if result:
    print("It is a palindrom")
else:
    print("It is not a palindrom")

if __name__ == '__main__':
    main()
