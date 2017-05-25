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

    while(True):
        choice = input("Enter a to add a tournament, m to add multiple tournaments(and update in between), u to update rankings,\nun to update (non-decay), o to output rankings, p to print rankings, or q to quit: ")
        choice = choice.lower()
        if choice == "a":
            RankingFunctions.getTournament(rankingDict)
        elif choice == "m":
            RankingFunctions.getTournament(rankingDict,1)
        elif choice == "u":
            RankingFunctions.updateRankings(rankingDict, 0)
        elif choice == "un":
            RankingFunctions.updateRankings(rankingDict, 1)
        elif choice == "o":
            RankingFunctions.outputRankings(rankingDict)
        elif choice == "p":
            RankingFunctions.printRankings(rankingDict)
        elif choice == "d":
            RankingFunctions.outputDisplayRankings(rankingDict)
        elif choice == "q":
            break

main()