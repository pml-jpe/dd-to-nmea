import math


def lat2nmea(input):
    frac, whole = math.modf(input)
    deg = "{:02d}".format(abs(int(whole)))
    mins = "{:08.5f}".format(abs(round(frac*60, 5)))
    nmea_lat = "{0}{1}".format(deg, mins)
    if input >= 0:
        northing = "N"
    else:
        northing = "S"
    return(nmea_lat, northing)


def lon2nmea(input):
    frac, whole = math.modf(input)
    deg = "{:03d}".format(abs(int(whole)))
    mins = "{:08.5f}".format(abs(round(frac*60, 5)))
    nmea_lon = "{0}{1}".format(deg, mins)
    if input >= 0:
        easting = "E"
    else:
        easting = "W"
    return(nmea_lon, easting)
