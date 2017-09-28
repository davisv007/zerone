def main(intlist=list(input('zeroes and ones?')), state=None, prev=None, num=0, lenlist=[]):
    # create list of lengths of consecutive zeroes and ones
    for element in intlist:
        state = element == '0'
        if prev != state:
            lenlist.append(num)
            num = 0
        num += 1
        prev = state

    # append final num,remove initial 0
    lenlist = lenlist[1:] + [num]

    pairlist = zip(lenlist, lenlist[1:]) + zip((lenlist[1:], lenlist[2:]))

    # find the max across the mins across the pairs of the elements of these two lists
    print(max(list(map(min, [pair for pair in pairlist if len(pair) == 2]))))


main()