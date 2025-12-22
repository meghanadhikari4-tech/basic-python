
import time
alarm_time=input("Enter the time(HH:MM):")
print(f"the time is {alarm_time}")
while True:
    current_time=time.strftime("%H:%M")
    if current_time==alarm_time:
        print("\n WAKE UP ALARM RINGS\n")
        break

    