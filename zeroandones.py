def main():
    intlist = list(input('zeroes and ones?'))
    state, prev, num, lenlist = None, None, 0, []

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

    pairlist = [lenlist[i: i + 2] for i in range(0, len(lenlist), 2)] + \
               [lenlist[i: i + 2] for i in range(1, len(lenlist), 2)]

    # find the max across the mins across the pairs of the elements of these two lists
    jax = max(list(map(min, [element for element in pairlist if len(element) == 2])))
    print(jax)


main()