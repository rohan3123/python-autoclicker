import pyautogui
import time

# delay before starting in seconds
initalDelay = 5

# click interval in seconds
clickInterval = 1

# number of clicks to perform
numbClicks = 10

# pause between clicks 
pauseBetweenClicks = 0.5

print(f"Autoclicker will start in {initialDelay} seconds...")
time.sleep(initalDelay)

# Perform autoclicks
for _ in range(numbClicks):
    # Get the current mouse position
    x, y = pyautogui.position()
    
    pyautogui.click(x, y)
    
    time.sleep(pauseBetweenClicks)
    
    time.sleep(clickInterval)
    
print("Autoclicker is done")