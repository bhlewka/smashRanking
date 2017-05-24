def printRankings(playerDict):
    
    orderedRank = []
    
    for key in playerDict:
        orderedRank.append(playerDict[key])
    
    sortPlayers(orderedRank)
    
    for player in orderedRank:
        print(player.name, player.rating)
        
    return orderedRank