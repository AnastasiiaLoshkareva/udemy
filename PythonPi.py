# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math

# function to count pi
def pi_count(num):
    if num <15:
        pi_value = round(math.pi,num)
        return pi_value
    else:
        print('number should be less then 15')

# Wrapper function
def main():  
  num = int(input('Enter the number of decimals to calculate to: '))
  result = pi_count(num)
  print(result)

if __name__ == '__main__':
    main()
