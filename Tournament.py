player_list=[]
wins_list=[]
losses_list=[]
for s in range(1,17):
    player_list.append(s)
print("Round of 16")
print("Competitiors:",player_list)
print("="*200)
for k in range(0,8):
    winner=int(input(str(player_list[2*k])+" vs "+str(player_list[2*k+1])+":"))
    if winner==player_list[2*k]:
        player_list[2*k+1]=0
        print(winner,"goes to the Round of 8")
        print("="*200)
    elif winner==player_list[2*k+1]:
        player_list[2*k]=0
        print(winner,"goes to the Round of 8")
        print("="*200)
while 0 in player_list:
    player_list.remove(0)
print("Round of 16 finished")
print("Remaining members:",player_list)
print("="*200)
print("Round of 8")
print("="*200)
for k in range(0,4):
    winner=int(input(str(player_list[2*k])+" vs "+str(player_list[2*k+1])+":"))
    if winner == player_list[2 * k]:
        player_list[2 * k + 1] = 0
        print(winner, "goes to the semi-final")
        print("=" * 200)
    elif winner == player_list[2 * k + 1]:
        player_list[2 * k] = 0
        print(winner, "goes to the semi-final")
        print("=" * 200)
while 0 in player_list:
    player_list.remove(0)
print("Round of 8 finished")
print("Remaining members:",player_list)
print("="*200)
print("semi-final")
print("="*200)
for k in range(0,2):
    winner = int(input(str(player_list[2 * k]) + " vs " + str(player_list[2 * k + 1]) + ":"))
    if winner == player_list[2 * k]:
        player_list[2 * k + 1] = 0
        print(winner, "goes to the final")
        print("=" * 200)
    elif winner == player_list[2 * k + 1]:
        player_list[2 * k] = 0
        print(winner, "goes to the final")
        print("=" * 200)
while 0 in player_list:
    player_list.remove(0)
print("Semi-final finished")
print("Remaining members:",player_list)
print("="*200)
print("final")
print("="*200)
winner = int(input(str(player_list[0]) + " vs " + str(player_list[1]) + ":"))
if winner == player_list[0]:
    print(winner, "wins the tournament")
    print("=" * 200)
elif winner == player_list[1]:
    print(winner, "wins the tournament")
    print("=" * 200)



