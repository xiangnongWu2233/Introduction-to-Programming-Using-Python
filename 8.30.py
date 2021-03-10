import random
class Card:
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        
    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

class Deck:
    
    suits=['\u2660','\u2661','\u2662','\u2663']

    ranks=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
    
    def __init__(self):
        self.cards=[]
        for i in Deck.suits:
            for j in Deck.ranks:
                self.cards.append(Card(i,j))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def dealCard(self):
        return self.cards.pop()

class Hand:
    
    def __init__(self,name):
        self.name=name
        self.cards=[]
        
    def addCard(self, card):
        self.cards.append(card)

    def showHand(self):
        print(self.name,':',end='')
        for i in range(len(self.cards)):
            print(' {:}{:}'.format(self.cards[i].rank,self.cards[i].suit),end='')
        print('')
        
    def countHand(self):
        self.count=0
        values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
        self.aces=0
        for i in self.cards:
            self.count+=values[i.rank]
            if i.rank=='A':
                self.aces+=1
        while self.count>21 and self.aces>0:
            self.aces-=1
            self.count-=10
            
        return self.count

class Game():

    deck=Deck()
    
    def __init__(self):
        
        self.house=Hand('House')
        self.player=Hand('You')

        Game.deck.shuffle()
        self.house.addCard(Game.deck.dealCard())
        self.player.addCard(Game.deck.dealCard())

        self.house.addCard(Game.deck.dealCard())
        self.player.addCard(Game.deck.dealCard())

        self.house.showHand()
        self.player.showHand()

        if self.Player()==0:
            if self.House()==0:
                self.result()

    def Player(self):
        while True:
            decision=input('Stand or Hit? (Enter s or h): ')
            while decision!='s' and decision!='h':
                print('Please re-enter the correct letter.')
                decision=input('Stand or Hit? (Enter s or h): ')
            if decision=='h':
                card=Game.deck.dealCard()
                print('You got {:}{:}'.format(card.getRank(),card.getSuit()))
                self.player.addCard(card)
                if self.player.countHand()>21:
                    print('You went over... You lose.')
                    return 1
            else:
                break
        return 0

    def House(self):
        while self.house.countHand()<17:
            card=Game.deck.dealCard()
            print('House got {:}{:}'.format(card.getRank(),card.getSuit()))
            self.house.addCard(card)
            if self.house.countHand()>21:
                print('House went over... You win.')
                return 1
        return 0

    def result(self):
        
        if self.player.countHand()>self.house.countHand():
            print('You win.')
        elif self.player.countHand()<self.house.countHand():
            print('You lose.')
        elif self.player.countHand()==21 and len(self.player.cards)==2<len(self.house.cards):
            print('You got Black Jack! You win.')
        elif self.house.countHand()==21 and len(self.house.cards)==2<len(self.player.cards):
            print('House got Black Jack! You lose.')
        else:
            print('Tie')

