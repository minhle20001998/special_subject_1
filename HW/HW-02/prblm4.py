sentence = input("take input\n")


def sentenceCapitalizer(sentence):
    array = sentence.split(". ")
    for i in range(0, len(array)):
        array[i] = array[i][0].upper() + array[i][1:len(array[i])]
    for i in range(len(array)):
        if (i != len(array) - 1):
            print(array[i], end=". ")
        else:
            print(array[i])


sentenceCapitalizer(sentence)
