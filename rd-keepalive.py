import random
import time

import pyautogui

keep_looping = True
pyautogui.FAILSAFE = True


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

print("Program started. Stop mouse movements by moving mouse to any corner of screen. ")
print("Now move to remote desktop. You have 10 seconds...")

time.sleep(10)

print("Beginning random mouse movements.  ")

try:
    while keep_looping:
        rand_wait_time = random.randint(1, 10)
        rand_x_offset = random.randint(-50, 50)
        rand_y_offset = random.randint(-50, 50)
        rand_move_duration = random.randint(1, 5)

        mouse_x, mouse_y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        # TODO if mouse is near screen edges, clip

        print("Moving to", mouse_x, ", ", mouse_y)

        pyautogui.moveRel(rand_x_offset, rand_y_offset, rand_move_duration)

        print("Waiting...")

        time.sleep(rand_wait_time)
except pyautogui.FailSafeException:
    print("Program Finished")
