# Matchmaking 
# Create a list of players
# Sort it by their ELO score

import random

class basicPlayer:
    
    def __init__(self, name, score):
        
        self.name = name
        self.score = score
        
        
def sortPlayers(playerList):
    # playerList will be a list of player basicPlayer objects
    
    playerList.sort(key=lambda x: x.score, reverse=True)
    
    
    
def main(inputFile):
    
    while(True):    
        try:
            file = open(inputFile, 'r')
            break
        except:
            print("File not found or cannot be opened")
            return -1    
    
plist = []    
for i in range(1,6):
    basicP = basicPlayer("Kappa"+str(i), i)
    plist.append(basicP)

random.shuffle(plist)
sortPlayers(plist)
for player in plist:
    print(player.name)
    



    
