import pypyodbc
from ics import Calendar, Event
from datetime import datetime
import time
try:
    #Student query 
    myConnection = pypyodbc.connect('Driver={SQL Server};'
                                    'Server=DESKTOP-SB51I6U\SQLEXPRESS;'
                                    'Database=RIMS_Attendance')
    # print('Wooooo')

    try:
        myCursor = myConnection.cursor()
        SQLCommand = ("SELECT Clock "
                      "FROM ras_AttRecord "
                      "WHERE DIN =15000001")
        myCursor.execute(SQLCommand)
    
        results = myCursor.fetchall()
        flattened = [x[0] for x in results]
        
        log = []
        
        for x in range(len(flattened)):
            human = flattened[x]
            attended = int(time.mktime(flattened[x].timetuple()))
            log.append(attended)
            # print (x+1, attended, human)

    except:
        print("could not retrieve")
    myConnection.close()
except:
    print('Failed')



#Calendar query 
calendar = Calendar(open('calendar.ics', 'r'))
event = calendar.events
currentTime = int(time.mktime(datetime.now().timetuple()))

beginlog = []
endlog = []
for x in range(len(event)):
    human = event[x].begin
    timetable = int(time.mktime(event[x].begin.timetuple()))
    timetableEnd = int(time.mktime(event[x].end.timetuple()))
    beginlog.append(timetable)
    endlog.append(timetableEnd)
    
    if timetable > currentTime:
        break
    # else :
         # print (x+1 ,(timetable), human)

counter = 0
for x in range(len(beginlog)):
    for j in range(len(log)):
        present = (beginlog[x]-300) <= log[j] <= endlog[x]
        if present == True:
            counter += 1
            print(beginlog[x])
            break
        
    
print("Attended class count:" , counter)
