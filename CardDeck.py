import random



class DeckOfCards:
    def __init__(self, num_decks=1, num_players=2, init_shuffle=True, num_init_shuffle=3):

        # Initialization Parameters 
        self.num_decks = num_decks
        self.num_players = num_players
        self.num_init_shuffle = num_init_shuffle


        # Create Initial Deck of Cards 
        self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.card_values = {'ACE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8,
                            'NINE': 9, 'TEN': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13}

        self.new_deck = self.create_new_deck()
        self.new_deck_index = [i for i in range(1,53)]

        self.current_deck = self.new_deck
        self.current_deck_index = self.new_deck_index


        # Initial Deck Shuffle 
        if init_shuffle:

            self.init_shuffle_deck()

        else: 
            pass 


    def create_new_deck(self):
        unshuffled_deck = {}
        count = 1
        for suit in self.suits:
            for card in self.card_values:

                unshuffled_deck[count]= (card, suit)
                count += 1
        return unshuffled_deck

    def create_deck_from_index(self, new_indexing):

        new_deck = {} 

        for card_index in new_indexing:
            new_deck[card_index] = self.new_deck[card_index]

        return new_deck


    def init_shuffle_deck(self):

        shuffled_index = self.current_deck_index

        for _ in range(self.num_init_shuffle):

            random.shuffle(shuffled_index)

        self.current_deck = self.create_deck_from_index(shuffled_index)
        self.current_deck_index = shuffled_index

        
    def shuffle_dec(self):

        shuffled_index = self.current_deck_index
        random.shuffle(shuffled_index)

        self.current_deck = self.create_deck_from_index(shuffled_index)
        self.current_deck_index = shuffled_index

    def deal_card(self):
        
            


    def draw_card(self):
        pass

    def discard_card(self):
        pass

    def print_thing(self):
        print(self.current_deck_index)


d = DeckOfCards()
d.print_thing()