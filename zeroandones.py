prevmin = 0
prevmax = 0

state = None
lenlist = None


def main():
    intlist = input('zeroes and ones?')
    numbergenerator = nummer(intlist)
    groupgenerator = grouper(numbergenerator)
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


def grouper(nummer):git 
    num=0
    firstpass=True
    prevele = 'p'
    while True:
        try:
            current = next(nummer)
        except StopIteration:
            yield num
        if firstpass:
            continue
        else:
            if current !=prevele:
                yield num
                num = 0
        prevele = current
        num+=1
        firstpass=False



main()
