#!/usr/bin/env python2.7

import gps

gpsd = gps.gps()
gpsd.stream(gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)

for report in gpsd:
    if report['class'] == 'TPV':
        latitude=report['lat']
        longitude=report['lon']
        break


latitude=str(latitude)
longitude=str(longitude)

# file output
f = open('/tmp/location.txt','w')   # output file to /tmp calling it 'location.txt' 
f.write(latitude)
f.write(' ')
f.write(longitude)
f.close()
