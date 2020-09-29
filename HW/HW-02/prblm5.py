from itertools import count


def isVowel(char):
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True
    else:
        return False


def vowelsCount(string):
    count = 0
    for i in range(len(string)):
        if (isVowel(string[i])):
            count += 1
    return count


def consonantsCount(string):
    count = 0
    for i in range(len(string)):
        if (not isVowel(string[i]) and string[i] != ' ' and string[i].isalpha()):
            count += 1
    return count


user_input = input("take input")
print(vowelsCount(user_input))
print(consonantsCount(user_input))
