
class Player:
    VERSION = "TOP STRATEGY RUSSIAN BOT"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Rafa El Diablo":
                card1 = player["hole_cards"][0]["rank"]
                card2 = player["hole_cards"][1]["rank"]
                if card1 == card2:
                    return 1000
                elif card1 in "AKQJ" or card2 == "AKQJ":
                    return 500
        return 400

    def showdown(self, game_state):
        pass

