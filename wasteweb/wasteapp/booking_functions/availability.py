import datetime
from wasteapp.models import Schedule,Booking,Truck

'''def check_availability(schedule,booking_time):
    avail_list = []
    booking_list = Booking.objects.filter(schedule=schedule)
    for booking in booking_list:
        if booking.booking_time == schedule :
            avail_list.append(True) 
        else:
            avail_list.append(False)
    return all(avail_list)       ''' 
    