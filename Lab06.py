'''
Kwabena Ansah
Lab06 Solution File
'''

'''
Part II
=======
#Solution Ex.1
'''
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team
'''
#Solution Ex.2
'''
    def add_score(self,date,score):
        self.scores.append(score)

'''
#Solution Ex.3
'''        
    def total_score(self):
        return sum(self.scores)
'''
#Solution Ex.4
'''    
    def average_score(self):
        return float(sum(self.scores))/len(self.scores)
'''
#Solution Ex.5
'''    
torres=Player('Fernando','Torres')
scores=[0,0,1,0,1]
for i in scores:
    torres.add_score('date', i)

print torres.average_score()

'''
Part III
========
'''
class Team:
    
    def __init__(self,name,league,manager_name,points=0):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.points=points
        self.players=[]
        
    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        return self.name+' play in '+self.league
        
    
portugal=Team('Portugal','Europe','Paulo Bento')
spain=Team('Spain','Europe','Del Bosque')
print spain
print portugal
torres=Player('Fernando','Torres',spain)
ronaldo=Player('Cristiano','Ronaldo',portugal)
spain.add_player(torres)
portugal.add_player(ronaldo)

import datetime
class Match:
    def __init__(self,home,away):
        self.home_team=home
        self.away_team=away
        self.date=None
        self.home_scores={}
        self.away_scores={}
        
    def home_score(self):
        return sum(self.home_scores.values())
    
    def away_score(self):
        return sum(self.away_scores.values())
    
    def winner(self):
        if self.home_score()>self.away_score():
            print self.home_team.name
        else:
            print self.away_team.name
        
    def add_score(self,player,score):
        player_team=player.team
        if player_team == self.home_team:
            print 'home'
            if player.last_name in self.home_scores.keys():
                self.home_scores[player.last_name]+=score
            else:
                self.home_scores[player.last_name]=score
                
        if player_team == self.away_team:
            print 'away'
            if player.last_name in self.away_scores.keys():
                self.away_scores[player.last_name]+=score
            else:
                self.away_scores[player.last_name]=score
        
euro_semi_final=Match(spain,portugal)
euro_semi_final.add_score(torres, 1)
euro_semi_final.add_score(ronaldo, 1)
euro_semi_final.add_score(torres, 1)
euro_semi_final.winner()
print euro_semi_final.away_scores
