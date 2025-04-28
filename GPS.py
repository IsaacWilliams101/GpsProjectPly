import gps
try:
    session = gps.gps(mode=gps.WATCH_ENABLE)
    while 0 == session.read():
        if not (gps.MODE_SET & session.valid):
            continue
        print('Mode: %s(%d) Time: ' %
              (("Invalid", "NO_FIX", "2D", "3D")[session.fix.mode],
               session.fix.mode), end="")
        print(session.fix.time, end="")
        if ((gps.isfinite(session.fix.latitude)) and
             gps.isfinite(session.fix.longitude)):
            print(" Lat %.6f Lon %.6f" %
                  (session.fix.latitude, session.fix.longitude))
        else:
            print(" Lat n/a Lon n/a")    
except KeyboardInterrupt:
    print('')
session.close()
exit(0)
