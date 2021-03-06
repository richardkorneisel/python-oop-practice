#
# Instructions:
# Work through the following prompts. Prompts marked with "We Do", we will work
# on together, as a class; prompts marked with "You Do", you will be given time
# to work through on your own.
#
# Tip: comment out your solution to each prompt before moving on to the next
# one! This will keep your console clear.
#

#
# Prompt 1: We Do
#
# Define a class for a Car. Your Car class should have the following
# properties:
#
#    - make
#    - model
#    - color
#
# class Car:
#     def __init__(self, make, model, color):
#        self.make = make
#        self.model = model
#        self.color = color
   
#     def __str__(self):
#        return f"{self.make} {self.model} {self.color}"
   
#     def drive(self):
#        return 'vroom vroom'
        
# car = Car('chevy', 'nova', 'gray')
# print(car)
# print(car.drive())
      
# Your Car class should have the following methods:
#
#    - drive: print 'vroom vroom' to the console
#
# Once you create your class definition create two instances.
#

#
# Prompt 2: We Do
#
# We're going to modify our Car class from the previous prompt and extend it to
# create a Toyota class:
#
#   - Extend your Car class to create a Toyota class. The make property will always
#     be 'Toyota'. Add a drive method to your Toyota class.
#
# Make an instance of your Toyota class.
#
# class Toyota(Car):
#     def __init__(self, make, model, color):
#        super().__init__('Toyota', model, color)
   
#     def drive(self):
#        return ('run run')
        
# toyota = Toyota('toyota', 'new', 'cherry red')
# print(toyota)
# print(toyota.drive())
#
# Prompt 3: You Do
#
# Define a class for your favorite animal (dog, cat, giraffe, etc). Give your
# class 3 attributes and two methods.
#
# After you've defined your class, create 3 instances.
#
# class Cougar:
#     def __init__(self, name, genus, species):
#         self.name = name
#         self.genus = genus
#         self.species = species
#     def __str__(self):
#        return f"{self.name} {self.genus} {self.species}"
   
#     def sound(self):
#        return 'roar or scream'
        
# cat = Cougar('Cougar', 'Felis', 'Concolor')
# print(cat)
# print(cat.sound())
# Prompt 4: You Do
#
# Once we've completed the above, work through the following changes to your
# Car and Toyota classes:
#
#   - move the color property to your Toyota class
#   - move the drive method to your Car class
#   - add a property to your Toyota class
#   - add a property to your Car class and "fill it in" for your Toyota class
#
class Car:
    def __init__(self, make, model, weight):
       self.make = make
       self.model = model
       self.weight = weight
   
    def __str__(self):
       return f"{self.make} {self.model} {self.weight}"
   
    def drive(self):
       return 'vroom vroom'
        
car = Car('chevy', 'nova', '2000 lbs')
#print(car)
#print(car.drive())

class Toyota(Car):
    def __init__(self, model, weight, color, engine, make='Toyota'):
        super().__init__(make, model, weight)
        self.color = color
        self.engine = engine
    
    def __str__(self):
       return f"{self.make} {self.model} {self.weight} {self.color} {self.engine}"
   
    # def drive(self):
    #    return ('run run')
   
    # def fuel_economy(self):
    #     return ('34 mpg')
        
toyota = Toyota('corolla', '2000 lbs','cherry red', '4L')
#print(toyota)
#print(toyota.drive())

#
# Prompt 5: You Do
#
# Define and Animal class with the following properties and methods:
#
#   - group (Invertebrates, Fish, Amphibians, Reptiles, Birds, and Mammals)
#   - eat: log "yum yum" to the console
#   - sleep: log "zzzzz" to the console
#
# Modify your animal from the previous prompt so that it extends your new
# Animal class.
#
# Create an instance of your animal class (the one that extends the Animal
# class).
#
class Cougar:
    def __init__(self, name, genus, species):
        self.name = name
        self.genus = genus
        self.species = species
    def __str__(self):
       return f"{self.name} {self.genus} {self.species}"
   
    def sound(self):
       return 'roar or scream'
        
cat = Cougar('Cougar', 'Felis', 'Concolor')
#print(cat)
#print(cat.sound())

class Animal(Cougar):
    def __init__(self, name, genus, species, group):
        super().__init__(name, genus, species)
        self.group = group
    
    def __str__(self):
       return f"{self.name} {self.genus} {self.species} {self.group}"
    
    def eat(self):
       return 'Yum Yum'
    
    def sleep(self):
       return 'zzzzz'
    
animal = Animal('Cougar', 'Felis','Concolor', 'Mammal')
print(animal)
print(animal.eat())
print(animal.sleep())   
    
#
# Prompt 6: You Do
#
# Define a Card class with the following properties:
#
#   - suit (hearts, spades, clubs, diamonds)
#   - rank (Ace, 2, 3, 4, .. Jack, King, Queen)
#   - score (1, 2, 3, 4, ... 11, 12, 13)
#
# Define a Deck class with the following properties and methods:
#
#   - length (the number of cards - should start at 52)
#   - cards (an array of cards in the deck)
#   - draw: return a random card from the cards array
import random

class Card:                                  
    def __init__ (self, suit, score, rank): #, score
        self.suit = suit
        self.score = score
        self.rank = rank
        
        
    def show(self):
        print ("{} of {} rank {}".format(self.rank, self.suit, self.score+2))

#card= Card('Card', 6)
#card.show()
                                                
class Deck:
    def __init__ (self): 
        self.cards = []
        self.build()
      
    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            #for r in range(1, 14):
            for sc, r in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace"]):
                self.cards.append(Card(s, sc, r))
    def show(self):
        for c in self.cards:
            c.show()
  
#deck = Deck()
#deck.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

# deck = Deck()
# deck.shuffle()
# deck.show()

    def drawCard(self):
        return self.cards.pop()
    
deck = Deck()
deck.shuffle()

card = deck.drawCard()
card.show()

            
#       const values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"];
#       var cards = [];                               // creating an array to store cards
#         for(let i=0; i<suits.length; i++) {         // nested for loop.  Loop of ranks inside loop of suits. 
#           for(let j=0; j<values.length; j++) {
#             var newCard = new Card (suits[i], values[j], j)  //create card suit, then value, then rank.
#             cards.push(newCard);
#           }
#         }
#       this.length = cards.length                       //referencing the length of the cards array
#       this.cards = cards                               //defining the cards property as the array
#       }
# When you create an instance of your Deck class (i.e. in your constructor),
# fill in the cards array with 52 instances of your Card class. You can do
# this with a nested for loop - first loop through an array of all possible
# suits, then loop through an array of all possible ranks. Inside your inner
# loop, create an instance of your Card class and push it into the Deck's cards
# array.
#
# Instantiate an instance of your Deck and start drawing random cards!
#
