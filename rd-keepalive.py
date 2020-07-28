import random
import time

import pyautogui

keep_looping = True
pyautogui.FAILSAFE = True
mouse_zone_border = 80  # bounds to keep the mouse away from screen edges
screen_width, screen_height = pyautogui.size()


def stop_looping():
    global keep_looping
    keep_looping = False


# TODO implement event hook correctly. Doesn't work yet...

# def key_pressed():
#     key = keyboard.KeyboardEvent.name
#     if key == "q":
#         print(key, " pressed. Stopping...")
#         stop_looping()
#
#
# keyboard.hook(key_pressed())

print("Program started. Stop mouse movements by moving mouse to any corner of screen, or press Ctrl+C in this "
      "terminal. ")
print("Screen dimensions - ", screen_width, ", ", screen_height)
print("Now move to remote desktop. You have 10 seconds...")

time.sleep(10)

print("Beginning random mouse movements.  ")

try:
    while keep_looping:
        rand_wait_time = random.randint(10, 60)
        rand_move_duration = random.randint(1, 5)

        curr_mouse_x, curr_mouse_y = pyautogui.position()

        new_mouse_x = curr_mouse_x + random.randint(-50, 50)
        new_mouse_y = curr_mouse_y + random.randint(-50, 50)

        if (screen_width - new_mouse_x) < mouse_zone_border:
            new_mouse_x = screen_width - mouse_zone_border
        elif new_mouse_x < mouse_zone_border:
            new_mouse_x = mouse_zone_border

        if (screen_height - new_mouse_y) < mouse_zone_border:
            new_mouse_y = screen_height - mouse_zone_border
        elif new_mouse_y < mouse_zone_border:
            new_mouse_y = mouse_zone_border

        print("Moving to - ", new_mouse_x, ", ", new_mouse_y)

        pyautogui.moveTo(new_mouse_x, new_mouse_y, rand_move_duration)

        print("Waiting...")

        time.sleep(rand_wait_time)

except pyautogui.FailSafeException:
    print("Program Finished")
