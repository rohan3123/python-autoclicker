import pyautogui
import time

# delay before starting in seconds
initalDelay = 5

# click interval in seconds
clickInterval = 1

# number of clicks to perform
numbClicks = 10

# pause between clicks 
pause_between_clicks = 0.5

print(f"Autoclicker will start in {initialDelay} seconds...")
time.sleep(initalDelay)

# Perform autoclicks
for _ in range(numbClicks):
    # Get the current mouse position
    x, y = pyautogui.position()
    
    
print("Autoclicker is done")