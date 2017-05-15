import time
from urllib.request import urlopen
import smtplib
import xml.etree.ElementTree as ET

# The next step of this program is to allow user to designate a text document containing urls for tournaments? 
# What about returning a list of tournaments and allowing the user to designate which to include, going back to a certain date?
# Renaming the tournaments in challonge would make things easier but who knows


# This will return a python list object of all the names of people in the tournament
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


# This will return all the matches
# We should also create a function to return us the simple dateTime of the first round report or whatever
# So we know the date of the tournament
def getMatches(name, apiKey):
    url = "https://api.challonge.com/v1/tournaments/" + name +"/matches.xml?api_key=" + apiKey
    txt = urlopen(url).read()
    txt = txt.decode('utf-8')
    matches = []
    
    # Text becomes an xml tree object
    txt = ET.fromstring(txt)
    
    
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
        ind.append(match[3].text)
        ind.append(score[0])
        ind.append(match[4].text)
        ind.append(score[1])
        matches.append(ind)
        
   
    #Testing for indices    
    #count = 0
    #for thing in txt[0]:
        #print(thing.text, count)
        #count += 1
        
    return matches   

def getDate(name, apiKey):
    url = "https://api.challonge.com/v1/tournaments/" + name +"/matches.xml?api_key=" + apiKey
    txt = urlopen(url).read()
    txt = txt.decode('utf-8')
    date = ''
        
    # Text becomes an xml tree object
    txt = ET.fromstring(txt)
    
    date = txt[0][11].text
    
    return date
    
    
        
def outputScores(participants, matches, date,iteration):
    # participants is participants, to be find/replaced later
    file = open("output"+str(iteration)+".txt", "a")
    file.write(date)
    file.write('\n')
    # Replace the player id in matches with the player name from player dict
    for match in matches:
        match[0] = participants[match[0]]
        match[2] = participants[match[2]]
        
        # Now format the list into a writeable format
        
        line = match[0] + ' ' + match[1] +' ' + match[2] +' ' + match[3] + '\n'
        
        file.write(line)
        
        #file.write('\n')
        
    file.close()  
    #print(matches)
    return matches
      
def main():
    # open input file in read only
    # create a list of tournaments provided by the read only file
    # Api key must be first element, space seperated
    # Afterwards the tournaments should be urls or the subdomain-name
    
    # open the file, ensuring a file exists 
    while(True):
        fileToOpen = input("Designate the file to open: ")
        
        try:
            file = open(fileToOpen, 'r')
            break
        except:
            print("File not found or cannot be opened")
    
    # prepare output file, erasing previous entries
    outputFile = open("output.txt", "w")
    outputFile.write("")
    outputFile.close()
            
    # Create the list of tournaments to process
    file = file.read()  
    file = file.splitlines()
    
    # Pop the api key
    apiKey = file.pop(0)
    
    # Process the data for each tournament
    # This could error correct if the tournament name was copy/pasted wrong
    # Ill fix this later in the third version or some shit
    # Make sure the tournaments exist
    # Insert name as <host-name>
    iteration = 1
    for tournament in file:
        players = getParticipants(tournament, apiKey)
        matches = getMatches(tournament, apiKey)
        date = getDate(tournament,apiKey) 
        outputScores(players, matches, date, iteration)
        print(tournament, "values computed")
        iteration+= 1
    
    
    
    
    
            
main()
    
#players = getParticipants()
#matches = getMatches()
#date = getDate()

#print(players)
#print(matches)
#outputScores(players, matches, date)


