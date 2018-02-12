
class Player:
    VERSION = "TOP STRATEGY RUSSIAN BOT"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Rafa El Diablo":
                card1 = player["hole_cards"][0]["rank"]
                card2 = player["hole_cards"][1]["rank"]
                if card1 == card2:
                    return 1000
                elif (card1 in "AKQJ98" or card1 == "10") and (card2 in "AKQJ98" or card2 == "10"):
                    return 1000
        return 0

    def showdown(self, game_state):
        pass

