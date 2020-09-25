from random import choices
ntrials=15000
di = 6
player1wins = 0
for i in range(ntrials):
    p2roll = choices(range(1,di+1), k=2)
    if p2roll[0] == p2roll[1]:
        continue
    p1roll = choices(range(1,di+1), k=3)
    p1roll.sort(reverse=True)
    p1total = p1roll[0] + p1roll[1]
    if p1roll.count(2) == 2:
        continue
    if p1total > p2roll[0]+p2roll[1]:
        player1wins += 1


print("player 1 win ratio=",player1wins/ntrials)
print("player 1 wins=",player1wins)