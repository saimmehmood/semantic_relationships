import math
from random import uniform

#Earth_radius is in kilometre
_Earth_radius = 6371

#Haversine Formula
#calculate the distance between two points in term of Longitude and Latitude
#calculates distance by kilometer (km)
def distanceLatLong(Lat1, Long1, Lat2, Long2):
    
    _lat1_radian = math.radians(Lat1)
    _lat2_radian= math.radians(Lat2)
    _lat_diff = math.radians(Lat2 - Lat1)
    _long_diff = math.radians(Long2 - Long1)

    _a = math.pow(math.sin(_lat_diff/2), 2) + (math.cos(_lat1_radian) * math.cos(_lat2_radian) * (math.pow(math.sin(_long_diff/2), 2))) 

    _c = 2 * (math.atan2(math.sqrt(_a), math.sqrt(1 - _a)))

    return _Earth_radius * _c

# Find the destination coordinate
# parameters MUST be in floating types
# without the correct input type, the calculation will be inaccurate
def calculateDestination(lat, long, bearing, distance):
    lat_radian = math.radians(lat) 
    bearing_radian = math.radians(bearing)

    angular_distance = distance / _Earth_radius

    inner_func = (math.sin(lat_radian) * math.cos(angular_distance)) + (math.cos(lat_radian) * math.sin(angular_distance) * math.cos(bearing_radian))
    
    destination_lat = math.asin(inner_func)
    destination_lat = math.degrees(destination_lat)
    
    destination_lat_radian = math.radians(destination_lat)

    delta_inner = (math.sin(bearing_radian) * math.sin(angular_distance) * math.cos(lat_radian))

    delta = math.atan2(delta_inner, math.cos(angular_distance) - (math.sin(lat_radian) * math.sin(destination_lat_radian)))
    delta_degree = math.degrees(delta)
    destination_long = long + delta_degree


    return (destination_lat, destination_long)

#calculate the bearing angle between two points
def calculateBearing(lat1, long1, lat2, long2):
    
    _lat1_radian = math.radians(lat1)
    _lat2_radian= math.radians(lat2)
    _lat_diff = math.radians(lat2 - lat1)
    _long_diff = math.radians(long2 - long1)

    y_coor = math.sin(_long_diff) * math.cos(_lat2_radian)
    x_coor = (math.cos(_lat1_radian) * math.sin(_lat2_radian)) - (math.sin(_lat1_radian) * math.cos(_lat2_radian) * math.cos(_long_diff)) 

    bearing_radian = math.atan2(y_coor, x_coor)

    return math.degrees(bearing_radian) 

#generate random coordinates given the boundary coordinates
def generateRandom(lower_bound, upper_bound):
    random_x = uniform(lower_bound[0], upper_bound[0])
    random_y = uniform(lower_bound[1], upper_bound[1])

    return (random_x, random_y)
