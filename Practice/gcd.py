# a.x = b mod m , find x


list_quotients = []
list_diviends = []
list_divisors = []
steps = 0


def gcdFinder(a, m):
    print("---------find GCD---------")
    if (m % a == 0):
        print("GCD equals: {}".format(min(m, a)))
        return min(m, a)
    global steps
    # initialize
    gcd = 0
    int_dividend = m
    int_divisor = a
    int_quotient = int_dividend // int_divisor
    int_remainder = int_dividend - int_quotient * int_divisor

    # appending lists
    list_quotients.append(int_quotient)
    list_diviends.append(int_dividend)
    list_divisors.append(int_divisor)

    print("dividend: {} | divisor: {} | quotient : {} | remainder: {}"
          .format(int_dividend, int_divisor, int_quotient, int_remainder))
    while (int_remainder != 0):
        int_dividend = int_divisor
        int_divisor = int_remainder
        int_quotient = int_dividend // int_divisor

        list_quotients.append(int_quotient)
        list_diviends.append(int_dividend)
        list_divisors.append(int_divisor)

        if (int_dividend - int_quotient * int_divisor == 0):
            gcd = int_remainder
        int_remainder = int_dividend - int_quotient * int_divisor

        print("dividend: {} | divisor: {} | quotient : {} | remainder: {}"
              .format(int_dividend, int_divisor, int_quotient, int_remainder))
        steps = steps + 1
    print("--->GCD = {}".format(gcd))
    return gcd


def inverse(gcd):
    print("---------Inverse step---------")
    global list_quotients
    global list_diviends
    global list_divisors

    list_quotients = list_quotients[0:steps]
    list_quotients.reverse()

    list_diviends = list_diviends[0:steps]
    list_divisors = list_divisors[0:steps]

    r = [0] * steps
    s = [0] * steps
    r[0] = 1
    s[0] = -(list_quotients[0])

    print("{} = {}.{} + {}.{}"
          .format(gcd, list_diviends[-1], r[0] if r[0] > 0 else "(" + str(r[0]) + ")", list_divisors[-1],
                  s[0] if s[0] > 0 else "(" + str(s[0]) + ")"))
    for i in range(1, steps):
        r[i] = s[i - 1]
        s[i] = r[i - 1] - list_quotients[i] * s[i - 1]
        print("{} = {}.{} + {}.{}".format(gcd, list_diviends[-i - 1], r[i] if r[i] > 0 else "(" + str(r[i]) + ")",
                                          list_divisors[-i - 1], s[i] if s[i] > 0 else "(" + str(s[i]) + ")"))
    invert_s = s[-1]
    print("---> r = {},s = {}".format(r[-1], s[-1]))
    return invert_s


def check(gcd, b):
    if (b % gcd == 0):
        return True
    else:
        return False


def findX(gcd, s, b, m):
    x = []
    x0 = ((s * b) / (gcd)) % (m / gcd)
    for i in range(gcd):
        xn = x0 + i * (m / gcd)
        if (xn != 0):
            x.append(int(xn))
    return x


def main():
    print("ax = b mod m, find x")
    while True:  # Keep getting input from the user
        try:
            int_a = int(input('Input a: '))
            int_b = int(input('Input b: '))
            int_m = int(input('Input m: '))
            break
        except ValueError:
            print('Conversion error, please re-enter the values!')
            continue
    gcd = int(gcdFinder(int_a, int_m))
    if(check(gcd,int_b)):
        invert_s = inverse(gcd)
        all_x = findX(gcd, invert_s, int_b, int_m)
        print("---------solution---------")
        print("x =", format(all_x))
    else:
        print("---------solution---------")
        print("There is no solution because {} does not divide by {}".format(int_b,gcd))


main()
