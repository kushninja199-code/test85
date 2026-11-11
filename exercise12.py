'''
Exercise 12 Drink Water Reminder :
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system.
'''

# import win32com.client
# import time
# import cv2
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# voice=speaker.GetVoices()
# speaker.Voice = voice.Item(0)
# for i in range(1):
#     time.sleep(10)
#     speaker.Speak("drink water")
#     img = cv2.imread('image.jpg')
#     cv2.imshow('Image Presentation', img)
#     speaker.Speak("drink water")
#     cv2.waitKey(10000)  # Wait for 10000 milliseconds (5 seconds) before closing the window
#     cv2.destroyAllWindows()

# or

from plyer import notification
import win32com.client
import time
from PIL import Image
speaker = win32com.client.Dispatch("SAPI.SpVoice")
voice=speaker.GetVoices()
speaker.Voice = voice.Item(0)
a=int(input("Enter the time in seconds after which you want to be reminded to drink water: "))
b=int(input("Enter the number of times you want to be reminded: "))
for i in range(b):
    time.sleep(a)
    speaker.Speak("drink water")
    img=Image.open('image.jpg')
    speaker.Speak("drink water")
    img.show()
    notification.notify(
        title="DRINK WATER REMINDER",
        message="Leave your work and drink water",
        app_name="My Python Script",
        timeout=10  # Duration in seconds
    )

