import pywhatkit as kit
import time

phone = input("Enter phone number including country code: ")

messages = []
hours = []
minutes = []

while True:
    message = input("Enter message to send (type 'x' to exit): ")
    if message == "x":
        break
    hour = int(input("Enter hour to send (0-23): "))
    minute = int(input("Enter minute to send (0-59): "))
    messages.append(message)
    hours.append(hour)
    minutes.append(minute)

for i in range(len(messages)):
    message = messages[i]
    hour = hours[i]
    minute = minutes[i]
    kit.sendwhatmsg(phone, message, hour, minute)
    time.sleep(10) # Wait for 10 seconds before sending the next message