"""
WAR CARD GAME
"""
from random import shuffle

color=("Spades","Hearts","Clubs","Diamonds")
figures=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
cards_and_values={'Two':2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,\
"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card():
    """
    Class CARD
    """
    def __init__(self,color_card,figure):
        self.color_card=color_card
        self.figure=figure
        self.value = cards_and_values[figure]#value of card,the higher card has higher the value

    def __str__(self):
        return f"{self.figure} {self.color_card}"

    def __repr__(self):
        return self.__str__()

class Deck():
    """
    CLASS DECK
    """
    def __init__(self):
        self.all_of_cards =[]
    #how many cards are in the deck
    def __len__(self):
        """
        how many cards are in the deck
        """
        return len(self.all_of_cards)

    def create_deck_cards(self):
        """
        create deck
        """
        for color_card in color :
            for card_figure in figures:
                new_card=Card(color_card,card_figure)
                self.all_of_cards.append(new_card)

    def shuffle(self):
        """
        shuffle deck
        """
        shuffle(self.all_of_cards)

class Player():
    """
    CLASS PLAYER
    """
    def __init__(self,name):
        self.name=name
        self.cards=[]

    def __str__(self):
        return f"Player {self.name} has {len(self.cards)}"

    def add_cards(self,new_cards):
        """
        add cards to player's deck
        """
        if isinstance(new_cards,type([])):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove_cards(self,card_number):
        """
        remove cards from player's deck
        """
        del self.cards[0:card_number+1]

def main():
    """
    main function
    """
    player_one=Player("One")#create player
    player_two=Player("Two")#create player
    deck=Deck()#create Deck
    deck.create_deck_cards()#create deck_of_cards
    deck.shuffle()#shuffle deck
    player_one.cards=deck.all_of_cards[:26]#split deck
    player_two.cards=deck.all_of_cards[26:53]#split deck
    print("Start a game:")
    game_on=True
    war_round=1

    #GAME START
    while game_on:#check game on
        #Check player one's deck is empty
        #Win player 1
        if len(player_one.cards)==0:
            print("Congratulions. Win player 2")
            break
        #Check player second's deck is empty
        #Win player 1
        if len(player_two.cards)==0:
            print("Congratulions. Win player 1")
            break

        print(f"{war_round} round")

        card_index=0
        #if first player's card is equal to second player's card
        #there is war and check next cards until if any of player win round
        #counter is incremented by 2,because we check every second card
        while card_index<26:
                #Battle
            if card_index>=2:#if value of player one's cards is equal to value of player two a draw, it will be War
                print("War")
            if player_one.cards[card_index].value > player_two.cards[card_index].value: #if player one's card is better than player two's card
                player_one.remove_cards(card_index+1)
                player_two.remove_cards(card_index+1)
                player_one.add_cards(player_one.cards[:card_index+1])
                player_one.add_cards(player_two.cards[:card_index+1])
                print(f"Win player 1 in the {war_round} round")
                break
            elif player_one.cards[card_index].value < player_two.cards[card_index].value:#if player two's card is better than player one's card
                player_one.remove_cards(card_index+1)
                player_two.remove_cards(card_index+1)
                player_two.add_cards(player_two.cards[:card_index+1])
                player_two.add_cards(player_one.cards[:card_index+1])
                print(f"Win player 2 in the {war_round} round")
                break
            else:#if there is draw
                #check how cards player one has
                #if he has less than 3 cards,he loses
                if len(player_one.cards)<3:
                    print("Player One unable to declare war")
                    print("Congratulions. Win player 2")
                    game_on=False
                    break
                #check how cards player two has
                #if he has less than 3 cards,he loses
                elif len(player_two.cards)<3:
                    print("Player Two unable to declare war")
                    print("Congratulions. Win player 1")
                    game_on=False
                    break
                #if players have more than 3 cards
                #they will take next cards and check again
                else:
                    card_index+=2
                    continue
        war_round+=1

main()
