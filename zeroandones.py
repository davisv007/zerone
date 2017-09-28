prevmin = 0
prevmax = 0

state = None
lenlist = None


def main():
    intlist = input('zeroes and ones?')
    numbergenerator = nummer(intlist)
    groupgenerator = grouper(numbergenerator)
    mingenerator = minner(groupgeneratogitr)
    maxgenerator = maxer(mingenerator)


def nummer(intlist):
    yield from iter(intlist)


def maxer(minner):
    prevmax = 0
    while True:
        current = next(minner)
        yield max(current, prevmax)
        prevmax = current


def minner(grouper):
    prevmin = 0
    while True:
        current = next(grouper)
        yield min(prevmin, current)
        prevmin = current


def grouper(nummer):
    num = 0
    prevele = None
    while True:
        element = next(nummer)
        state = element == '0'
        if prevele != state:
            yield num
            num = 0
        num += 1
        prevele = state


main()
