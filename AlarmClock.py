import datetime
import winsound

alarmHour = int(input("Set alarm for what hour?"))
alarmMinute = int(input("Set alarm for what minute?"))
currentTime = datetime.datetime.now()
print(str(currentTime))
activate = True
stop = ""
while activate:
    if(currentTime.minute != datetime.datetime.now().minute):
        print(datetime.datetime.now())
        currentTime = datetime.datetime.now()
    if(alarmHour == currentTime.hour):
        if(alarmMinute == currentTime.minute):
            winsound.Beep(1000, 1000)
            activate = False
                
