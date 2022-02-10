import argparse
import math
from geopy.geocoders import Nominatim
import folium
from folium import plugins



def parsering():
    """
Returns persed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('year')
    parser.add_argument('latitude')
    parser.add_argument('longitude')
    parser.add_argument('path_to_dataset', type=str)
    return parser.parse_args()


def reading_locations(path_to_dataset: str, year: str) -> list:
    """
Reads locations from a file and adds all movies from a particular year to the list
Args:
    path_to_dataset (str): path to the dataset with films and locations where they were shot
    year (str): year of filming
Returns:
    list: a list of lists with films from a particuler year and their places
    """
    with open(path_to_dataset, mode="r", encoding="UTF-8", errors="ignore") as file:
        data = file.readlines()[14:]
        lst_film_place = []
        for i in range(len(data)):
            data[i] = data[i].strip("\n").split("\t")
            while '' in data[i]:
                data[i].remove('')
            # deletes mess from a file to get clear location
            if data[i][-1][0] == '(':
                data[i].pop(-1)
            if year in data[i][0]:
                lst_film_place.append(data[i])
    return lst_film_place


def coordinates(location_list: list) -> list:
    """
Using geopy determines coordinates of the place where the movie was shot and add it to the list
Args:
    location_list (list): list of lists whith film title and the location
Returns:
    list: list with film's title, place and coordinates
    """
    list_to_remove = []
    geolocator = Nominatim(user_agent="film_map")
    for i in range(len(location_list)):
        try:
            location = geolocator.geocode(location_list[i][-1])
            coord = (location.latitude, location.longitude)
            location_list[i].append(coord)
        except:
            location_list[i][-1] = location_list[i][-1].split(", ")
            location_list[i][-1].pop(0)
            location_list[i][-1] = ", ".join(location_list[i][-1])
            try:
                location = geolocator.geocode(location_list[i][-1])
                coord = (location.latitude, location.longitude)
                location_list[i].append(coord)
            except:
                list_to_remove.append(location_list[i])
    for item in list_to_remove:
        while item in location_list:
            location_list.remove(item)
    return location_list


def distance(location_list: list, coordinates: tuple) -> dict:
    """
Counts the distance from the movie location to the given starting point
Args:
    location_list (list): list with film's title, place and coordinates
    coordinates (tuple): starting point
Returns:
    dict: key - film's title and location, value - distance to the starting point
    """
    dict_distance = {}
    for film in location_list:
        f1 = film[-1][0]
        f2 = coordinates[0]
        l1 = film[-1][1]
        l2 = coordinates[1]
        distance = 12734.889 * \
            math.asin(math.sqrt((math.sin((f2-f1)/2))**2+math.cos(f1)
                      * math.cos(f2)*(math.sin((l2-l1)/2))**2))
        dict_distance[(film[0], film[-1])] = distance
    return dict_distance


def nearest_locations(dict_distance: dict) -> dict:
    """
Chooses top 10 nearest locations
Args:
    dict_distance(dict): key - film's title and location, value - distance to the starting point
Returns:
    dict: top 10 nearest locations
    """
    dict_sorted = dict(sorted(dict_distance.items(), key=lambda item: item[1]))
    dict_to_folium = {}
    for i in range(10):
        try:
            dict_to_folium[list(dict_sorted.keys())[i][0]] = list(
                dict_sorted.keys())[i][1]
        except:
            break
    return dict_to_folium


def generating_map(dict_to_folium: dict, start_latitude: str, start_longitude: str):
    """
Generates and saves an HTML map with markers on the nearest locations where a movie was shot in the particular year
Args:
    dict_to_folium (dict): dictionary with 10 films with nearest locations
Returns:
    None
    """
    map = folium.Map(tiles="Stamen Terrain", location=[
                     start_latitude, start_longitude], control_scale=True)
    fg = folium.FeatureGroup(name="Nearest films")
    for key in dict_to_folium:
        latitude = dict_to_folium.get(key)[0]
        longitude = dict_to_folium.get(key)[1]
        fg.add_child(folium.Marker(location=[
                     latitude, longitude], popup=key, icon=folium.Icon(icon='film', color="red")))
    map.add_child(fg)
    # mini map in the corner
    minimap = plugins.MiniMap(toggle_display=True)
    map.add_child(minimap)
    plugins.ScrollZoomToggler().add_to(map)
    plugins.Fullscreen(position="topright").add_to(map)
    fg2 = folium.FeatureGroup(name="Starting location")
    fg2.add_child(folium.Marker(location=[start_latitude, start_longitude],
                  popup="You are here", icon=folium.Icon(color="black", icon='nothing')))
    map.add_child(fg2)
    map.add_child(folium.LayerControl())
    map.save('Map.html')


def main():
    """
Main function
    """
    args = parsering()
    path_to_dataset = args.path_to_dataset
    year = args.year

    list_of_locations = reading_locations(path_to_dataset, year)

    list_with_coords = coordinates(list_of_locations)

    start_latitude = float(args.latitude)
    start_longitude = float(args.longitude)

    coords = (start_latitude, start_longitude)

    dict_with_distances = distance(list_with_coords, coords)
    dict_with_nearest = nearest_locations(dict_with_distances)
    generating_map(dict_with_nearest, start_latitude, start_longitude)


if __name__ == "__main__":
    main()
