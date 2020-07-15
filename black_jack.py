#Step 1:Import the random module.This will be used to shuffle the deck prior.Then declare variables to store suits, ranks and values.
#Finally declare a Boolean value to be used to control while loops.

import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
#dictionary <--> values
playing True
#----------------------------------------------------------------------------------------------------------------------------------------

#Step 2:Consider making ''''''a card class'''''' where each '''Card object''' has a suit and a rank, then a Deck class to hold all 52 card objects,
#and can be shuffled(kağıtları karmak) and finally a Hand class that holds those Cards.
#A '''Card object''' really only needs two attributes:SUİT AND RANK.
#In addition to the Card's __init__method, consider adding a __str__ method that, when asked to print a Card, returns a string in the form
# "two of Hearts" 

class Card:
  
  def __init__(self,suit,rank):
    self.suit=suit
    self.rank=rank
    
  def __str__(self):
    return self.rank+" of "+self.suit
  
  #--------------------------------------------------------------------------------------------------------------------------------------
  
  
  #Step 3:'''''Create deck class'''''.(iskambil destesi).Here we might store 52 Card objects in a list that can later be shuffled.First, though 
  #we need to create 52 card objects and add them to our list.So long as(sürece) the Card class defn appears in our code, we can build Card objects
  #inside our Deck__init_method.Consider iterating over sequences of suits and ranks to build out each card.
  
  #for suit in suits:
       #for rank in ranks:
    
  # In addition to an __init__method, we will want to add '''methods''' to shuffle(karmak) our deck(deste).
  
  class Deck:
    
    def __init__(self):
        self.deck=[] # start with an empty list
        for suit in suits:
          for rank in ranks:
            self.deck.append(Card(suit,rank))
                    
    def __str__(self):     
        deck_composition=''  
        for card in self.deck:
           deck_composition+='\n'+card.__str__()
        return "the deck has:"+deck_composition
      
    def shuffle(self): #karmak
        random.shuffle(self.deck)
        
    def deal(self):    #dağıtmak
       single_card=self.deck.pop()
       return single_card
    
    
# now we can test it:

test_deck=Deck()
print(test_deck)

#output:
#The deck has:
#two of hearts, three of hearts, four of hearts.....

#--------------------------------------------------------------------------------------------------------------------------------------

#Step 4:''''''Create a hand class''''''.In addition to holding card objects dealt from the Deck, the Hand class may be used to calculate
#the value of those cards using the values dictionary defined above.it may also need to adjust for the value of Aces when appropriate.

class Hand:
  def __init__(self):
    self.cards=[]  #start with an empty list as we did in the Deck class
    self.value=0   #start with zero value
    self.aces=0    # add an attribute to keep track of aces
    
  def add_card(self,card):
     self.cards.append(card)
     self.value+=values[card.rank]
  #track aces
  if card.rank=='Ace':
    self.aces+=1
     
  def adjust_for_ace(self):
     while self.value >21 and self.aces:
           self.value -=10
           self.aces -= 1
   
  
  
 # test_deck=Deck()
 #test_deck.shuffle()
 #PLAYER
 #test_player=Hand()

#--------------------------------------------------------------------------------------------------------------------------------------

#Step 5: ''''Create a Chips Class''''.In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets 
#and ongoing winnings.This could be done using global variables, but in the spirit of object oriented programing, let's make a Chips class
#instead!

class Chips:
  def __init__(self,total=100):
      self.total=total #This can be set to a default value or supplied by a user input 
      self.bet=0
      
  def win_bet(self):
      self.total +=self.bet
      
  def lose_bet(self):
      self.total -=self.bet #iddia, bahis
#--------------------------------------------------------------------------------------------------------------------------------------

#function definitions= A lot of steps are going to be repetitive.That's where functions come in!The following steps are guidelines.add or
#remove functions as needed in your own program.

#Step 6:Write a function for taking bets.
  
    

    


            
      
      
        
      
      
      
      
  
  
  
  
  
  
