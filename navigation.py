import math

def haversine_distance(lat1, lat2, lon1, lon2):
    r = 6371 #km
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon1_rad = math.radians(lon1)
    lon2_rad = math.radians(lon2)
    distance = 2*r*math.asin(math.sqrt((math.sin((lat2_rad-lat1_rad)/2))**2+math.cos(lat1_rad)*math.cos(lat2_rad)*((math.sin((lon2_rad-lon1_rad)/2))**2)))
    return distance

