# Card Game Mechanics
##################################################
# This is the base class which supplied the basic mechanics of card games to other classes which are to inherit from
# this class. This is intended to be the base layer of a card game simulator.
##################################################
# Author: Jonathan Dorsey
# Credits: [{credit_list}]
# Version: 0.0.1
# Maintainer: Jonathan Dorsey
# Status: Testing
##################################################

import random


class CardGameMechanics:

    def __init__(self, number_decks=1, number_players=5, auto_init_shuffle=True, cards_per_player=2, auto_init_deal=True):

        # Deck of Cards is Stored as a list
        self.cards_per_deck = 52

        self.num_deck = number_decks
        self.card_per_player = cards_per_player
        self.num_players = number_players
        self.shuffled_deck = None
        self.discard_pile = []

        # Generate New Unshuffled Deck of Cards
        new_deck = [i for i in range(self.cards_per_deck*self.num_deck)]

        self.one_deck_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.one_deck_suits = ['_S', '_D', '_C', '_H']
        self.card_to_type = self.card_ind_to_type()

        # Shuffle Deck if AutoShuffle is Enabled
        if auto_init_shuffle:
            self.shuffled_deck = self.shuffle(new_deck, 3)
        else:
            self.shuffled_deck = new_deck

        self.running_deck = self.shuffled_deck

        # Player State Stored as a Dictionary given the player index
        self.player_states = {i: [] for i in range(self.num_players)}

        if auto_init_deal:
            for player in range(self.num_players):
                self.pull(player, self.card_per_player)

    def card_ind_to_type(self):
        ind_to_type = {}
        counter = 0
        for num_deck in range(self.num_deck):
            for suit in self.one_deck_suits:
                for rank in self.one_deck_ranks:

                    total_ind = counter
                    card_type = rank + suit
                    ind_to_type[total_ind] = card_type

                    counter += 1
        return ind_to_type

    @staticmethod
    def shuffle(current_deck_list, num_shuffles):
        """
        This function shuffles any list given to it after X number of shuffles operations on that list
        :param current_deck_list: The list to be shuffled
        :param num_shuffles: The number of times a shuffle operation is to be performed on the input list
        :return: The new shuffled list
        """

        for i in range(num_shuffles):
            random.shuffle(current_deck_list)
        return current_deck_list

    def burn_cards(self, num_cards_to_burn=1):
        """
        This function discards X number cards from the top of the running deck
        :param num_cards_to_burn:
        :return:
        """

        for _ in range(num_cards_to_burn):
            card_to_burn = self.running_deck.pop(0)
            self.discard_pile.append(card_to_burn)

    def discard(self, player_ind, num_cards, discard_indices=None):
        """
        :param player_ind: The dict index of the player
        :param num_cards: The number of cards the current player wishes to discard
        :param discard_indices: This is a list of the "deck" indices (in the currently players state)
                                which the player wishes to discard
        """

        # If no Card values are given to discard, the last card in the players hand will be discarded
        if discard_indices is None:

            player_state = self.player_states[player_ind]

            for _ in range(num_cards):

                discarded_deck_ind = player_state[-1]
                play_state_ind = player_state.index(discarded_deck_ind)
                player_state.pop(play_state_ind)

                self.discard_pile.append(discarded_deck_ind)

            self.player_states[player_ind] = player_state

        elif discard_indices is not None:

            player_state = self.player_states[player_ind]
            player_state = [x for x in player_state if x not in discard_indices ]

            self.player_states[player_ind] = player_state

    def pull(self, player_ind, num_pull_cards):
        """
        :param player_ind: The dict index of the player performing the action
        :param num_pull_cards: The number of cards the player wishes to pull from the deck
        """

        # Initialize Locally Scoped Player State
        player_state = self.player_states[player_ind]

        # Iterate Through number of cards "PULLed" from the running deck
        for _ in range(num_pull_cards):
            pull_card_ind = self.running_deck[0]
            player_state.append(pull_card_ind)

            self.running_deck.remove(self.running_deck[0])

        self.player_states[player_ind] = player_state

    def discard_and_pull(self, player_ind, num_discard, num_pull, discard_ind=None):
        """
        :param player_ind: The dict index of the player performing the action
        :param num_discard: The number of cards the player wishes to discard
        :param num_pull: The number of cards the player wishes to pull from the deck
        :param discard_ind: This is a list of the "deck" indices (in the currently players state)
                            which the player wishes to discard
        """

        self.discard(player_ind, num_discard, discard_ind)
        self.pull(player_ind, num_pull)




