from glicko2 import Player
from matches import getParticipants

#no inactivity implementation, no dq handling
#problem if a player object doesn't exist ie. add new player a? and you decline
#if player b has a match with player a it messes up

#if the program is only able to write names and to output file, readElo bugs out 
#because it will try to convert strings to floats or something


#use ben's getParticipants and compares its dictionary values to the input dict's values 
#returns a list of players
def updatePlayerList(inputPlayerDict, inputDictionary):
    #read matches.txt file and updates dictionary
    for key, value in inputDictionary.items():
        if value not in inputPlayerDict:
            userChoice = input("New player: " + value + ". Add as new player or existing?\nType in add to add as new player, edit to add to existing tag, or type exit to exit.\n")
            if userChoice.lower() == "add":
                inputPlayerDict[value] = Player(value)
            #if not userChoice.lower() == "edit":
                #break
            if userChoice.lower() == "edit":
                existingTag = input("Enter the correct tag: ")
                if existingTag in inputPlayerDict:
                    inputPlayerDict[value] = inputPlayerDict[existingTag]
                if existingTag not in inputPlayerDict:
                    newTag = input("Tag not found. Enter the new tag: ")
                    inputPlayerDict[newTag] = Player(newTag)
            if userChoice.lower() == "exit": 
                break
            
    return inputPlayerDict

#each line in input file is of format: playerA 1 playerB 2
#adds players' opponents, and results
#returns dictionary of player objects 
def addPlayerMatches(playerDict, playerList, matches):
    
    #open player match file to read
    matchOutput = open(matches, "r")
    matchOutput = matchOutput.read()
    #split each word
    matchOutput = matchOutput.split()
    matchOutput.pop(0)

    #if a score < 0 it is a dq? haven't done anything with it yet, just 
    #disregarded those matches for now
    for x in range(1, len(matchOutput), 4):
        if matchOutput[x] > matchOutput[x+2]:
            if matchOutput[x-1] in playerDict:
                #print("a")
                playerDict[matchOutput[x-1]].addMatch(playerDict[matchOutput[x+1]], 1)
            if matchOutput[x+1] in playerDict:
                    #print("b")
                    playerDict[matchOutput[x+1]].addMatch(playerDict[matchOutput[x-1]], 0)
                
        elif matchOutput[x] < matchOutput[x+2] and int(matchOutput[x]) >=0: 
            if matchOutput[x-1] in playerDict:
                    #print("c")
                playerDict[matchOutput[x-1]].addMatch(playerDict[matchOutput[x+1]], 0) 
            if matchOutput[x+1] in playerDict:
                    #print("d")
                playerDict[matchOutput[x+1]].addMatch(playerDict[matchOutput[x-1]], 1)
                
    return playerDict


#takes dictionary of player objects and updates attributes
def updatePlayers(playerDict):
          
    for player in playerDict:
        playerDict[player].update_player()
        
    return playerDict

#input file format: name, rating, rd, vol
#updates playerDict with player info from input file
def readElo(playerInfoInput, playerDict):
    
    fileToOpen = open("text.txt", "r")
    file = fileToOpen.read()
    file = file.splitlines()
    try:
        file.pop(0)
    except:
        pass
    
    #list containing all info
    playerInfo = list()
    for line in file:
        for person in line.split():
            playerInfo.append(person)

    #create player objects 
    #x is name, x+1 is rating, x+2 is rd, x+3 is vol
    for x in range(0, len(playerInfo), 4):
        playerDict[playerInfo[x]] = Player(playerInfo[x])
        playerDict[playerInfo[x]].rating = float(playerInfo[x+1])
        playerDict[playerInfo[x]].rd = float(playerInfo[x+2])
        playerDict[playerInfo[x]].vol = float(playerInfo[x+3])
         
    return playerDict
            

def main():
    
    #input text file of existing players
    while(True):
        playerListFile = input("Enter the file name of your list of players and their rating, etc...: ")
        try:
            playerList = open(playerListFile, "r")
            break
        except:
            print("Cannot find the file.")
    
    #create a dict for players from input file
    playerDict = dict()
    #only works with input files having names separated by spaces 
    playerList = playerList.read()
    playerList = playerList.splitlines()
    readElo(playerList, playerDict)
    
    #get rid of hardcode later
    name = "edmmelee-SmashAtCASE042817Melee"
    apiKey = "iRZrPhoDkyLV2xFXyUuJ5pVauosMlZPGMMmCdSaE"
   
    players = getParticipants(name, apiKey)
    updatePlayerList(playerDict, players)

    #update player list text file
    outputFile = open(playerListFile, "w")
    outputFile.write("")
    outputFile.close()
    outputFile = open(playerListFile, "a")
    for player in playerDict:
        outputFile.write(player + "\n")
    outputFile.close()

    while(True):
        matchInput = input("Enter the name of your matches file: " )    
        try:
            playerDict = addPlayerMatches(playerDict, playerDict, matchInput)    
            break
        except:
            print("Cannot find the file.")
            
    #playerDict = addPlayerMatches(playerDict, playerDict, matchInput)       
    updatePlayers(playerDict)
    
    
    #print player objects to output file    
    file = open(playerListFile, "w")
    file.write("")
    file.close()
    file = open(playerListFile, "a")
   
    outputList = list()
    for player in playerDict:
        atts = (playerDict[player].getAttributes())
        outputList.append(atts)
       
    file.write("name, rating, rd, vol\n")
    
    for line in outputList:
        file.write(str(line).replace("(", "").replace(")", "").replace("'", "").replace(",", ""))
        file.write("\n")
    file.close()    
    

    ##test print
    #for player in playerDict:
        #print(playerDict[player].getAttributes())

    
main()

    
