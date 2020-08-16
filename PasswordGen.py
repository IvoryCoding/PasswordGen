import random

def getChracter(characterNumber):
    if characterNumber == 1:
        return 'a'
    elif characterNumber == 2:
        return 'A'
    elif characterNumber == 3:
        return 'b'
    elif characterNumber == 4:
        return 'B'
    elif characterNumber == 5:
        return 'c'
    elif characterNumber == 6:
        return 'C'
    elif characterNumber == 7:
        return 'd'
    elif characterNumber == 8:
        return 'D'
    elif characterNumber == 9:
        return 'e'
    elif characterNumber == 10:
        return 'E'
    elif characterNumber == 11:
        return 'f'
    elif characterNumber == 12:
        return 'F'
    elif characterNumber == 13:
        return 'g'
    elif characterNumber == 14:
        return 'G'
    elif characterNumber == 15:
        return 'h'
    elif characterNumber == 16:
        return 'H'
    elif characterNumber == 17:
        return 'i'
    elif characterNumber == 18:
        return 'I'
    elif characterNumber == 19:
        return 'j'
    elif characterNumber == 20:
        return 'J'
    elif characterNumber == 21:
        return 'k'
    elif characterNumber == 22:
        return 'K'
    elif characterNumber == 23:
        return 'l'
    elif characterNumber == 24:
        return 'L'
    elif characterNumber == 25:
        return 'm'
    elif characterNumber == 26:
        return 'M'
    elif characterNumber == 27:
        return 'n'
    elif characterNumber == 28:
        return 'N'
    elif characterNumber == 29:
        return 'o'
    elif characterNumber == 30:
        return 'O'
    elif characterNumber == 31:
        return 'p'
    elif characterNumber == 32:
        return 'P'
    elif characterNumber == 33:
        return 'q'
    elif characterNumber == 34:
        return 'Q'
    elif characterNumber == 35:
        return 'r'
    elif characterNumber == 36:
        return 'R'
    elif characterNumber == 37:
        return 's'
    elif characterNumber == 38:
        return 'S'
    elif characterNumber == 39:
        return 't'
    elif characterNumber == 40:
        return 'T'
    elif characterNumber == 41:
        return 'u'
    elif characterNumber == 42:
        return 'U'
    elif characterNumber == 43:
        return 'v'
    elif characterNumber == 44:
        return 'V'
    elif characterNumber == 45:
        return 'w'
    elif characterNumber == 46:
        return 'W'
    elif characterNumber == 47:
        return 'x'
    elif characterNumber == 48:
        return 'X'
    elif characterNumber == 49:
        return 'y'
    elif characterNumber == 50:
        return 'Y'
    elif characterNumber == 51:
        return 'z'
    elif characterNumber == 52:
        return 'Z'
    elif characterNumber == 53:
        return '1'
    elif characterNumber == 54:
        return '2'
    elif characterNumber == 55:
        return '3'
    elif characterNumber == 56:
        return '4'
    elif characterNumber == 57:
        return '5'
    elif characterNumber == 58:
        return '6'
    elif characterNumber == 59:
        return '7'
    elif characterNumber == 60:
        return '8'
    elif characterNumber == 61:
        return '9'
    elif characterNumber == 62:
        return '0'
    elif characterNumber == 63:
        return '!'
    elif characterNumber == 64:
        return '@'
    elif characterNumber == 65:
        return '#'
    elif characterNumber == 66:
        return '$'
    elif characterNumber == 67:
        return '%'
    elif characterNumber == 68:
        return '^'
    elif characterNumber == 69:
        return '&'
    elif characterNumber == 70:
        return '*'

print('How many password(s) do you want? ')
number = input()
number = int(number)

passwordLength = random.randint(8, 12)
generatedPasswords = []

while len(generatedPasswords) < number:
    generatedPasswords.append("")

if number > 0:
    print(str(number) + ' password(s) being generated. Please wait...')
    while number > 0:

        while len(generatedPasswords[number - 1]) < passwordLength:
            r = random.randint(1, 70)
            generatedPasswords[number - 1] += getChracter(r)

        print('Password #' + str(number) + ':')
        print(generatedPasswords[number - 1])
        number -= 1