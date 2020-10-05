correctFile = open("correctAnswers.txt", "r")
userFile = open("userAnswers.txt", "r")


def readCorrectFile(correctFile):
    correctAnswers = []
    for c in correctFile.read():
        if (c.isalpha()):
            correctAnswers.append(c)
    return correctAnswers


def readUserFile(userFile):
    userAnswers = []
    for c in userFile.read():
        if (c.isalpha()):
            userAnswers.append(c)
    return userAnswers


def checkAnswers(correctAnswers, userAnswers):
    correct_count = 0
    wrong_count = 0
    wrong_list = []
    for i in range(len(correctAnswers)):
        questionNum = i + 1;
        if (correctAnswers[i] == userAnswers[i]):
            correct_count += 1
        elif (not correctAnswers[i] == userAnswers[i]):
            wrong_count += 1
            wrong_list.append(questionNum)
    print(
        'number of correct answers: {}\nnumber of wrong answers: {}\nquestion numbers of the incorrect answers: {}'.format(
            correct_count, wrong_count, wrong_list))


checkAnswers(readCorrectFile(correctFile), readUserFile(userFile))
