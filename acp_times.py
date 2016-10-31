"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    start = arrow.get(brevet_start_time)
    time_passed = 0
    past_dist = 0
    if(control_dist_km <= 1000 and control_dist_km > 600):
        open_speed = 28 #kmph
        temp_dist = control_dist_km - 600
        past_dist += temp_dist
        time_passed += (temp_dist / open_speed)
    if(control_dist_km > 400):
        open_speed = 30 #kmph
        temp_dist = control_dist_km - past_dist - 400
        past_dist += temp_dist
        time_passed += (temp_dist / open_speed)
    if(control_dist_km > 200):
        open_speed = 32 #kmph
        temp_dist = control_dist_km - past_dist - 200
        past_dist += temp_dist
        time_passed += (temp_dist / open_speed)
    if(control_dist_km >= 0):
        open_speed = 34 #kmph
        temp_dist = control_dist_km - past_dist
        time_passed += (temp_dist / open_speed)
    UTC_error = 8 #added 5 hours to fix the UTC bug for our timezone
    hours = (time_passed // 1)
    minutes = int(((time_passed - hours) * 60) // 1)
    open_time = start.replace(hours=+(hours+UTC_error))
    open_time = open_time.replace(minutes=+minutes)
    return open_time.isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    start = arrow.get(brevet_start_time)
    time_passed = 0
    past_dist = 0
    UTC_error = 8 #added 8 hours to fix the UTC bug for our timezone
    if(control_dist_km <= 1000 and control_dist_km > 600):
        open_speed = 11.428 #kmph
        temp_dist = control_dist_km - 600
        past_dist += temp_dist
        time_passed += (temp_dist / open_speed)
    if(control_dist_km > 0):
        open_speed = 15 #kmph
        temp_dist = control_dist_km - past_dist
        past_dist += temp_dist
        time_passed += (temp_dist / open_speed)
    if(control_dist_km == 0):
        close_time = start.replace(hours=+(1+UTC_error))
        return close_time.isoformat()
    hours = (time_passed // 1)
    minutes = int(((time_passed - hours) * 60) // 1)
    close_time = start.replace(hours=+(hours+UTC_error))
    close_time = close_time.replace(minutes=+minutes)
    return close_time.isoformat()
