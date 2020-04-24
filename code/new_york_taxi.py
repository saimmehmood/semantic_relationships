import googlemaps
import polyline
import pandas as pd
import calculation as _path
import math
import time
import random


#API_KEY = 'AIza....qSgEWaI4RnfCp0wXMI4'


def getPath(API_KEY, start, end, waypoints, traj_mode, index, threshold):
    # connect to the google maps api via api key
    _gmaps = googlemaps.Client(key=API_KEY)
    # allow convertion of an empty list
    if waypoints == []:
        waypoints == None

    _response = _gmaps.directions(start, end, waypoints=waypoints, mode=traj_mode, alternatives='true')

    # print(_response)
    if _response == []:
        return _response

    #print(_response[index])
    return _response[index]


def find_start_location(path):
    start_location = []

    #print(path)
    steps = path['legs'][0]['steps']

    for i in steps:
        location = i['start_location']
        coordinate = (location['lat'], location['lng'])

        start_location.append(coordinate)

    return start_location


# extract reasonable constant K distance between two points
def _extract_polyline(start_location, end_location, radius_distance):
    new_points = [start_location]

    lat1 = start_location[0]
    lat2 = end_location[0]
    long1 = start_location[1]
    long2 = end_location[1]

    bearing = _path.calculateBearing(lat1, long1, lat2, long2)

    lat = lat1
    lon = long1

    point = _path.calculateDestination(lat, lon, bearing, radius_distance)

    distance = (_path.distanceLatLong(lat, lon, lat2, long2)) * 1000

    while distance > (radius_distance * 1000):
        point = _path.calculateDestination(lat, lon, bearing, radius_distance)
        new_points.append(point)

        lat = point[0]
        lon = point[1]

        distance = (_path.distanceLatLong(lat, lon, lat2, long2)) * 1000

    return new_points


# return a list of decoded polyline coordinates given the index of the steps
def find_polylines(path, step_num):
    points_list = []
    steps = path['legs'][0]['steps']

    points = steps[step_num]['polyline']['points']
    points_list = polyline.decode(points)
    ''' 
    for s in range(0, len(steps)):
        points = steps[s]['polyline']['points']
        points_list = polyline.decode(points)

        location_list.append(points_list)
    '''

    return points_list


# create a list in the form of (lat, lng) for end_location
def find_end_location(path):
    end_location = []
    steps = path['legs'][0]['steps']

    for s in steps:
        location = s['end_location']
        coordinate = (location['lat'], location['lng'])

        end_location.append(coordinate)

    return end_location


# given a list of steps, and the index of one path
# retrieve one trajectory/ path
def findRoute(path, start, end, waypoints, traj_mode, index, threshold):
    # initialized the values for the list(s)
    start_location = find_start_location(path)

    end_location = find_end_location(path)

    # concaternate in a parallel way
    route = []

    for i in range(0, len(start_location)):
        polyline = find_polylines(path, i)

        length = len(polyline)
        for p in range(0, length - 1):
            start = polyline[p]
            end = polyline[p + 1]
            points = _extract_polyline(start, end, threshold)
            route += points

        route.append(polyline[length - 1])

    #print(route)
    return route

# start = 40.767936706542969, -73.982154846191406
# end = 40.765602111816406, -73.964630126953125
#
waypoints = []

mode = "driving"
#
# path = getPath(API_KEY, start, end, waypoints, 'driving', 0, 0.05)
#
# trajectory = findRoute(path, start, end, waypoints, 'driving', 0, 0.05)
#
# print(trajectory)

# retrieving starting and ending coordinates of trip.
# "sample_10000.csv" is created by uniformly, randomly taking
# coordinates from new york taxi rides.
df = pd.read_csv("sample_10000.csv")

start_lon = df['s_long']
start_lat = df['s_lat']

end_lon = df['e_long']
end_lat = df['e_lat']


f_traj  = open("new_york_traj_02.csv", "w")
f_traj.write("trajectory\n")

start_time = time.time()

for i in range(len(start_lat)):

    start = start_lat[i], start_lon[i]
    end = end_lat[i], end_lon[i]


    path = getPath(API_KEY, start, end, waypoints, mode, 0, 0.05)
    trajectory = findRoute(path, start, end, waypoints, mode, 0, 0.05)

    f_traj.write(str('\"') + str(trajectory) + str('\"'))
    f_traj.write("\n")
#
f_traj.close()

end_time = time.time()

print(end_time - start_time)