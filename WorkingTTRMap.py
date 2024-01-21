import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from collections import Counter


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
