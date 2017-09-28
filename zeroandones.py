def main():
    intlist = input('zeroes and ones?')
    numbergenerator = nummer(intlist)
    groupgenerator = grouper(numbergenerator)
    mingenerator = minner(groupgenerator)
    answergenerator = maxer(mingenerator)

    print(next(answergenerator))

def nummer(intlist):
    yield from iter(intlist)


def maxer(minner):
    current=0
    for element in minner:
        current = max(current,element)
    yield current


def minner(grouper):
    prevmin = next(grouper)
    while True:
        try:
            current = next(grouper)
            yield min(prevmin, current)
            prevmin = current
        except:
            yield prevmin
            return


def grouper(nummer):
    num = 0
    current = next(nummer)
    prevele = current
    while True:
        try:
            while current == prevele:
                num += 1
                prevele = current
                current = next(nummer)
            else:
                yield num
                num = 1
                prevele = current
                current = next(nummer)
        except StopIteration:
            yield num
            return


main()
