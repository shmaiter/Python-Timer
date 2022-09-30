from timer import Timer


def swap_case1(s):
    return s.swapcase()


def swap_case2(s):
    return ''.join([i.upper() if i.islower() else i.lower() for i in s])


def swap_case3(s):
    output = ''

    for x in s:
        if (x.isupper() == True):
            output += x.lower()
        elif (x.islower() == True):
            output += x.upper()
        else:
            output += x

    return output


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'

    t = Timer()
    t.start()
    result = swap_case1(s)
    t.stop()

    t.start()
    result = swap_case2(s)
    t.stop()

    t.start()
    result = swap_case3(s)
    t.stop()
