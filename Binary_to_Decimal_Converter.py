# Binary to Decimal and Back Converter 
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def convert_num(num,convert_type):
    if convert_type.lower() == 'd':
        # the int() function is called with two arguments: the binary number represented as a string ('1010') and the base (2). 
        # This tells Python that the input number is in binary format, and it should convert it to its decimal equivalent.
        return int(num,2)
    elif convert_type.lower() == 'b':
        # In Python, the bin() function returns the binary representation of an integer prefixed with '0b' to indicate that it's a binary number.
        return bin(num)
    else:
        print('Incorrect type to convert')
try:
    num = int(input('Enter number: '))
except:
    print('Error - need to enter only digits.Try again')
else:
    convert_type = input('D - convert to decimal or B - convert to binary: ')
    result = convert_num(num,convert_type)
    print(f'result = {result}')


if __name__ == '__main__':
    main()
