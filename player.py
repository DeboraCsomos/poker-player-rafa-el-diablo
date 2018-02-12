
class Player:
    VERSION = "TOP STRATEGY RUSSIAN BOT"

    def betRequest(self, game_state):
        current_buyin = game_state["current_buy_in"]
        min_raise = game_state["minimum_raise"]
        big_blind = game_state["small_blind"] * 2
        community_cards = game_state["community_cards"]
        for player in game_state["players"]:
            if player["name"] == "Rafa El Diablo":
                card1 = player["hole_cards"][0]["rank"]
                card2 = player["hole_cards"][1]["rank"]
                if card1 == card2:
                    if card1 in "AKQJ":
                        return current_buyin - player["bet"] + min_raise * 2
                    return current_buyin - player["bet"] + min_raise
                elif len(community_cards) > 0:
                    for card in community_cards:
                        if not (card["rank"] == card1 or card["rank"] == card2):
                            return 0
                if (card1 in "AKQJ98" or card1 == "10") and (card2 in "AKQJ98" or card2 == "10"):
                    return current_buyin - player["bet"]
                elif (card1 == "A" and card2 in "12345") or (card2 == "A" and card1 in "12345"):
                    return current_buyin - player["bet"]
        return 0

    def showdown(self, game_state):
        pass

