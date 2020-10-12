import random
import numpy as np 



class DeckOfCards:
    def __init__(self, num_decks=1, num_players=2, num_card_per_player=5, init_shuffle=True, num_init_shuffle=3):

        # Initialization Parameters 
        self.num_decks = num_decks
        self.num_players = num_players
        self.num_init_shuffle = num_init_shuffle
        self.num_card_per_player = num_card_per_player

        self.player_state = self.create_empty_player_state()


        # Create Initial Deck of Cards 
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.card_values = {'ACE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8,
                            'NINE': 9, 'TEN': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13}

        self.new_deck = self.create_new_deck()
        self.new_deck_index = [i for i in range(1,len(self.new_deck)+1)]

        self.current_deck = self.new_deck
        self.current_deck_index = self.new_deck_index

        self.running_deck = self.current_deck
        self.running_deck_index = self.current_deck_index


        # Initial Deck Shuffle 
        if init_shuffle:

            self.init_shuffle_deck()

        else: 
            pass 

    def create_empty_player_state(self):

        player_state = [ [] for i in range(self.num_players)]

        return player_state

    def create_new_deck(self):
        unshuffled_deck = {}
        count = 1

        for num_deck in range(self.num_decks):
            for suit in self.suits:
                for card in self.card_values:

                    unshuffled_deck[count]= (card, suit)
                    count += 1
        return unshuffled_deck

    def create_deck_from_index(self, new_indexing):

        new_deck_dict = {} 

        for card_index in new_indexing:
            new_deck_dict[card_index] = self.current_deck[card_index]

        return new_deck_dict

    def init_shuffle_deck(self):

        shuffled_index = self.current_deck_index[:]

        for _ in range(self.num_init_shuffle):

            random.shuffle(shuffled_index)

        self.running_deck = self.create_deck_from_index(shuffled_index)
        self.running_deck_index = shuffled_index

    def shuffle_deck(self):

        shuffled_index = self.current_deck_index[:]
        random.shuffle(shuffled_index)

        self.current_deck = self.create_deck_from_index(shuffled_index)
        self.current_deck_index = shuffled_index

    def deal_cards(self):

        index_cp = self.running_deck_index[:]

        for num_card in range(self.num_card_per_player):
            for player in range(self.num_players):

                card_index = index_cp[0]

                self.player_state[player].append(card_index)

                index_cp.remove(card_index)

                self.running_deck = self.create_deck_from_index(index_cp)
                self.running_deck_index = index_cp
                
    def draw_card(self, player, num_cards_drawn):

        for _ in range(num_cards_drawn):
            card_index = self.running_deck_index[0]

            self.player_state[player].append(card_index)

            self.running_deck_index.remove(card_index)
            self.running_deck = self.create_deck_from_index(self.running_deck_index)

    def discard_card(self, player, num_cards_disc, specifc_discard=None):

        if specifc_discard is not None:
            raise("Not Implement Yet")

        else:
            #Discard Last Cards in the Hand

        
            for _ in range(num_cards_disc):
                card_index = self.player_state[player][-1]

                self.player_state[player].remove(card_index)

                self.running_deck_index.append(card_index)
                self.running_deck = self.create_deck_from_index(self.running_deck_index)

    def discard_and_draw(self, player, num_disc, num_drawn):
        pass



d = DeckOfCards(num_card_per_player=5, num_players=5, num_decks=2)

print(d.new_deck_index)
print(len(d.running_deck_index))
print(d.running_deck_index)

d.deal_cards()

print(d.running_deck_index)


print(len(d.running_deck_index))

print(d.new_deck_index)





class BlackJack(DeckOfCards):

    def __init__(self):
        super(BlackJack).__init__()

        pass
    def hit(self, player):
        pass
    def stick(self, player):
        pass




