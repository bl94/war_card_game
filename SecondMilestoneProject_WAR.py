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
    #Create players
    player_one=Player("One")
    player_two=Player("Two")
    
    #New Deck
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
    while game_on==True:
        if len(player_one.cards)==0:
            print("Congratulions. Win player 2")
            break
        if len(player_two.cards)==0:
            print("Congratulions. Win player 1")
            break
        print(f"{round} round") 

        #Battle
        if player_one.cards[0].value > player_two.cards[0].value:
            win_cards=[]
            win_cards.append(player_one.cards[0])
            win_cards.append(player_two.cards[0])
            player_one.remove_card()
            player_two.remove_card()
            player_one.add_cards(win_cards)
            print(f"Win player 1 the {round} round")

        elif player_one.cards[0].value < player_two.cards[0].value:
            win_cards=[]
            win_cards.append(player_two.cards[0])
            win_cards.append(player_one.cards[0])
            player_one.remove_card()
            player_two.remove_card()
            player_two.add_cards(win_cards)
            print(f"Win player 2 the {round} round")

        else:
            if len(player_one.cards)<3:
                print("Player One unable to declare war")
                print(f"Congratulions. Win player 2")
                break

            elif len(player_two.cards)<3:
                print("Player Two unable to declare war")
                print(f"Congratulions. Win player 1")
                break

            else:  
                for x in range(2,52,2):
                    if player_one.cards[x].value > player_two.cards[x].value:
                        print("War")
                        win_cards=[]
                        win_cards.extend(player_one.cards[0:x+1])
                        win_cards.extend(player_two.cards[0:x+1])
                        player_one.remove_cards(x+1)
                        player_two.remove_cards(x+1)
                        player_one.add_cards(win_cards)
                        print(f"Win player 1 the {round} round")
                        break

                    elif player_one.cards[x].value < player_two.cards[x].value:
                        print("War")
                        win_cards=[]
                        win_cards.extend(player_two.cards[0:x+1])
                        win_cards.extend(player_one.cards[0:x+1])
                        player_one.remove_cards(x+1)
                        player_two.remove_cards(x+1)
                        player_two.add_cards(win_cards)
                        print(f"Win player 2 the {round} round")
                        break
                    else:
                        continue
        round+=1

list1=[1,2,3]
list2=
list1.extend(list2)
print(list1)
#main()