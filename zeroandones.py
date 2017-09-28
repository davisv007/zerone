prevmin = 0
prevmax = 0

state = None
lenlist = None


def main():
    intlist = input('zeroes and ones?')
    numbergenerator = nummer(intlist)
    groupgenerator = grouper(numbergenerator)
    print(next(groupgenerator))
    print('burp')
    print(next(groupgenerator))
    print(next(groupgenerator))
    print(next(groupgenerator))
    # print(next(groupgenerator))
    # print(next(groupgenerator))
    # mingenerator = minner(groupgeneratogitr)
    # maxgenerator = maxer(mingenerator)


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
    num=0
    current = next(nummer)
    prevele = current
    while True:
        try:
            while current ==prevele:
                prevele=current
                current=next(nummer)
                num+=1
            else:
                yield num
                num=1
                prevele=current
                current=next(nummer)

        except StopIteration:
            yield num



main()
