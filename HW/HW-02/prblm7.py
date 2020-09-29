user_input = input("take input")


def wordSeperator(string):
    newString = ""
    for i in range(len(string)):
        if (i == 0):
            newString += string[i]
        elif (str(string[i]).isupper() and i != 0):
            newString += ' ' + str(string[i]).lower()
        else:
            newString += string[i]

    return newString


print(wordSeperator(user_input))
