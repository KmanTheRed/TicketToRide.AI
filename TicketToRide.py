import random
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class TicketToRideDeck:
    def shuffleDeck(self, drawPile):
      random.shuffle(drawPile)
      self.train_car_cards = drawPile
    def __init__(self):
        # Initialize the train car deck with a list of cards
        self.train_car_cards = ["Red", "Yellow", "Green", "Blue", "Pink", "Black", "White", "Orange", "Rainbow"] * 12 + ["Rainbow","Rainbow"]
        # Shuffle the deck initially
        self.shuffleDeck(self.train_car_cards)
    def seeTopFive(self):
        for i in range(5):
            print(self.train_car_cards[i])
    def takeCards(self, j, k):
        #variables j and k specify the type of draw
        if(j or k > 6 or j or k < 0):
            return []
        if len(self.train_car_cards) == 5:
            return []
        #if there are no more cards in the pile, you cannot draw!
        if len(self.train_car_cards) == 6:
            for card in self.train_car_cards[:5]:
                if card == "Rainbow":
                    self.train_car_cards.remove(card)
                    return [card]
            return []
        if(j == 6 and k == 6):
            newCards = [self.train_car_cards[5]]
            del self.train_car_cards[5]
            newCards.append(self.train_car_cards[5])
            del self.train_car_cards[5]
            return newCards
        if(j == 0 or k == 0):
            newCards = [self.train_car_cards[j+k-1]]
            return newCards
        newCards = [self.train_car_cards[j-1]]
        del self.train_car_cards[j-1]
        if(j < k):
            newCards.append(self.train_car_cards[k-2])
            del self.train_car_cards[k-2]
        else:
            newCards.append(self.train_car_cards[k-1])
            del self.train_car_cards[k-1]
class Player:
    def __init__(self):
        self.personalDeck = []
        self.personalRoutes = []
        self.personalTracks = []
        self.G = nx.Graph()
        self.cities = [
'Seattle', 'Portland', 'San Francisco', 'Los Angeles', 'Las Vegas', 'Salt Lake City',
'Helena', 'Duluth', 'Omaha', 'Denver', 'Kansas City', 'Oklahoma City', 'Dallas', 'Houston',
'El Paso', 'Santa Fe', 'Phoenix', 'Little Rock', 'Chicago', 'St. Louis', 'Pittsburgh',
'Nashville', 'Atlanta', 'Miami', 'New York', 'Boston', 'Montreal', 'Toronto', 'Sault Ste. Marie',
'Winnipeg',  'Raleigh', 'Washington', 'Charleston', 'New Orleans', 'Calgary', 'Vancouver']
        self.G.add_nodes_from(self.cities)
        self.trainCount = 45



      
class Routes:
    def __init__(self):
        self.route_points = {
    "Boston to Miami": 12,
    "Calgary to Phoenix": 13,
    "Calgary to Salt Lake City": 7,
    "Chicago to New Orleans": 7,
    "Chicago to Santa Fe": 9,
    "Dallas to New York": 11,
    "Denver to El Paso": 4,
    "Denver to Pittsburgh": 11,
    "Duluth to El Paso": 10,
    "Duluth to Houston": 8,
    "Helena to Los Angeles": 8,
    "Kansas City to Houston": 5,
    "Los Angeles to Chicago": 16,
    "Los Angeles to Miami": 20,
    "Los Angeles to New York": 21,
    "Montréal to Atlanta": 9,
    "Montréal to New Orleans": 13,
    "New York to Atlanta": 6,
    "Portland to Nashville": 17,
    "Portland to Phoenix": 11,
    "San Francisco to Atlanta": 17,
    "Sault St. Marie to Nashville": 8,
    "Sault St. Marie to Oklahoma City": 9,
    "Seattle to Los Angeles": 9,
    "Seattle to New York": 22,
    "Toronto to Miami": 10,
    "Vancouver to Montréal": 20,
    "Vancouver to Santa Fe": 13,
    "Winnipeg to Houston": 12,
    "Winnipeg to Little Rock": 11
}
        self.routes = [
    "Boston to Miami",
    "Calgary to Phoenix",
    "Calgary to Salt Lake City",
    "Chicago to New Orleans",
    "Chicago to Santa Fe",
    "Dallas to New York",
    "Denver to El Paso",
    "Denver to Pittsburgh",
    "Duluth to El Paso",
    "Duluth to Houston",
    "Helena to Los Angeles",
    "Kansas City to Houston",
    "Los Angeles to Chicago",
    "Los Angeles to Miami",
    "Los Angeles to New York",
    "Montréal to Atlanta",
    "Montréal to New Orleans",
    "New York to Atlanta",
    "Portland to Nashville",
    "Portland to Phoenix",
    "San Francisco to Atlanta",
    "Sault St. Marie to Nashville",
    "Sault St. Marie to Oklahoma City",
    "Seattle to Los Angeles",
    "Seattle to New York",
    "Toronto to Miami",
    "Vancouver to Montréal",
    "Vancouver to Santa Fe",
    "Winnipeg to Houston",
    "Winnipeg to Little Rock"
]
        random.shuffle(self.routes)
    def takeRoutes(self, choices):
        if(choices == 1):
          return [self.routes[0]]
        elif(choices == 2):
          return [self.routes[1]]
        elif(choices == 3):
          return [self.routes[2]]
        elif(choices == 4):
          return self.routes[0:1]
        elif(choices == 5):
          return self.routes[1:2]
        elif(choices == 6):
          return [self.routes[0], self.routes[2]]
        elif(choices == 7):
          return self.routes[0:2]
class Game:
    def __init__(self, num_players):
        self.gameEnd = False
        self.num_players = num_players
        self.players = [Player() for i in range(num_players)]
        self.order = 1
        #use order variable to designate which player's turn it will be 
        self.gameRoutes = Routes()
        self.gameDeck = TicketToRideDeck()
        self.gameBoard = Board()
        self.discardPile = []
    def Turn(self, choice, j, k, l):
        #Choice will either be draw cards, draw routes, or play cards
        if(choice == 1):
          self.players[self.order].personalDeck.extend(self.gameDeck.takeCards(j, k))
        elif(choice == 2):
          
          self.players[self.order].personalRoutes.extend(self.gameRoutes.takeRoutes(j))
        elif(choice == 3):
          self.players[self.order].trainCount -= (j + k)
          #when the player gets less than 2 trains mark the end of the game, and the loop will break
          if(self.players[self.order].trainCount <= 2):
            self.gameEnd == True
          #play cards means j = number of cards, k = number of rainbows, l = color
          for i in range(j):
            self.players[self.order].personalDeck.remove(l)
          for p in range(k):
            self.players[self.order].personalDeck.remove("Rainbow")
          self.discardPile += [l] * j + ["Rainbow"] * k
        elif(choice == 4):
          print("Player has forfeighted turn!")
        if(self.order == self.num_players):
            self.order = 1
        else:
            self.order += 1



class Board:
    def __init__(self):
        self.G = nx.Graph()
        self.cities = [
    'Seattle', 'Portland', 'San Francisco', 'Los Angeles', 'Las Vegas', 'Salt Lake City',
    'Helena', 'Duluth', 'Omaha', 'Denver', 'Kansas City', 'Oklahoma City', 'Dallas', 'Houston',
    'El Paso', 'Santa Fe', 'Phoenix', 'Little Rock', 'Chicago', 'St. Louis', 'Pittsburgh',
    'Nashville', 'Atlanta', 'Miami', 'New York', 'Boston', 'Montreal', 'Toronto', 'Sault Ste. Marie',
    'Winnipeg',  'Raleigh', 'Washington', 'Charleston', 'New Orleans', 'Calgary', 'Vancouver']
        self.G.add_nodes_from(self.cities)
        self.edges = [
          ('Vancouver', 'Seattle', {'color': 'Gray', 'length': 1}),
          ('Vancouver', 'Seattle', {'color': 'Gray', 'length': 1}), #Second Gray track
          ('Seattle', 'Portland', {'color': 'Gray', 'length': 1}),     
          ('Seattle', 'Portland', {'color': 'Gray', 'length': 1}),  # Second gray track
          ('Portland', 'San Francisco', {'color': 'Green', 'length': 5}),
          ('Portland', 'San Francisco', {'color': 'Pink', 'length': 5}),
          ('Los Angeles', 'Phoenix', {'color': 'Gray', 'length': 3}),
          ('Phoenix', 'Santa Fe', {'color': 'Gray', 'length': 3}),
          ('Santa Fe', 'Denver', {'color': 'Gray', 'length': 2}),
          ('Denver', 'Omaha', {'color': 'Pink', 'length': 4}),
          ('Omaha', 'Chicago', {'color': 'Blue', 'length': 4}),
          ('Las Vegas', 'Salt Lake City', {'color': 'Orange', 'length': 3}),
          ('Salt Lake City', 'Helena', {'color': 'Pink', 'length': 3}),
          ('Helena', 'Winnipeg', {'color': 'Blue', 'length': 4}),
          ('Winnipeg', 'Sault Ste. Marie', {'color': 'Gray', 'length': 6}),
          ('Los Angeles', 'San Francisco', {'color': 'Pink', 'length': 3}),
          ('Los Angeles', 'San Francisco', {'color': 'Yellow', 'length': 3}),
          ('San Francisco', 'Salt Lake City', {'color': 'Orange', 'length': 5}),
          ('San Francisco', 'Salt Lake City', {'color': 'White', 'length': 5}),
          ('Montreal', 'Boston', {'color': 'Gray', 'length': 2}),
          ('Montreal', 'Boston', {'color': 'Gray', 'length': 2}), #second
          ('Montreal', 'New York', {'color': 'Blue', 'length': 3}),
          ('Los Angeles', 'El Paso', {'color': 'Black', 'length': 6}),
          ('El Paso', 'Houston', {'color': 'Green', 'length': 6}),
          ('Houston', 'New Orleans', {'color': 'Gray', 'length': 2}),
          ('New Orleans', 'Miami', {'color': 'Red', 'length': 6}),
          ('Miami', 'Charleston', {'color': 'Pink', 'length': 4}),
          ('Washington', 'New York', {'color': 'Black', 'length': 2}),
          ('Washington', 'New York', {'color': 'Orange', 'length': 2}),
          ('New York', 'Boston', {'color': 'Yellow', 'length': 2}),
          ('New York', 'Boston', {'color': 'Red', 'length': 2}),
          ('Seattle', 'Calgary', {'color': 'Gray', 'length': 4}),
          ('Calgary', 'Winnipeg', {'color': 'White', 'length': 6}),
          ('Sault Ste. Marie', 'Montreal', {'color': 'Black', 'length': 5}),
          ('Duluth', 'Sault Ste. Marie', {'color': 'Gray', 'length': 3}),
          ('Sault Ste. Marie', 'Toronto', {'color': 'Gray', 'length': 2}),
          ('Toronto', 'Chicago', {'color': 'White', 'length': 4}),
          ('Calgary', 'Vancouver', {'color': 'Gray', 'length': 3}),
        ('Calgary', 'Seattle', {'color': 'Gray', 'length': 4}),
        ('Seattle', 'Helena', {'color': 'Yellow', 'length': 6}),
        ('Helena', 'Duluth', {'color': 'Orange', 'length': 6}),
        ('Helena', 'Denver', {'color': 'Green', 'length': 4}),
        ('Helena', 'Omaha', {'color': 'Red', 'length': 5}),
        ('Portland', 'Salt Lake City', {'color': 'Blue', 'length': 6}),
        ('Calgary', 'Helena', {'color': 'Gray', 'length': 4}),
        ('Winnipeg', 'Duluth', {'color': 'Black', 'length': 4}),
        ('Duluth', 'Toronto', {'color': 'Pink', 'length': 6}),
        ('Duluth', 'Omaha', {'color': 'Gray', 'length': 2}),
        ('Duluth', 'Omaha', {'color': 'Gray', 'length': 2}), #secondGrayRoute
        ('Duluth', 'Chicago', {'color': 'Red', 'length': 3}),
        ('Toronto', 'Pittsburgh', {'color': 'Gray', 'length': 3}),
        ('Toronto', 'Montreal', {'color': 'Gray', 'length': 3}),
        ('Salt Lake City', 'Denver', {'color': 'Red', 'length': 3}),
        ('Salt Lake City', 'Denver', {'color': 'Yellow', 'length': 3}),
        ('Denver', 'Kansas City', {'color': 'Black', 'length': 4}),
        ('Denver', 'Kansas City', {'color': 'Orange', 'length': 4}),
        ('Kansas City', 'Saint Louis', {'color': 'Blue', 'length': 2}),
        ('Kansas City', 'Saint Louis', {'color': 'Pink', 'length': 2}),
        ('Omaha', 'Kansas City', {'color': 'Gray', 'length': 1}),
        ('Omaha', 'Kansas City', {'color': 'Gray', 'length': 1}), #second route
        ('Chicago', 'Saint Louis', {'color': 'Green', 'length': 2}),
        ('Chicago', 'Saint Louis', {'color': 'White', 'length': 2}), 
        ('Chicago', 'Pittsburgh', {'color': 'Black', 'length': 3}), 
        ('Chicago', 'Pittsburgh', {'color': 'Orange', 'length': 3}), 
        ('Saint Louis', 'Pittsburgh', {'color': 'Green', 'length': 5}), 
        ('Pittsburgh', 'New York', {'color': 'Green', 'length': 2}), 
        ('Pittsburgh', 'New York', {'color': 'White', 'length': 2}), 
        ('Pittsburgh', 'Washington', {'color': 'Gray', 'length': 2}), 
        ('Pittsburgh', 'Raleigh', {'color': 'Gray', 'length': 2}), 
        ('Pittsburgh', 'Nashville', {'color': 'Yellow', 'length': 4}), 
        ('Washington', 'Raleigh', {'color': 'Gray', 'length': 2}), 
        ('Washington', 'Raleigh', {'color': 'Gray', 'length': 2}), #second route
        ('Raleigh', 'Charleston', {'color': 'Gray', 'length': 2}), 
        ('Raleigh', 'Atlanta', {'color': 'Gray', 'length': 2}), 
        ('Raleigh', 'Atlanta', {'color': 'Gray', 'length': 2}), #secondRoute
        ('Nashville', 'Raleigh', {'color': 'Black', 'length': 3}), 
        ('Atlanta', 'Charleston', {'color': 'Gray', 'length': 2}), 
        ('Nashville', 'Atlanta', {'color': 'Gray', 'length': 1}),
        ('Atlanta', 'New Orleans', {'color': 'Yellow', 'length': 4}),
        ('Atlanta', 'New Orleans', {'color': 'Orange', 'length': 4}),
        ('Little Rock', 'New Orleans', {'color': 'Green', 'length': 3}),
        ('Little Rock', 'Nashville', {'color': 'White', 'length': 3}),
        ('Saint Louis', 'Nashville', {'color': 'Gray', 'length': 2}), 
        ('Saint Louis', 'Little Rock', {'color': 'Gray', 'length': 2}), 
        ('Kansas City', 'Oklahoma City', {'color': 'Gray', 'length': 2}), 
        ('Kansas City', 'Oklahoma City', {'color': 'Gray', 'length': 2}), #second
        ('Oklahoma City', 'Litle Rock', {'color': 'Gray', 'length': 2}), 
        ('Oklahoma City', 'Dallas', {'color': 'Gray', 'length': 2}), 
        ('Oklahoma City', 'Dallas', {'color': 'Gray', 'length': 2}),#second
        ('Dallas', 'Little Rock', {'color': 'Gray', 'length': 2}),
        ('Dallas', 'Houston', {'color': 'Gray', 'length': 1}),
        ('Dallas', 'Houston', {'color': 'Gray', 'length': 1}), #second
        ('El Paso', 'Dallas', {'color': 'Red', 'length': 4}), 
        ('El Paso', 'Oklahoma City', {'color': 'Yellow', 'length': 5}), 
        ('Santa Fe', 'Oklahoma City', {'color': 'Blue', 'length': 3}),
        ('Denver', 'Oklahoma City', {'color': 'Red', 'length': 4}),
        ('Santa Fe', 'El Paso', {'color': 'Gray', 'length': 2}),
        ('Phoenix', 'Denver', {'color': 'White', 'length': 5}),
        ('Phoenix', 'El Paso', {'color': 'Gray', 'length': 3})
        ]
        self.G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True, font_size=8, node_size=500, node_color='skyblue', font_color='black', font_weight='bold', edge_color=[e[2]['color'] for e in G.edges(data=True)])
        plt.show()
    def findIndex(self, originCity, destinationCity, color):
    # This function takes in the origin city, destination city, and color of the route.
    #It then finds the index of the route in the edges list.
    
        for edge in self.edges:
            if (edge[0] == originCity and edge[1] == destinationCity) or \
                (edge[0] == destinationCity and edge[1] == originCity):
                if edge[2]['color'] == color:
                    return self.edges.index(edge)  
            return -1
    



print("How many players are there?")
players = int(input())
theGame = Game(players)
while(theGame.gameEnd != True):
  "Select an action, 1. Take Cards, 2. Take Routes, 3. Play Cards, 4. Forfeight"
  playerResponse = int(input())
  if(playerResponse == 1):
    print("Which cards would you like to take?(Format: X or X_Y)")
    choice = str(input())
    if(len(choice) == 1):
      theGame.Turn(1, int(choice), 0, 0)
    else:
      theGame.Turn(1, int(choice[0]), int(choice[2]), 0)
  elif(playerResponse == 2):
    print("Which routes would you like to take?(Format: X, X_Y, or X_Y_Z")
    choice = str(input())
    if(len(choice) == 1):
      theGame.Turn(2, int(choice), 0, 0)
    elif("1" in choice and "2" in choice and "3" in choice):
      theGame.Turn(2, 7, 0, 0)
    elif("1" in choice and "2" in choice):
      theGame.Turn(2,4,0,0)
    elif("2" in choice and "3" in choice):
      theGame.Turn(2,5,0,0)
    elif("1" in choice and "3" in choice):
      theGame.Turn(2,6,0,0)
  elif(playerResponse == 3):
    print("Which track would you like to secure?(Format: Los Angeles to Miami")
    i = -1
    while(i == -1):
      choice = str(input())
      cities = choice.split(" to ")
      print("Which color would you like to use?")
      color = str(input())
      i = theGame.gameBoard.findIndex(cities[0], cities[1], color)
      if(i != -1):
        print("Track not found, try again")
      else:
        print("How many cards and rainbows cards would you like to play? Format: X/Y")
        b = True
        while(b):
          choice = str(input())
          if(int(choice[0]) + int(choice[2])) == theGame.gameBoard.edges[i][2]['length']:
              b = False
        theGame.Turn(3,i,0,0)
    
        
    
      
    
    

  elif(playerResponse == 4):
    theGame.Turn(4,0,0,0)
  else:
    print("Invalid Choice, give a valid selection")
      
    
