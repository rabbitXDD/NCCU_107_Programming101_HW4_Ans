go = True
players = []
data = input()
while go:
    row = input()
    if row == '-1':
        go = False
        break
    else:
        row = row.split(',')
        # player_tuple: (Stephen Curry, 29.5, 6.1, 5.0, 0.3, 1)
        player_tuple = (
            row[0], float(row[1]), float(row[2]), 
            float(row[3]), float(row[4]), float(row[5])
        )
        players.append(player_tuple)

# Sort list with regular function
# Firstly sort by given column(PTS, AST...) in descending order
# Secondly, sort by player's name in ascending order 
# if there are player have the same value in first round.

def sortByPts(input_list):
    return -input_list[1], input_list[0]
def sortByAst(input_list):
    return -input_list[2], input_list[0]
def sortByTrb(input_list):
    return -input_list[3], input_list[0]
def sortByBlk(input_list):
    return -input_list[4], input_list[0]
def sortByStl(input_list):
    return -input_list[5], input_list[0]

if data == 'PTS':
    sorted_players = sorted(players, key=sortByPts)
elif data == 'AST':
    sorted_players = sorted(players, key=sortByAst)
elif data == 'TRB':
    sorted_players = sorted(players, key=sortByTrb)
elif data == 'BLK':
    sorted_players = sorted(players, key=sortByBlk)
else:
    sorted_players = sorted(players, key=sortByStl)

# Sort list with lambda function (For reference)

if data == 'PTS':
    sorted_players = sorted(players, key=lambda x : (-x[1], x[0]))
elif data == 'AST':
    sorted_players = sorted(players, key=lambda x : (-x[2], x[0]))
elif data == 'TRB':
    sorted_players = sorted(players, key=lambda x : (-x[3], x[0]))
elif data == 'BLK':
    sorted_players = sorted(players, key=lambda x : (-x[4], x[0]))
else:
    sorted_players = sorted(players, key=lambda x : (-x[5], x[0]))
    
print('The leaderboard of ' + data)    
for ele in sorted_players:
    print(ele[0])