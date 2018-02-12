
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print (game_state['current_buy_in'])
        return 1000

    def showdown(self, game_state):
        pass

