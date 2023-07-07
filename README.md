# dd-to-nmea
A simple script to convert decimal degrees coordinates to NMEA format. This is useful for situations where you are trying to construct a valid NMEA string (e.g. GNGLL) and your input coordinates are in decimal degees (DD) format.

## How to use
Simply pass your DD latitude to the `lat2nmea` function or your DD longitude to the `lon2nmea` function. A tuple will be returned with the relevant lat/lon and northing/easting:
```
>>> from dd_to_nmea import *

>>> lat2nmea(50.344260)
('5020.65560', 'N')
>>> lon2nmea(-4.152175)
('00409.13050', 'W')
```

Lat/lon with `+` symbol are also handled correctly:
```
>>> lat2nmea(+5.122106)
('0507.32636', 'N')
```

From here, it is possible to construct a valid NMEA GLL sentence with these lat/lon using `pynmea2` package:
```
>>> import pynmea2

>>> lat, northing = lat2nmea(50.34426)
>>> lon, easting = lon2nmea(-4.152175)
>>> msg = pynmea2.GLL("GP", "GLL", (lat, northing, lon, easting, "162530.00", "A", "A"))
>>> print(msg)
$GPGLL,5020.65560,N,00409.13050,W,162530.00,A,A*75
```
