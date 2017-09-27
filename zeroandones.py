
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

    # append final word,remove initial word
    nlist = nlist[1:] + [word]


    hlist = [nlist[i: i + 2] for i in range(0, len(nlist), 2)]
    klist = [[nlist[0]]] + [nlist[i: i + 2] for i in range(1, len(nlist), 2)] if len(nlist)% 2 !=0 else klist

    #find the max accros the mins across the pairs of the elements of these two lists
    jax = 0
    #sneaking suspicion this can be done with either list comp or reduce
    #effeciency or brevity??
    #brevity!! (at least for this challenge)
    for lst in [hlist, klist]:
        minlist=list(map(min,[list(map(len,element)) for element in lst]))
        jax=max(max(minlist),jax)
    print(jax)


main()
