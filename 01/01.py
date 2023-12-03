import string
import re

f = open('01/example.txt', 'r')

def partOne(f):
    calibrations = []
    for l in f.readlines():
        # Remove all letters + newlines
        onlyDigits = l.strip('\n' + string.ascii_letters)
        
        # First and last position now has the string's first and last digit
        calibrations.append(int(onlyDigits[0] + onlyDigits[len(onlyDigits) - 1]))

    return sum(calibrations)

print("Part one")
print(partOne(f))
print("========")

f = open('01/input.txt', 'r')

def partTwo(f):
    calibrations = []
    digitTranslations = {
        'twone': '21',
        'eightwo': '82',
        'oneight': '18',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    numbersPattern = '(' + '|'.join(digitTranslations.keys()) + ')'
    for l in f.readlines():
        # Remove all letters + newlines
        replacedNumbers = re.sub(numbersPattern, lambda match: digitTranslations[match.group()], l)
        onlyDigits = replacedNumbers.strip('\n' + string.ascii_letters)
        # First and last position now has the string's first and last digit
        calibrations.append(int(onlyDigits[0] + onlyDigits[len(onlyDigits) - 1]))
    return sum(calibrations)

print("Part two")
print(partTwo(f))