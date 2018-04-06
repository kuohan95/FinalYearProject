from ics import Calendar, Event
from datetime import datetime
import time

calendar = Calendar(open('calendar.ics', 'r'))
event = calendar.events
a = int(time.mktime(datetime.now().timetuple()))

for x in range(len(event)):
            human = event[x].begin
            timetable = int(time.mktime(event[x].begin.timetuple()))
            if timetable > a:
                break
            else :
                print (x+1 ,(timetable), human)




