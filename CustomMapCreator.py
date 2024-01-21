import pandas as pd
import math
import networkx as nx
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from collections import Counter
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers

    return distance


def distanceMapping(value, factor):
    mapping_pairs = {
        (40, 27): 8,
        (27, 18): 7,
        (18, 13): 6,
        (13, 9): 5,
        (9, 6.5): 4,
        (6.5, 4.8): 3,
        (4.8, 3.2): 2,
        (3.2, 1.8): 1
    }

    for (start, end), result in mapping_pairs.items():
        if start >= value*factor > end:
            return result

    # If the input value doesn't fall into any range, return None or handle it accordingly
    return None

# Specify the file path
file_path = r'C:\Users\Kethan Raman\Downloads\citiesAbove1000 - Feuil1.csv'

# Read the CSV file into a pandas DataFrame
cities_df = pd.read_csv(file_path)
name_list = cities_df['Name'].tolist()
country_list = cities_df['Country name EN'].tolist()
population_list = cities_df['Population'].tolist()
coordinate_list = cities_df['Coordinates'].tolist()
coordinates = []
for i in range(len(coordinate_list)):
    if isinstance(coordinate_list[i], str):
        j = coordinate_list[i].split(', ')
        j[0] = float(j[0])
        j[1] = float(j[1])
        coordinates.append(j)
    else:
        pass

print("What are the upper and lower latitude and upper and lower longitude (Ex: X/Y/Z/W)")
input_string = input()
print("Would you like to enable length 8 tracks?")
input_bool = input()

# Split the input string into a list of strings
coordinates_list = input_string.split('/')
upper_lat = float(coordinates_list[0])
lower_lat = float(coordinates_list[1])
upper_lon = float(coordinates_list[2])
lower_lon = float(coordinates_list[3])


lat_range = upper_lat - lower_lat
lon_range = upper_lon - lower_lon

# Calculate the width and height of each smaller rectangle
lat_step = lat_range / 5
lon_step = lon_range / 5

# List to store the coordinates of each partitioned rectangle
rectangles = []

# Partition the rectangle into 9 smaller rectangles
for i in range(5):
    for j in range(5):
        # Calculate the coordinates of each corner of the smaller rectangle
        rect_upper_lat = upper_lat - i * lat_step
        rect_lower_lat = upper_lat - (i + 1) * lat_step
        rect_upper_lon = lower_lon + j * lon_step
        rect_lower_lon = lower_lon + (j + 1) * lon_step

        # Store the coordinates in the list
        rectangle_coordinates = [rect_upper_lat, rect_lower_lat, rect_upper_lon, rect_lower_lon]
        rectangles.append(rectangle_coordinates)

area = abs(upper_lon - lower_lon) * abs(upper_lat - lower_lat)
factor = 1458/area

# Calculate the width and height of each smaller rectangle
lat_range = (upper_lat - lower_lat) / 5
lon_range = (upper_lon - lower_lon) / 5



# Assuming 'coordinates' is your array of coordinates, and 'rectangles' is the list of partitioned rectangles
min_distance = 1.8*(1/factor)  # Set your minimum distance threshold
# List to store the first instance of an index for each rectangle
first_instance_indices = []

for rectangle in rectangles:
    rect_upper_lat, rect_lower_lat,  rect_lower_lon, rect_upper_lon = rectangle

    for idx, coordinate in enumerate(coordinates):
        lat, lon = coordinate

        # Check if the coordinate falls within the current rectangle
        if rect_lower_lat <= lat <= rect_upper_lat and rect_lower_lon <= lon <= rect_upper_lon:
            # Check if the coordinate is not too close to other coordinates
            if all(haversine_distance(coordinate, other_coord) >= min_distance for other_coord in coordinates[:idx] + coordinates[idx+1:]):
                first_instance_indices.append(idx)
                break  # Break out of the inner loop once the first instance is found

city_coordinates = {}

for idx in first_instance_indices:
    print(name_list[idx])
    city_name = name_list[idx]
    city_coordinates[city_name] = tuple(coordinates[idx])
print(len(city_coordinates))
# Print or use the city_coordinates dictionary as needed

G = nx.DiGraph() 

# Create a Cartopy map with a topography feature
fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([lower_lon, upper_lon, lower_lat, upper_lat])

# Add topography using Cartopy's natural_earth_shaded relief feature
ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='0.8', alpha=0.5))

# Plot cities on the map
for city, coordinates in city_coordinates.items():
    x, y = coordinates[1], coordinates[0]
    ax.plot(x, y, 'ro', markersize=8, transform=ccrs.PlateCarree(), label=city)
    ax.text(x, y, city, color='black', fontsize=8, ha='right', va='bottom', transform=ccrs.PlateCarree())



# Customize the map
ax.coastlines(resolution='10m', color='black', linewidth=1)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)

plt.title('Topographical Map with Cities')
plt.show()

'''
Length 1: 8 repeated routes, 1 Unique
Length 2: 22 repeated routes, 13 Unique
Length 3: 6 repeated routes, 15 Unique
Length 4: 4 repeated routes, 12 Unique
Length 5: 4 repeated routes, 6 Unique
Length 6: 0 repeated routes, 9 Unqiue
Length 7: 0 repeated routes, 4 Unique
Length 8: 0 repeated routes, 1 Unique
'''
