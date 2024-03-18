# Credit Card Validator - Takes in a credit card number from a common credit card vendor 
# (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number 
# (look into how credit cards use a checksum).

def validate_credit_card(card):
    # empty list to put all numbers of card as int
    card_list = []
    
    #sum of all digits (doubled and not)
    sum_digits = 0
    
    #checksum
    checksum = 0
    
    # cread a list of int for each num in card number
    for char in card:
        card_list.append(int(char))
    
    # 1. Starting from the rightmost digit (excluding the check digit), double the value of every second digit. 
    # If doubling a digit results in a number greater than 9, subtract 9 from the result.
    for num in range (0,len(card_list),2):
        new_val = card_list[num]*2
        if new_val > 9:
            card_list[num]=new_val - 9
        else:
            card_list[num]=new_val
    
    # 2. Sum up all the digits obtained from the previous step 1, including the unaffected digits.
    sum_digits = sum(card_list)

    # 3.Calculate the checksum by finding the remainder when the sum from step 2 is divided by 10.
    checksum = sum_digits%10
    
    # If the remainder is 0, the checksum is 0. 
    if checksum == 0:
        #Compare the checksum obtained in step 3 with the check digit (the rightmost digit). 
        #If they match, the credit card number is valid; otherwise, it is invalid.
        if checksum == card_list[-1]:
            return True
        else:
            return False
    # Otherwise, subtract the remainder from 10 to obtain the checksum.
    else:
        checksum = 10 - checksum
        #Compare the checksum the check digit (the rightmost digit). 
        #If they match, the credit card number is valid; otherwise, it is invalid.
        if checksum == card_list[-1]:
            return True
        else:
            return False    

card = '4556737586899855' 
result = validate_credit_card(card)
print(result)


if __name__ == '__main__':
    main()
