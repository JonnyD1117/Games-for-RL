from card_game_mechanics import CardGameMechanics

import re


class Player(CardGameMechanics):

    def __init__(self, number_of_players=2, numberofDecks=1):
        super().__init__()

        self.dealer_index = 0
        self.dealer_score_thres = 17

        self.type_to_score_dict = {'A': (1, 11), '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   '10': 10, 'J': 10, 'Q': 10, 'K': 10}

        self.episode_player_score = {i: [] for i in range(number_of_players)}
        self.total_player_score = self.episode_player_score

        self.compute_initial_score()

    def hit(self, player):
        print("Score before HIT", self.episode_player_score)
        self.pull(player, 1)  # Player get dealt a card by dealer
        self.score(player)  # Player Score is computed

        print("Score after HIT", self.episode_player_score)

    def stick(self, player):
        pass

    def compute_initial_score(self):
        for player in range(self.num_players):
            score_list = []
            for card_ind in self.player_states[player]:
                card_type = self.card_to_type[card_ind]
                score_list.append(self.type_to_score(card_type))

            self.episode_player_score[player] = score_list

    def score(self, player):
        # Computes the Score for ALL Players in the game
        # for player in range(self.num_players):
        score_list = []
        for card_ind in self.player_states[player]:
            card_type = self.card_to_type[card_ind]
            score_list.append(self.type_to_score(card_type))

        self.episode_player_score[player] = score_list

    def type_to_score(self, type_of_card):
        """
        This function accepts the "type" of card (Ace of Spades...etc) and converts the type to a numerical score
        :param type_of_card: String
        :return: the corresponding score for the type of card input
        """

        prefix = type_of_card

        if prefix[0] == 'J' or prefix[0] == 'A' or prefix[0] == 'K' or prefix[0] == 'Q':
            output_str = re.findall("[^_SDHC]", str(prefix))

        elif prefix[0] == '1' and prefix[1] == '0':
            output_str = re.findall("[0-9][0-9]", str(prefix))
        else:
            output_str = re.findall("[0-9]", str(prefix))

        return self.type_to_score_dict[output_str[0]]



class BlackJack(Player):

    def __init__(self):
        super().__init__(self, number_of_games=5, number_of_decks=1, number_of_players=2)


















    def run_game(self):

        pass



if __name__ == '__main__':

    game = BlackJack()

    game.hit(player=1)
    game.hit(player=1)
    game.hit(player=0)
    game.hit(player=1)
    game.hit(player=1)




