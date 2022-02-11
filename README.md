# WebMap
Creates an HTML map with the location you entered and shows the nearest 10 locations where some films where shot in the given year

Program uses *folium* and *geopy.geocoders* libraries

## Usage
Program works from a command line
```bash
> python main.py 2017 1 1 locations_1.4
```
It takes 4 positional arguments:
- year 
- latitude of the starting point
- longitude of the starting point
- path to the [dataset](https://github.com/beheni/WebMap/blob/main/locations_1.4.list): 

##  Output
Program creates an html file like [this](https://github.com/beheni/WebMap/blob/main/Map_exmpl.html)

![Example](https://github.com/beheni/WebMap/blob/main/map_example.PNG)

## Tool set
When you open the map you can:
- zoom in or out and enter or exit full-screen mode (topright) ![plus](https://user-images.githubusercontent.com/91615487/153141864-358904da-fabf-4cef-87a4-0a152a71f6ab.PNG) ![minus](https://user-images.githubusercontent.com/91615487/153141861-7df705fe-f22c-4b63-932a-072d33f07d22.PNG) ![full_scr](https://user-images.githubusercontent.com/91615487/153141866-04988c63-91c3-4bb0-bd25-3f340dbb726c.PNG)

- show or hide layers of film markers and you starting location (black marker) ![layers](https://user-images.githubusercontent.com/91615487/153140867-5fc5e19c-2b25-43f3-a426-0ba207b8cb94.PNG) ![l1](https://user-images.githubusercontent.com/91615487/153142181-d985a06c-785d-41c0-a46b-6a57aefa2a68.PNG) ![l2](https://user-images.githubusercontent.com/91615487/153142188-a61f6dc9-934a-4c00-9c69-9e40f7b57b8c.PNG) ![l3](https://user-images.githubusercontent.com/91615487/153142192-c5b3c956-ec71-4014-b8bb-4a255a271189.PNG)
- change scrolling method (bottomleft) ![scroll](https://user-images.githubusercontent.com/91615487/153141499-2b8f6750-f179-4c86-afa7-fa78dfa49328.PNG)
- mini map that shows your location and you can change the location on it (bottomright)   
![minimap](https://user-images.githubusercontent.com/91615487/153144351-200b422b-6fa1-43d1-803a-bf4f4dabdf01.PNG)
