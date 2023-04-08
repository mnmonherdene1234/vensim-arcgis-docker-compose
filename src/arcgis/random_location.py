import random


def get_random_location():
    # Mongolia's latitude and longitude boundaries
    min_lat, max_lat = 41.5906, 52.1491
    min_lon, max_lon = 87.743, 119.772

    # Generate a random latitude and longitude within the boundaries
    lat = random.uniform(min_lat, max_lat)
    lon = random.uniform(min_lon, max_lon)

    # Return the location as a tuple
    return (lat, lon)
