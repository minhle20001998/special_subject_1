user_input = input("take input")


def mostFreq(string):
    array = list(string)
    count = 0
    mostFreqChar = array[0]
    for char in array:
        current_freq = array.count(char)
        if (current_freq > count):
            count = current_freq
            mostFreqChar = char
    return mostFreqChar


print(mostFreq(user_input))
