import pyautogui, sys, random, time, keyboard

# give us time to head over to MSRD
time.sleep(10)

keepLooping = True

while keepLooping:
    randWaitTime = random.randint(1,10)
    randXOffset = random.randint(-50,50)
    randYOffset = random.randint(-50,50)
    randMoveDuration = random.randint(1,5)
    
    mouseX, mouseY = pyautogui.position()

    #TODO enforce bounds on mouse position     

    pyautogui.moveRel(randXOffset,randYOffset,randMoveDuration)

    time.sleep(randWaitTime)


def stopLooping(self, parameter_list):
    keepLooping = False