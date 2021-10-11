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

    def remove_card(self):
        return self.cards.pop(0)

    def remove_cards(self,x):
         del self.cards[0:x+1]
        
    
def main():
    #create players
    player_one=Player("One")
    player_two=Player("Two")
    
    #new Deck
    deck=Deck()

    #create deck_of_cards
    deck.create_deck_cards()

    #shuffle deck
    deck.shuffle()
    #split deck
    player_one.cards=deck.all_of_cards[:26]
    player_two.cards=deck.all_of_cards[26:53]
    print("Start a game :")
    game_on=True
    round=1
    #GAME START
    #check game on
    while game_on==True:
        #Check player 1 deck is empty
        if len(player_one.cards)==0:
            print("Congratulions. Win player 2")
            break
        #Check player 2 deck is empty
        if len(player_two.cards)==0:
            print("Congratulions. Win player 1")
            break

        print(f"{round} round") 
        
        x=0
        #if  first player's card is equal to second player's cards
        #is war and we check next cards until if any of player's win round
        #counter is incremented by 2,because we check every second card
        while x<26:
            #Battle
            #If there is a draw, it is War
            if x>=2:
                print("War")
            #if player 1 card is better than player two card
            if player_one.cards[x].value > player_two.cards[x].value:
                player_one.remove_cards(x+1)
                player_two.remove_cards(x+1)
                player_one.add_cards(player_one.cards[:x+1])
                player_one.add_cards(player_two.cards[:x+1])
                print(f"Win player 1 in the {round} round")
                break
            #if player 1 card is better than player two card
            elif player_one.cards[x].value < player_two.cards[x].value:
                player_one.remove_cards(x+1)
                player_two.remove_cards(x+1)
                player_two.add_cards(player_two.cards[:x+1])
                player_two.add_cards(player_one.cards[:x+1])
                print(f"Win player 2 in the {round} round")
                break
            #if player 1 card is better than player two card
            else:
                if len(player_one.cards)<3:
                    print("Player One unable to declare war")
                    print(f"Congratulions. Win player 2")
                    game_on=False
                    break
                elif len(player_two.cards)<3:
                    print("Player Two unable to declare war")
                    print(f"Congratulions. Win player 1")
                    game_on=False
                    break 
                else:
                    x+=2  
                    continue
        round+=1


main()