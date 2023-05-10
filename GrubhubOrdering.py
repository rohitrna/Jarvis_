# open grubhub
# click zipcode text field
# enter zipcode
import webbrowser
import pyautogui
import time

webbrowser.open("https://www.grubhub.com/")
time.sleep(3)
pyautogui.click(1500, 800)

#print("Enter Zip")
#zip = input()
pyautogui.typewrite("94583")
pyautogui.click(1600, 800)


pyautogui.click(1000, 750)

time.sleep(5)

pyautogui.scroll(-50000)
#pyautogui.scroll(-500000)
time.sleep(3)

pyautogui.click(1400, 600)