def roman_to_integer():
    '''A Function to convert Romanumerals to Integers'''

    #Romanumeral Key
    roman_symbols = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    roman = input('') #Desired Input
    
    x = 0
    last_digit = roman[-1] #Remembers Last Romanumeral Digit

    #Reverses Romanumerals
    for i in roman[::-1]:
        roman_integer = roman_symbols[i] #Assigns the int of the Roman
        if roman_symbols[last_digit] > roman_integer: #Checks if subtraction is needed
            x -= roman_integer
            continue
        last_digit = i
        x += roman_integer #Adds single Roman Integer to Total
    print(x)

roman_to_integer()
