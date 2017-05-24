# Challonge initialization
# "File 2"
import time
from urllib.request import urlopen
import smtplib
import xml.etree.ElementTree as ET

from RankingObjects import *
#from matches2 import *

# Takes tournament name (eg. edmmelee-vapebracket10201) and APIKey and returns a dictionary of participants
# and their local tournament ID
# If you just want the participant list you can list off the keys of the dictionary
# Alternativiely I could change this to have an option that returns a list instead
def getParticipants(name, apiKey):
    url = "https://api.challonge.com/v1/tournaments/" + name +"/participants.xml?api_key=" + apiKey
    txt = urlopen(url).read()
    txt = txt.decode('utf-8')
    parts = dict()
    
    # Text becomes an xml tree object
    txt = ET.fromstring(txt)
    
    # Append each participant.name to list of participants
    # While also stripping spaces/whitespace and making names lowercase
    # This should be a dictionary
    for part in txt:
        
        parts[part[0].text] = part[2].text.replace(" ","").lower()
        
        #player = []
        #player.append(part[2].text.replace(" ","").lower())
        #player.append(part[0].text)
        #parts.append(player)
   
    return parts

# Takes tournament name (eg. edmmelee-vapebracket10201) and APIKey and returns a list of match objects
# These match objects have a date so you can in theory sort all returned matches by the date they happened
# They are ordered from round1 -> grand finals in a chronological order
def getMatches(name, apiKey):
    url = "https://api.challonge.com/v1/tournaments/" + name +"/matches.xml?api_key=" + apiKey
    txt = urlopen(url).read()
    txt = txt.decode('utf-8')
    matches = []
    participants = getParticipants(name, apiKey)
    
    # Text becomes an xml tree object
    txt = ET.fromstring(txt)
    
    # Get date function will obselete
    # Store date here instead
    date = txt[0][11].text
    
    # Currently hardcoded, winner loser is index 9 10
    # Better to do differently due to the way score is formatted
    # player 1 is index 3, player 2 is index 4
    # score is 29
    ## Hardcoded for single digit scores
    # Can be easily fixed for 2 digit scores in the future, split at the "-"
    # Yeah, split here at version 3, if retard to's input meme scores itll fuck shit up
    # This is fixed, score is now grabbed better
    for match in txt:
        ind = []
        
        # Ensuring the program doesn't go full retard if there is a negative score input may be a challenge
        # Worst case is 2 negative scores, should not happen, however we can handle it
        # If a score value is an empty string, we know the next score value must have a negative infront of it
        # So maybe iterate over the split list
        # If char = "" then pop char, insert to front of next char a "-"
        
        # Possibly include fix for meme games, if val is negative set a hard score
        # detect whether a forfeit was encountered and set the score to a predefined DQ score
        # instead of whatever the TO decides to do to signify the player did not "win" or "lose"
        
        #print(match[29].text)
        score = match[29].text.split('-')
        for char in score:
            if char == "":
                score.remove("")
                score[0] = "-" + score[0]
        #print(score)
        
        #player1, player1 score, player2, player2 score
        ind.append(match[3].text)
        ind.append(score[0])
        ind.append(match[4].text)
        ind.append(score[1])
        matches.append(ind)
        
        
    # Creates a list of match objects, should be done in the above loop but it can be here for now lol    
    matches2 = []  
    for match in matches:
        player1 = participants[match[0]]
        score1 = match[1]
        player2 = participants[match[2]]
        score2 = match[3]
        
        if (score1 > score2):
            matches2.append(Match(player1, player2, score1, score2, date))
        else:
            matches2.append(Match(player2, player1, score2, score1, date))
            
        
   
    #Testing for indices    
    #count = 0
    #for thing in txt[0]:
        #print(thing.text, count)
        #count += 1
        
    return matches2 

# Will prompt the user the specify the text file containing the apiKey as well
# as a list of tournaments formatted as edmmelee-case21342
# Will return large list of matches from all tournaments
# Ordered in batches, first tournament processed, first tournament batch of matches
# Ensure your input file's tournaments are listed chronologically
# Although each match has a date attribute so you can process stuff using the date outside instead
# Will also return a set containing all tags
def getTournamentData(mode = 0):
    
    # Mode is the optional argument to put in a file instead
    if(mode == 1):
        # open the file, ensuring a file exists 
        while(True):
            fileToOpen = input("What is the name of the input file?: ")
            
            try:
                file = open(fileToOpen, 'r')
                break
            except:
                print("File not found or cannot be opened")
                
        file = file.read()  
        file = file.splitlines()
        
        # Pop the api key
        apiKey = file.pop(0)
        
    else:
        apiKey = input("Enter your API key: ")
        name = input("Enter the tournament name in the form <subdomain-name>: ")
        file = []
        file.append(name)
        
    
    # Process the data for each tournament
    # This could error correct if the tournament name was copy/pasted wrong
    # Ill fix this later in the third version or some shit
    # Make sure the tournaments exist
    # Insert name as <host-name>
    finalMatchList = []
    finalParticipantSet = set()
    for tournament in file:
        matches = getMatches(tournament, apiKey)
        participants = getParticipants(tournament, apiKey)
        participants = list(participants.values())
        for match in matches:
            finalMatchList.append(match)
        for part in participants:
            finalParticipantSet.add(part)
        print(tournament, "values computed")

    return finalMatchList, list(finalParticipantSet)

def getTournament(rankingDict):

    matchList, entrantList = getTournamentData()

    if len(rankingDict) == 0:
        for entrant in entrantList:
            rankingDict[entrant] = Player(entrant)
    else:
        for entrant in entrantList:
            if entrant not in rankingDict:
                while():
                    check = input("If %s is a new player, press n, if %s is an alt tag, press a: " % (entrant, entrant))
                    if check.lower() == "n":
                        rankingDict[entrant] = Player(entrant)
                        break
                    elif check.lower() == "a":
                        while():
                            tag = input("Enter the original tag of this player: ")
                            if tag.lower() in rankingDict:
                                rankingDict[entrant] = rankingDict[tag.lower]
                                break
                            else:
                                print("This tag is not found, try again.")
                        break

    for match in matchList:
        match.addMatchToPlayers()


def getRankings():
    while (True):
        fileToOpen = input("What is the name of the ranking input file?: ")

        try:
            file = open(fileToOpen, 'r')
            break
        except:
            print("File not found or cannot be opened")

    file = fileToOpen.read()
    file = file.splitlines()

    try:
        file.pop(0)
    except:
        pass

    rankingDict = {}

    # list containing all info
    playerInfo = list()
    for line in file:
        for person in line.split():
            playerInfo.append(person)

    # create player objects
    # x is name, x+1 is rating, x+2 is rd, x+3 is vol
    for x in range(0, len(playerInfo), 4):
        rankingDict[playerInfo[x]] = Player(playerInfo[x])
        rankingDict[playerInfo[x]].rating = float(playerInfo[x + 1])
        rankingDict[playerInfo[x]].rd = float(playerInfo[x + 2])
        rankingDict[playerInfo[x]].vol = float(playerInfo[x + 3])

    return rankingDict


def updateRankings(rankingDict):
    for player in rankingDict:
        rankingDict[player].updatePlayer()


def outputRankings(rankingDict):
    while (True):
        fileToOpen = input("What is the name of the ranking output file?: ")
        try:
            file = open(fileToOpen, "w")
            break
        except:
            print("File not found or cannot be opened")

    file.write("")
    file.close()
    file = open(fileToOpen, "a")

    file.write("name, rating, rd, vol\n")
    for player in rankingDict:
        atts = (rankingDict[player].getAttributes())
        file.write(str(atts).replace("(", "").replace(")", "").replace("'", "").replace(",", ""))
        file.write("\n")
    file.close()


        
# Here is a useful function for sorting the final output of the 
# ordered elo scores
# leave key=lambda alone
# x:x.<whatever att to sort by>
# reverse just makes it highest to lowest

def sortPlayers(playerList):
    # playerList will be a list of player basicPlayer objects
    
    playerList.sort(key=lambda x: x.score, reverse=True)


