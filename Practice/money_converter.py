NUMBERS = {
    "1": "mot",
    "2": "hai",
    "3": "ba",
    "4": "bon",
    "5": "nam",
    "6": "sau",
    "7": "bay",
    "8": "tam",
    "9": "chin",
    "10": "muoi"
}

UNITS = ["ty", "trieu", "ngan", "tram"]


# chuyen number thanh dang co dau phay, vd: 1000000 -> 1,000,000
def commas(number):
    number_with_commas = "{:,}".format(number)
    return number_with_commas


# chuyen tien thanh dang chu
def convert(number):
    unit = commas(number).split(",")
    text = ""
    for i in range(len(unit)):
        currentNumber = unit[i]
        currentUnit = UNITS[(4 - len(unit)) + i]

        # truong hop unit dau tien co 1 chu so , vd: 1,000,000
        if (i == 0 and len(currentNumber) == 1):
            text += NUMBERS[currentNumber[0]] + " "
            if not (currentUnit == "tram"):
                text += currentUnit + " "

        # truong hop unit dau tien co 2 chu so, vd: 20,000,000:
        if (i == 0 and len(currentNumber) == 2):
            if (currentNumber[0] == "1"):  # vd 10-> muoi ; 20-> hai muoi
                text += NUMBERS["10"] + " "
            else:
                text += NUMBERS[currentNumber[0]] + " " + NUMBERS["10"] + " "

            if (currentNumber[1] == "0"):  # vd 10->muoi
                text += ""
            elif (currentNumber[1] == "5"):
                text += "lam "
            else:  # vd 21->hai muoi mot
                text += NUMBERS[currentNumber[1]] + " "

            if not (currentUnit == "tram"):
                text += currentUnit + " "
            else:
                text += ""

        # truong hop chia het cho 100
        if (int(currentNumber) % 100 == 0 and not int(currentNumber) == 0):
            text += NUMBERS[currentNumber[0]] + " tram "
            if not (currentUnit == "tram"):
                text += currentUnit + " "
            else:
                text += " "

        # cac truong hop bi`nh thuo`ng
        if (not int(currentNumber) % 100 == 0 and len(currentNumber) == 3
                and len(unit) >= 1):
            # xet hang tram:
            if (currentNumber[0] == "0" and not currentUnit == "tram"):
                text += ""
            elif (not currentNumber[0] == "0"):
                text += NUMBERS[currentNumber[0]] + " tram "
                # xet hang tram cua hang tram :)
            elif (currentNumber[0] == "0" and not currentNumber[1] == "0" and currentUnit == "tram" and (
                    not (int(unit[-2][-1]) == 0)) or not (int(unit[-2][-2]) == 0)):
                if (len(unit) >= 3):
                    text += "khong tram "

            # xet hang chuc:
            if (currentNumber[1] == "0"):
                text += "le "
            else:
                if (currentNumber[1] == "1"):
                    text += NUMBERS["10"] + " "
                else:
                    text += NUMBERS[currentNumber[1]] + " " + NUMBERS["10"] + " "

            # xet hang don vi:
            if (currentNumber[2] == "0"):
                text += ""
            else:
                text += NUMBERS[currentNumber[2]] + " "

            # neu la hang don vi thi khong duoc them currentUnit:
            if not (currentUnit == "tram"):
                text += currentUnit + " "
    return text


user_input = int(input("nhap so tien\n"))
print(convert(user_input))
