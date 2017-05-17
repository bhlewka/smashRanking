from glicko2 import Player



class Match:
    
   def __init__(self, winner, loser, winnerScore, loserScore, date):
      self.winner = winner
      self.loser = loser
      self.winnerScore = winnerScore
      self.loserScore = loserScore
      self.date = date
    
