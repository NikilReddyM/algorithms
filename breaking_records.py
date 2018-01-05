def breakingTheRecords(game):
    hr= game[0]
    lr= game[0]
    hrc=0
    lrc=0
    for i in game[1:]:
        if i > hr:
            hrc += 1
            hr = i
        if i < lr:
            lrc+= 1
            lr = i
    print(hrc,lrc)


n=input()
game = list(map(int,input().split()))
breakingTheRecords(game)