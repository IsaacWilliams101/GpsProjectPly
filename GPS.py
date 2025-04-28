import gps #imports gps, should already be installed when gpsd was installed
try:
    session = gps.gps(mode=gps.WATCH_ENABLE) #points the script to connect to the gpsd daemon
    while 0 == session.read(): #creates while loop to handle packets
        if not (gps.MODE_SET & session.valid): #checks that the session is valid and the GPS has fix
            continue
        print('Mode: %s(%d) Time: ' % #prints time
              (("Invalid", "NO_FIX", "2D", "3D")[session.fix.mode],
               session.fix.mode), end="")
        print(session.fix.time, end="")
        if ((gps.isfinite(session.fix.latitude)) and #checks that lat and lon are finite
             gps.isfinite(session.fix.longitude)):
            print(" Lat %.6f Lon %.6f" % #prints lat and lon
                  (session.fix.latitude, session.fix.longitude))
        else:
            print(" Lat n/a Lon n/a") #if fix is invalid print n/a"
except KeyboardInterrupt: #on ^c exit script
    print('')
session.close()
exit(0)
