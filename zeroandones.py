def main():
    intlist = list(input('zeroes and ones?'))
    state, prev, num, lenlist = None, None, 0, []

    # group up ones with ones and zeroes with zeroes
    for element in intlist:
        state = element == '0'
        if prev != state:
            lenlist.append(num)
            num = 0
        num += 1
        prev = state

    # append final num,remove initial num
    lenlist = lenlist[1:] + [num]

    pairlist = [lenlist[i: i + 2] for i in range(0, len(lenlist), 2)]
    pairlist += [[lenlist[0]]] + [lenlist[i: i + 2] for i in range(1, len(lenlist), 2)] if len(lenlist) % 2 != 0 else []

    # find the max across the mins across the pairs of the elements of these two lists
    jax = max(list(map(min, pairlist)))
    print(jax)


main()