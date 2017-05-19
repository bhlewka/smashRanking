import RankingFunctions


def main():

    while():
        choice = input("Enter n to create new rankings, u to update existing: ")
        choice = choice.lower()
        if choice == "n":
            rankingDict = {}
            break
        elif choice == "u":
            rankingDict = RankingFunctions.getRankings()
            break

    while():
        choice = input("Enter a to add a tournament, u to update rankings, o to output rankings, or q to quit: ")
        choice = choice.lower()
        if choice == "a":
            RankingFunctions.getTournament(rankingDict)
        elif choice == "u":
            RankingFunctions.updateRankings(rankingDict)
        elif choice == "o":
            RankingFunctions.outputRankings(rankingDict)
        elif choice == "q":
            break
