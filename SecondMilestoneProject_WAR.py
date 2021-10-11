#Card
#Class
#Game
#Deck
#GameLogic


from random import shuffle

color=("Spades","Hearts","Clubs","Diamonds")
figures=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
cards_and_values={'Two':2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card():
    
    def __init__(self,color_card,figure):
        self.color_card=color_card
        self.figure=figure
        self.value = cards_and_values[figure]
    
    def __str__(self):
        return f"{self.figure} {self.color_card}"

my_Card = Card("Hearts","Ten")

print(my_Card.value)

class Deck():
    def __init__(self):
        self.all_of_cards =[]

    def __len__(self):
        return len(self.all_of_cards)

    def __str__(self):
        for x in self.all_of_cards:
            print(x)
        return ""

    def create_deck_cards(self):
        for x in color :
            for y in figures:
                new_card=Card(x,y)
                self.all_of_cards.append(new_card)

    def shuffle(self):
        shuffle(self.all_of_cards)

    def pop_deck_of_cards(self):
        return self.all_of_cards.pop()

class Player():
    def __init__(self,name):
        self.name=name
        self.cards=[]
    
    def __str__(self):
        return f"Player {self.name} has {len(self.cards)}"
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)
      
    def remove_cards(self):
        return self.cards.pop(0)
    
def main():
    #Create players
    player_one=Player("One")
    player_two=Player("Two")
    
    #New Deck
    deck=Deck()

    #create deck_of_cards
    deck.create_deck_cards()

    #shuffle deck
    deck.shuffle()
    print(deck)
    #split deck
    player_one.cards=deck.all_of_cards[:26]
    print(player_one)
    player_two.cards=deck.all_of_cards[26:53]
    print(player_two)

main()