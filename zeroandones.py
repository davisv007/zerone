def main():
    zlist = list(input('zeroes and ones?'))
    state, prev, word = None, None, None
    nlist = []

    for element in zlist:
        state = element == '0'
        if prev != state:
            nlist.append(word)
            word = ''
        word += element
        prev = state

    nlist = nlist[1:] + [word]  # append final word,remove initial word

    if len(nlist) % 2 == 0:
        hlist = []
        klist = [nlist[i: i + 2] for i in range(0, len(nlist) - 2, 2)]
    else:
        hlist = [nlist[i: i + 2] for i in range(0, len(nlist) - 2, 2)]
        klist = [nlist[i: i + 2] for i in range(1, len(nlist), 2)]
        # we can get rid of the first and last elements in this case

    max = 0
    for lst in [hlist,klist]:
        for element in lst:
            if len(element) == 2:
                consec = min(len(element[0]), len(element[1]))
                if max < consec:
                    max = consec

    print(max)


main()
