import pyautogui
import random
import time
import keyboard

keepLooping = True


def stoplooping():
    keepLooping = False


# wait 10 seconds so we can move to remote desktop window
time.sleep(10)

while keepLooping:
    randWaitTime = random.randint(1, 10)
    randXOffset = random.randint(-50, 50)
    randYOffset = random.randint(-50, 50)
    randMoveDuration = random.randint(1, 5)

    mouseX, mouseY = pyautogui.position()

    # TODO enforce bounds on mouse position

    pyautogui.moveRel(randXOffset, randYOffset, randMoveDuration)

    time.sleep(randWaitTime)
