import RankingFunctions


def main():

    while(True):
        choice = input("Enter n to create new rankings, u to update existing: ")
        choice = choice.lower()
        if choice == "n":
            rankingDict = {}
            break
        elif choice == "u":
            rankingDict = RankingFunctions.getRankings()
            break

    apiKey = input("Enter api key: ")

    while(True):

        choice = input("Enter 'a' to add a tournament\nEnter 'm' to add multiple tournaments(and update in between)\nEnter 'u' to update rankings\nEnter 'un' to update (non-decay)\nEnter 'o' to output rankings\nEnter 'p' to print rankings\nEnter 'q' to quit: ")

        choice = choice.lower()
        if choice == "a":
            RankingFunctions.getTournament(rankingDict, apiKey)
        elif choice == "m":
            RankingFunctions.getTournament(rankingDict, apiKey, 1)
        elif choice == "u":
            RankingFunctions.updateRankings(rankingDict, 0)
        elif choice == "un":
            RankingFunctions.updateRankings(rankingDict, 1)
        elif choice == "o":
            RankingFunctions.outputRankings(rankingDict)
        elif choice == "p":
            RankingFunctions.printRankings(rankingDict)
        elif choice == "d":
            RankingFunctions.outputDisplayRankings()
        elif choice == "q":
            break

main()
