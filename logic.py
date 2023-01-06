import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def getPassword(nr_letters, nr_numbers, nr_symbols):
    passAlpha = random.choices(letters, k=nr_letters)
    passNumerics = random.choices(numbers, k=nr_numbers)
    passSymbols = random.choices(symbols, k=nr_symbols)

    return passAlpha + passNumerics + passSymbols


def ListTOString(geneated_pass):
    password = ''
    for x in geneated_pass:
        password += x
        continue
    return password