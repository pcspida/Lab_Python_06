"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

'''
Solution by Kwabena Ansah
'''

## create the player_stats data structure
player_stats={datetime.date(2012,06,24):['rooney',2],
              datetime.date(2012,06,25):['rooney',2],
              datetime.date(2012,06,19):['ronaldo',0],
              datetime.date(2012,06,20):['ronaldo',3],
              datetime.date(2012,06,21):['torres',0],
              datetime.date(2012,06,22):['torres',1]}

print player_stats[datetime.date(2012,06,22)]
'''
Dictionary with the date as it's key and players name and score as the value.
Name and score are entered as a list because it's mutable, the records can be updated.
'''

## implement highest_score
def highest_score(player_stats):
    highest=0
    high_date=0
    for date in player_stats.keys():
        play_goals=player_stats[date]
        if play_goals[1]>highest:
            highest=play_goals[1]
            high_date=date
    play_goals=player_stats[high_date]
    return (play_goals[0],high_date,play_goals[1])
    
print highest_score(player_stats)          

## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    highest=0
    high_date=0
    for date in player_stats.keys():
        play_goal=player_stats[date]
        if player in play_goal:
            
            if play_goal[1]>highest:
                highest=play_goal[1]
                high_date=date
    play_goal=player_stats[high_date]
    return (play_goal[0],high_date,play_goal[1])

print highest_score_for_player(player_stats,'ronaldo') 


## implement highest_scorer
def highest_scorer(player_stats):
    sum_score=0
    high_scorer=''
    all_play={}
    for date in player_stats.keys():
        play_goals=player_stats[date]
        if play_goals[0] in all_play.keys():
            all_play[play_goals[0]]+=play_goals[1]
        else:
            all_play[play_goals[0]]=play_goals[1]
    for player in all_play.keys():
        if all_play[player]>sum_score:
            sum_score=all_play[player]
            high_scorer=player
    return player
    
print highest_scorer(player_stats)  
