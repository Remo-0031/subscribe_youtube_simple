from time import sleep

import pyautogui

pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("ctrl", "t")

pyautogui.write("youtube.com")
pyautogui.hotkey("enter")

sleep(4)
search_button = pyautogui.locateCenterOnScreen("search_youtube.jpg", confidence=0.8)
pyautogui.moveTo(search_button)
pyautogui.click()

pyautogui.write("Coding 101 with Steve")
pyautogui.hotkey("enter")

sleep(2)
coding_steve = pyautogui.locateCenterOnScreen("coding_steve.jpg", confidence=0.8)
pyautogui.moveTo(coding_steve)
pyautogui.click()

sleep(1)

try:
    subscribe = pyautogui.locateCenterOnScreen("subscribe.png", confidence=0.9)
    pyautogui.moveTo(subscribe)
    pyautogui.click()
except pyautogui.ImageNotFoundException:
    print("you are already subscribed")
