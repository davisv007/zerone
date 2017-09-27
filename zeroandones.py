





def main():
    zlist=list(input('zeroes and ones?'))
    state=None
    prev=None
    nlist=[]
    word =None
    #print(zlist)
    for element in zlist:
        if element == '0':
            state=True
        else:
            state = False
        if prev == state:
            word +=element
        else:
            nlist.append(word)
            word = element
        prev = state
    nlist.append(word)
    nlist = nlist[1:]
    #print(nlist)
    if len(nlist) % 2 == 0:
        hlist=[]
        klist = [nlist[i: i + 2] for i in range(0, len(nlist) - 2, 2)]
    else:
        hlist=[nlist[i: i + 2] for i in range(0, len(nlist) - 2, 2)]+[[nlist[-1]]]
        klist=[[nlist[0]]]+[nlist[i: i + 2] for i in range(1, len(nlist), 2)]
        # we can get rid of the first and last elements in this case, but we'll keep them for now
    # print(hlist)
    # print(klist)
    max=0
    for element in hlist:
        if len(element) == 2:
            consec = min(len(element[0]),len(element[1]))
            if max < consec:
                max= consec
    for element in klist:
        if len(element) == 2:
            consec = min(len(element[0]),len(element[1]))
            if max < consec:
                max= consec
    print(max)
main()