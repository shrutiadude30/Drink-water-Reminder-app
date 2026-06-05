import time
from plyer import notification

while True:
    print("Time to drink water! Stay hydrated!")
    notification.notify(title="Drink Water Reminder",
                        message="It's time to drink water! Stay hydrated!",
                        timeout=10)
    time.sleep(60*60)  # Wait for 1 hour before the next reminder
