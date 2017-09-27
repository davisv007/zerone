def main():
    zlist = list(input('zeroes and ones?'))
    state, prev, word = None, None, None
    nlist = []

    # group up ones with ones and zeroes with zeroes
    for element in zlist:
        state = element == '0'
        if prev != state:
            nlist.append(word)
            word = ''
        word += element
        prev = state

    nlist = nlist[1:] + [word]
    # append final word,remove initial word


    hlist = [nlist[i: i + 2] for i in range(0, len(nlist), 2)]
    klist = [[nlist[0]]] + [nlist[i: i + 2] for i in range(1, len(nlist), 2)] if len(nlist)% 2 !=0 else []

    max = 0
    #sneaking suspicion this can be done with either list comp or reduce
    for lst in [hlist, klist]:
        for element in lst:
            consec = min(list(map(len,element)))
            if max < consec:
                max = consec

    print(max)


main()
