import random
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def count_cards_by_color(cards):
    color_counts = {}

    for card in cards:
        color = card.lower()  # Convert to lowercase for case-insensitivity
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    for color, count in color_counts.items():
        print(f"You have {count} {color} cards.")

scoringGuide = {
    1:1,
    2:2,
    3:4,
    4:7,
    5:10,
    6:15
}
routes = [ 
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
route_points = {
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

city_coordinates = {
    'Seattle': (47.608013,-122.335167),
    'Portland': (45.5051, -122.6750),
    'San Francisco': (37.7749, -122.4194),
    'Los Angeles': (34.0522, -118.2437),
    'Las Vegas': (36.1699, -115.1398),
    'Salt Lake City': (40.7608, -111.8910),
    'Helena': (46.595806, -112.027031),
    'Duluth': (46.786671, -92.100487),
    'Omaha': (41.2565, -95.9345),
    'Denver': (39.7392, -104.9903),
    'Kansas City': (39.0997, -94.5786),
    'Oklahoma City': (35.4676, -97.5164),
    'Dallas': (32.7767, -96.7970),
    'Houston': (29.7604, -95.3698),
    'El Paso': (31.7619, -106.4850),
    'Santa Fe': (35.6869, -105.9378),
    'Phoenix': (33.4484, -112.0740),
    'Little Rock': (34.7465, -92.2896),
    'Chicago': (41.8781, -87.6298),
    'St. Louis': (38.6270, -90.1994),
    'Pittsburgh': (40.4406, -79.9959),
    'Nashville': (36.1627, -86.7816),
    'Atlanta': (33.7490, -84.3880),
    'Miami': (25.7617, -80.1918),
    'New York': (40.7128, -74.0060),
    'Boston': (42.3601, -71.0589),
    'Montreal': (45.5017, -73.5673),
    'Toronto': (43.6532, -79.3832),
    'Sault Ste. Marie': (46.5215, -84.3467),
    'Winnipeg': (49.8951, -97.1384),
    'Raleigh': (35.7796, -78.6382),
    'Washington': (38.8951, -77.0364),
    'Charleston': (32.7765, -79.9311),
    'New Orleans': (29.9511, -90.0715),
    'Calgary': (51.0447, -114.0719),
    'Vancouver': (49.2827, -123.1207),
}
def longest_path_length(graph, source, weight='weight'):
    # Run Bellman-Ford algorithm
    path_lengths = nx.single_source_bellman_ford_path_length(graph, source, weight=weight)

    # Find the maximum length
    max_length = min(path_lengths.values())

    return max_length * -1

edges = [ ('Vancouver', 'Seattle', {'color': 'Gray', 'length': 1}),
    ('Seattle', 'Vancouver', {'color': 'Gray', 'length': 1}), #Second Gray track
    ('Seattle', 'Portland', {'color': 'Gray', 'length': 1}),     
    ('Portland', 'Seattle', {'color': 'Gray', 'length': 1}),  # Second gray track
    ('Portland', 'San Francisco', {'color': 'Green', 'length': 5}),
    ('San Francisco', 'Portland', {'color': 'Pink', 'length': 5}),
    ('Los Angeles', 'Phoenix', {'color': 'Gray', 'length': 3}),
    ('Phoenix', 'Santa Fe', {'color': 'Gray', 'length': 3}),
    ('Santa Fe', 'Denver', {'color': 'Gray', 'length': 2}),
    ('Denver', 'Omaha', {'color': 'Pink', 'length': 4}),
    ('Omaha', 'Chicago', {'color': 'Blue', 'length': 4}),
    ('Las Vegas', 'Salt Lake City', {'color': 'Orange', 'length': 3}),
    ('Los Angeles', 'Las Vegas', {'color': 'Gray', 'length': 2}),
    ('Salt Lake City', 'Helena', {'color': 'Pink', 'length': 3}),
    ('Helena', 'Winnipeg', {'color': 'Blue', 'length': 4}),
    ('Winnipeg', 'Sault Ste. Marie', {'color': 'Gray', 'length': 6}),
    ('Los Angeles', 'San Francisco', {'color': 'Pink', 'length': 3}),
    ('San Francisco', 'Los Angeles', {'color': 'Yellow', 'length': 3}),
    ('San Francisco', 'Salt Lake City', {'color': 'Orange', 'length': 5}),
    ('Salt Lake City', 'San Francisco', {'color': (0.95, 0.95, 0.95), 'length': 5}),
    ('Montreal', 'Boston', {'color': 'Gray', 'length': 2}),
    ('Boston', 'Montreal', {'color': 'Gray', 'length': 2}), #second
    ('Montreal', 'New York', {'color': 'Blue', 'length': 3}),
    ('Los Angeles', 'El Paso', {'color': 'Black', 'length': 6}),
    ('El Paso', 'Houston', {'color': 'Green', 'length': 6}),
    ('Houston', 'New Orleans', {'color': 'Gray', 'length': 2}),
    ('New Orleans', 'Miami', {'color': 'Red', 'length': 6}),
    ('Miami', 'Charleston', {'color': 'Pink', 'length': 4}),
    ('Washington', 'New York', {'color': 'Black', 'length': 2}),
    ('New York', 'Washington', {'color': 'Orange', 'length': 2}),
    ('New York', 'Boston', {'color': 'Yellow', 'length': 2}),
    ('Boston', 'New York', {'color': 'Red', 'length': 2}),
    ('Seattle', 'Calgary', {'color': 'Gray', 'length': 4}),
    ('Calgary', 'Winnipeg', {'color': (0.95, 0.95, 0.95), 'length': 6}),
    ('Sault Ste. Marie', 'Montreal', {'color': 'Black', 'length': 5}),
    ('Duluth', 'Sault Ste. Marie', {'color': 'Gray', 'length': 3}),
    ('Sault Ste. Marie', 'Toronto', {'color': 'Gray', 'length': 2}),
    ('Toronto', 'Chicago', {'color': (0.95, 0.95, 0.95), 'length': 4}),
    ('Calgary', 'Vancouver', {'color': 'Gray', 'length': 3}),
  ('Seattle', 'Helena', {'color': 'Yellow', 'length': 6}),
  ('Helena', 'Duluth', {'color': 'Orange', 'length': 6}),
  ('Helena', 'Denver', {'color': 'Green', 'length': 4}),
  ('Helena', 'Omaha', {'color': 'Red', 'length': 5}),
  ('Portland', 'Salt Lake City', {'color': 'Blue', 'length': 6}),
  ('Calgary', 'Helena', {'color': 'Gray', 'length': 4}),
  ('Winnipeg', 'Duluth', {'color': 'Black', 'length': 4}),
  ('Duluth', 'Toronto', {'color': 'Pink', 'length': 6}),
  ('Duluth', 'Omaha', {'color': 'Gray', 'length': 2}),
  ('Omaha', 'Duluth', {'color': 'Gray', 'length': 2}), #secondGrayRoute
  ('Duluth', 'Chicago', {'color': 'Red', 'length': 3}),
  ('Toronto', 'Pittsburgh', {'color': 'Gray', 'length': 2}),
  ('Toronto', 'Montreal', {'color': 'Gray', 'length': 3}),
  ('Salt Lake City', 'Denver', {'color': 'Red', 'length': 3}),
  ('Denver', 'Salt Lake City', {'color': 'Yellow', 'length': 3}),
  ('Denver', 'Kansas City', {'color': 'Black', 'length': 4}),
  ('Kansas City', 'Denver', {'color': 'Orange', 'length': 4}),
  ('Kansas City', 'St. Louis', {'color': 'Blue', 'length': 2}),
  ('St. Louis', 'Kansas City', {'color': 'Pink', 'length': 2}),
  ('Omaha', 'Kansas City', {'color': 'Gray', 'length': 1}),
  ('Kansas City', 'Omaha', {'color': 'Gray', 'length': 1}), #second route
  ('Chicago', 'St. Louis', {'color': 'Green', 'length': 2}),
  ('St. Louis', 'Chicago', {'color': (0.95, 0.95, 0.95), 'length': 2}), 
  ('Chicago', 'Pittsburgh', {'color': 'Black', 'length': 3}), 
  ('Pittsburgh', 'Chicago', {'color': 'Orange', 'length': 3}), 
  ('St. Louis', 'Pittsburgh', {'color': 'Green', 'length': 5}), 
  ('Pittsburgh', 'New York', {'color': 'Green', 'length': 2}), 
  ('New York', 'Pittsburgh', {'color': (0.95, 0.95, 0.95), 'length': 2}), 
  ('Pittsburgh', 'Washington', {'color': 'Gray', 'length': 2}), 
  ('Pittsburgh', 'Raleigh', {'color': 'Gray', 'length': 2}), 
  ('Pittsburgh', 'Nashville', {'color': 'Yellow', 'length': 4}), 
  ('Washington', 'Raleigh', {'color': 'Gray', 'length': 2}), 
  ('Raleigh', 'Washington', {'color': 'Gray', 'length': 2}), #second route
  ('Raleigh', 'Charleston', {'color': 'Gray', 'length': 2}), 
  ('Raleigh', 'Atlanta', {'color': 'Gray', 'length': 2}), 
  ('Atlanta', 'Raleigh', {'color': 'Gray', 'length': 2}), #secondRoute
  ('Nashville', 'Raleigh', {'color': 'Black', 'length': 3}), 
  ('Atlanta', 'Charleston', {'color': 'Gray', 'length': 2}), 
  ('Nashville', 'Atlanta', {'color': 'Gray', 'length': 1}),
  ('Atlanta', 'New Orleans', {'color': 'Yellow', 'length': 4}),
  ('New Orleans', 'Atlanta', {'color': 'Orange', 'length': 4}),
  ('Little Rock', 'New Orleans', {'color': 'Green', 'length': 3}),
  ('Little Rock', 'Nashville', {'color': (0.95, 0.95, 0.95), 'length': 3}),
  ('St. Louis', 'Nashville', {'color': 'Gray', 'length': 2}), 
  ('St. Louis', 'Little Rock', {'color': 'Gray', 'length': 2}), 
  ('Kansas City', 'Oklahoma City', {'color': 'Gray', 'length': 2}), 
  ('Oklahoma City', 'Kansas City', {'color': 'Gray', 'length': 2}), #second
  ('Oklahoma City', 'Little Rock', {'color': 'Gray', 'length': 2}), 
  ('Oklahoma City', 'Dallas', {'color': 'Gray', 'length': 2}), 
  ('Dallas', 'Oklahoma City', {'color': 'Gray', 'length': 2}),#second
  ('Dallas', 'Little Rock', {'color': 'Gray', 'length': 2}),
  ('Dallas', 'Houston', {'color': 'Gray', 'length': 1}),
  ('Houston', 'Dallas', {'color': 'Gray', 'length': 1}), #second
  ('El Paso', 'Dallas', {'color': 'Red', 'length': 4}), 
  ('El Paso', 'Oklahoma City', {'color': 'Yellow', 'length': 5}), 
  ('Santa Fe', 'Oklahoma City', {'color': 'Blue', 'length': 3}),
  ('Denver', 'Oklahoma City', {'color': 'Red', 'length': 4}),
  ('Santa Fe', 'El Paso', {'color': 'Gray', 'length': 2}),
  ('Phoenix', 'Denver', {'color': (0.95, 0.95, 0.95), 'length': 5}),
  ('Phoenix', 'El Paso', {'color': 'Gray', 'length': 3}),
  ('Atlanta', 'Miami', {'color': 'Blue', 'length': 5})]



def findIndex(originCity, destinationCity, color):
    # This function takes in the origin city, destination city, and color of the route.
    #It then finds the index of the route in the edges list.
        for edge in edges:
            if (edge[0] == originCity and edge[1] == destinationCity) or \
                (edge[0] == destinationCity and edge[1] == originCity):
                if edge[2]['color'] == color:
                    return edges.index(edge)  
            return -1
def seeMap():
    G = nx.DiGraph() 
    m = Basemap(projection='merc', llcrnrlat=25, urcrnrlat=52, llcrnrlon=-130, urcrnrlon=-60, resolution='l')

    for city, coordinates in city_coordinates.items():
        x, y = m(coordinates[1], coordinates[0])
        G.add_node(city, pos=(x, y))
    G.add_edges_from(edges)

    # Set up the Basemap
    fig, ax = plt.subplots(figsize=(12, 10))
    m.drawcountries()
    m.drawcoastlines()

    # Draw nodes
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=100, node_color='red')

    edge_colors = [edge[2]['color'] for edge in G.edges(data=True)]
    background_color = '#c0c0c0'  # Replace with your desired background color
    rect = plt.Rectangle((m.xmin, m.ymin), m.xmax - m.xmin, m.ymax - m.ymin, color=background_color)
    ax.add_patch(rect)

    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad=0.1', edgelist=G.edges(), edge_color=edge_colors, width=[edge[2]['length'] for edge in G.edges(data=True)])

    edge_labels = {(edge[0], edge[1]): edge[2]['length'] for edge in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw edges using nx.draw_networkx_edges with custom attributes
    plt.title('Ticket To Ride')

    plt.show()





class TicketToRideDeck:
 
    def __init__(self):
        # Initialize the train car deck with a list of cards
        self.train_car_cards = ["Red", "Yellow", "Green", "Blue", "Pink", "Black", "White", "Orange", "Rainbow"] * 12 + ["Rainbow","Rainbow"]
        # Shuffle the deck initially
        self.shuffleDeck(self.train_car_cards)
    def shuffleDeck(self, drawPile):
      random.shuffle(drawPile)
      self.train_car_cards = drawPile
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
        self.score = 0
        self.G = nx.DiGraph()
        self.cities = city_coordinates
        self.trainCount = 45
        self.m  = Basemap(projection='merc', llcrnrlat=25, urcrnrlat=52, llcrnrlon=-130, urcrnrlon=-60, resolution='l')
        for city, coordinates in city_coordinates.items():
            x, y = self.m(coordinates[1], coordinates[0])
            self.G.add_node(city, pos=(x, y))




    def addEdges(self, originCity, destinationCity, color):
       k = edges[findIndex(originCity, destinationCity, color)] 
       self.personalTracks.append(k)
       self.G.add_edge(k)
    
    def calculateScore(self):
        self.score = 0
        for track in self.personalTracks:
            self.score += scoringGuide[track[2]['length']]
        return self.score
    
    def recursive(self, target, current):
        if target == current:
            return True
        node_edges = self.G.edges(current)
        for edge in node_edges:
            if self.recursive(target, edge[1]):
                return True
        return False


    def calculateRoutes(self):
        for route in self.personalRoutes:
            cities = route.split(" in ")
            if(self.recursive(cities[0], cities[1]) == True):
                self.score += route_points[route]
            else:
                self.score -= route_points[route]
                    

    def calculateLongestRoute(self):
        G = nx.DiGraph()
        nodes = self.cities
        edges = self.personalRoutes
        for j in range(len(edges)):
            edges[j][2]['length'] *= -1
        # Add nodes to the graph
        G.add_nodes_from(nodes)

        # Add edges to the graph
        G.add_edges_from(edges)
        maxDistanceLengths = []
        for node in nodes:
            maxDistanceLengths.append(longest_path_length(G, node))
        return max(maxDistanceLengths)

        
            

        









    def seeBoard(self):
        # Set up the Basemap
        fig, ax = plt.subplots(figsize=(12, 10))
        self.m.drawcountries()
        self.m.drawcoastlines()

        # Draw nodes
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw_networkx_nodes(self.G, pos, ax=ax, node_size=100, node_color='red')

        edge_colors = [edge[2]['color'] for edge in self.G.edges(data=True)]
        background_color = '#c0c0c0'  # Replace with your desired background color
        rect = plt.Rectangle((self.m.xmin, self.m.ymin), self.m.xmax - self.m.xmin, self.m.ymax - self.m.ymin, color=background_color)
        ax.add_patch(rect)

        nx.draw(self.G, pos, with_labels=True, connectionstyle='arc3, rad=0.1', edgelist=self.G.edges(), edge_color=edge_colors, width=[edge[2]['length'] for edge in self.G.edges(data=True)])

        edge_labels = {(edge[0], edge[1]): edge[2]['length'] for edge in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        # Draw edges using nx.draw_networkx_edges with custom attributes
        plt.title('Board Progress')

        plt.show()










class Routes:
    def __init__(self):
        self.routes = routes
        random.shuffle(self.routes)
    
    def takeRoutes(self, choices):
        selected_routes = []

        if choices == 1:
            selected_routes.append(self.routes.pop(0))
        elif choices == 2:
            selected_routes.append(self.routes.pop(1))
        elif choices == 3:
            selected_routes.append(self.routes.pop(2))
        elif choices == 4:
            selected_routes.extend(self.routes.pop(0))
            selected_routes.extend(self.routes.pop(0))
        elif choices == 5:
            selected_routes.append(self.routes.pop(1))
            selected_routes.append(self.routes.pop(1))
        elif choices == 6:
            selected_routes.append(self.routes.pop(0))
            selected_routes.append(self.routes.pop(1))
        elif choices == 7:
            selected_routes.append(self.routes.pop(0))
            selected_routes.append(self.routes.pop(0))
            selected_routes.append(self.routes.pop(0))
        return selected_routes
class Game:
    def __init__(self, num_players):
        self.gameEnd = False
        self.num_players = num_players
        self.players = [Player() for i in range(num_players)]
        self.order = 0
        #use order variable to designate which player's turn it will be 
        self.gameRoutes = Routes()
        self.gameDeck = TicketToRideDeck()
        self.gameBoard = Board()
        self.discardPile = []
        self.gameScore = []
    def beginning(self):
        #function to distribute cards and Routes
        for i in range(4):
            for player in self.players:
                if(i <= 2):
                    player.personalRoutes.append(self.gameRoutes.routes.pop(0))
                player.personalDeck.append(self.gameDeck.train_car_cards.pop(0))
    def Turn(self, choice, j, k, l):
        #Choice will either be draw cards, draw routes, or play cards
        if(choice == 1):
          temp = self.gameDeck.takeCards(j, k)
          print(temp)
          self.players[self.order].personalDeck += temp
        elif(choice == 2):
          temp = self.gameRoutes.takeRoutes(j)
          self.players[self.order].personalRoutes += temp
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
        if(self.order == self.num_players-1):
            self.order = 0
        else:
            self.order += 1
    def calculateScore(self):
        longestRoute = []
        for player in self.players:
            player.calculateScore()
            player.calculateRoutes()
            longestRoute.append(player.calculateLongestRoute())
            self.gameScore.append(player.score)
        for index in range(len(longestRoute)):
            if(longestRoute[index] == max(longestRoute)):
                self.players[index].score += 10
            self.gameScore.append(self.players[index].score)
        return self.gameScore







class Board:
    def __init__(self):
        self.G = nx.DiGraph()
        self.nodes = city_coordinates
        self.edges1 = edges
        self.edges2 = []
        self.m  = Basemap(projection='merc', llcrnrlat=25, urcrnrlat=52, llcrnrlon=-130, urcrnrlon=-60, resolution='l')

        for city, coordinates in self.nodes.items():
            x, y = self.m(coordinates[1], coordinates[0])
            self.G.add_node(city, pos=(x, y))
        self.G.add_edges_from(self.edges2)
    
    def findIndex(self, originCity, destinationCity, color):
    # This function takes in the origin city, destination city, and color of the route.
    #It then finds the index of the route in the edges list.
        for edge in self.edges1:
            if (edge[0] == originCity and edge[1] == destinationCity) or \
                (edge[0] == destinationCity and edge[1] == originCity):
                if edge[2]['color'] == color:
                    return self.edges1.index(edge)  
            return -1





    def addEdges(self, originCity, destinationCity, color):
       k = edges[findIndex(originCity, destinationCity, color)] 
       self.edges2.append(k)
       self.G.add_edge(k)




    def seeBoard(self):
        # Set up the Basemap
        fig, ax = plt.subplots(figsize=(12, 10))
        self.m.drawcountries()
        self.m.drawcoastlines()

        # Draw nodes
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw_networkx_nodes(self.G, pos, ax=ax, node_size=100, node_color='red')

        edge_colors = [edge[2]['color'] for edge in self.G.edges(data=True)]
        background_color = '#c0c0c0'  # Replace with your desired background color
        rect = plt.Rectangle((self.m.xmin, self.m.ymin), self.m.xmax - self.m.xmin, self.m.ymax - self.m.ymin, color=background_color)
        ax.add_patch(rect)

        nx.draw(self.G, pos, with_labels=True, connectionstyle='arc3, rad=0.1', edgelist=self.G.edges(), edge_color=edge_colors, width=[edge[2]['length'] for edge in self.G.edges(data=True)])

        edge_labels = {(edge[0], edge[1]): edge[2]['length'] for edge in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        # Draw edges using nx.draw_networkx_edges with custom attributes
        plt.title('Board Progress')

        plt.show()







def take_turn(theGame, playerResponse):
    if playerResponse == 1:
        # Logic for taking cards
        print("Which cards would you like to take?(Format: X or X_Y)")
        choice = str(input())
        if len(choice) == 1 and theGame.gameDeck.train_car_cards[int(choice)-1] != "Rainbow":
            temp = theGame.gameDeck.train_car_cards.pop(int(choice)-1)
            theGame.players[theGame.order].personalDeck.append(temp)
            theGame.gameDeck.seeTopFive()
            choice = str(input())
            print("What second card would you like to take?")
            theGame.Turn(1, int(choice[0])-1, 0, 0)
        elif len(choice) == 1:
            theGame.Turn(1, int(choice[0])-1, 0, 0)
        else:
            theGame.Turn(1, int(choice[0])-1, int(choice[2])-1, 0)
    elif playerResponse == 2:
        # Logic for taking routes
        print("Which routes would you like to take?(Format: X, X_Y, or X_Y_Z")
        choice = str(input())
        if len(choice) == 1:
            theGame.Turn(2, int(choice), 0, 0)
        elif "1" in choice and "2" in choice and "3" in choice:
            theGame.Turn(2, 7, 0, 0)
        elif "1" in choice and "2" in choice:
            theGame.Turn(2, 4, 0, 0)
        elif "2" in choice and "3" in choice:
            theGame.Turn(2, 5, 0, 0)
        elif "1" in choice and "3" in choice:
            theGame.Turn(2, 6, 0, 0)
    elif playerResponse == 3:
        # Logic for playing cards
        print("Which track would you like to secure?(Format: Los Angeles to Miami")
        i = -1
        while i == -1:
            choice = str(input())
            cities = choice.split(" to ")
            print("Which color would you like to use?")
            color = str(input())
            #check if they have the route already
            for edge10 in theGame.players[theGame.order].personalRoutes:
                if((edge10[0] == cities[0] and edge10[1] == cities[1]) or (edge10[1] == cities[0] and edge10[0] == cities[1])):
                    print("Invalid Choice, You already have this route secured, give a valid selection")
                    break
            i = theGame.gameBoard.findIndex(cities[0], cities[1], color)
            if i != -1:
                print("Track not found/already purchased, try again")
            else:
                print("How many cards and rainbows cards would you like to play? Format: X/Y")
                b = True
                while b:
                    choice = str(input())
                    if (
                        theGame.players[theGame.order].count(color) > choice[0]
                        and theGame.players[theGame.order].count("Rainbow") > choice[2]
                    ):
                        if int(choice[0]) + int(choice[2]) == theGame.gameBoard.edges[i][2]["length"]:
                            b = False
                            theGame.Turn(3, i, 0, 0)
                            theGame.players[theGame.order].addEdges(
                                edges[i][0], edges[i][1], edges[i][2]["color"]
                            )
                            theGame.gameBoard.addEdges(
                                edges[i][0], edges[i][1], edges[i][2]["color"]
                            )
                            del theGame.gameBoard.edges2[i]
                        else:
                            print("Wrong number of cards, try again")
                    else:
                        print("You do not have the right number of cards, make another selection")
                        break
                        break
    elif playerResponse == 4:
        theGame.Turn(4, 0, 0, 0)
    elif playerResponse == 5:
        seeMap()
    elif playerResponse == 6:
        theGame.gameBoard.seeBoard()
    elif playerResponse == 7:
        theGame.players[theGame.order].seeBoard()
    elif playerResponse == 8:
        print("Your Tickets are")
        print(theGame.players[theGame.order].personalRoutes)
    elif playerResponse == 9:
        count_cards_by_color(theGame.players[theGame.order].personalDeck)
    elif playerResponse == 10:
        theGame.gameDeck.seeTopFive()
    else:
        print("Invalid Choice, give a valid selection")



print("How many players are there?")
players = int(input())
theGame = Game(players)
theGame.beginning()

#Throw Away Routes

for i in range(len(theGame.players)):
    option = 0
    while(option != 5):
        print("Select an action before the game begins, 1. See Map, 2. See your Routes, 3. See your Cards, 4. See Top 5 Cards, 5. Move On")
        option = int(input())
        if(option > 6 or option < 1):
            print("Give a valid selection")
        else:
            if(option == 1):
                seeMap()
            elif(option == 2):
                print("Your Tickets are")
                print(theGame.players[i].personalRoutes)
            elif(option == 3):
                count_cards_by_color(theGame.players[i].personalDeck)
            elif(option == 4):
                theGame.gameDeck.seeTopFive()
            elif(option == 5):
                pass

for i in range(len(theGame.players)):
    print("Would you like to throw away any routes?(Sample Response: '3'[-1 removes no routes])")
    throwAway = int(input())
    if(throwAway != -1):
        removed_element  = theGame.players[i].personalRoutes.pop(throwAway-1)
        theGame.gameRoutes.routes.append(removed_element)



#Main Game Sequence
while not theGame.gameEnd:
    print("Select an action, 1. Take Cards, 2. Take Routes, 3. Play Cards, 4. Forfeit, 5. See Map, 6. See Board, 7. See Your Tracks, 8. See your Routes, 9. See your cards, 10. See Public Stack, 11, See Discard Pile")
    playerResponse = int(input())
    take_turn(theGame, playerResponse)



#model out when the game ends
print("The Game is ending, last turn!")
for i in range(len(theGame.players)):
    print("Select an action, 1. Take Cards, 2. Take Routes, 3. Play Cards, 4. Forfeit, 5. See Map, 6. See Board, 7. See Your Tracks, 8. See your Routes, 9. See your cards, 10. See Public Stack, 11, See Discard Pile")
    playerResponse = int(input())
    take_turn(theGame, playerResponse)


theGame.calculateScore
for i in range(len(theGame.gameScore)):
    print("Player " + i + " had " + str(theGame.gameScore[i]) + " points!")

    
    




