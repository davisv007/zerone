def main():
    intlist = input('zeroes and ones?')
    numbergenerator = nummer(intlist)
    groupgenerator = grouper(numbergenerator)
    mingenerator = minner(groupgenerator)
    maxgenerator = maxer(mingenerator)

    print(max([x for x in maxgenerator]))

def nummer(intlist):
    yield from iter(intlist)


def maxer(minner):
    prevmax = next(minner)
    while True:
        current = next(minner)
        yield max(current, prevmax)
        prevmax = current


def minner(grouper):
    prevmin = next(grouper)
    while True:
        current = next(grouper)
        yield min(prevmin, current)
        prevmin = current


def grouper(nummer):
    num = 0
    current = next(nummer)
    prevele = current
    fails = 0
    while True:
        try:
            while current == prevele:
                prevele = current
                current = next(nummer)
                num += 1
            else:
                yield num
                num = 1
                prevele = current
                current = next(nummer)
        except StopIteration:
            return num


main()
