from time import sleep, time
from sense_hat import SenseHat
_sense = SenseHat()

def showSnowFlake():
    X = [0, 0, 255]  # Blue
    O = [255, 255, 255]  # White

    snowFlake = [
    X, X, X, O, O, X, X, X,
    X, O, X, O, O, X, O, X,
    X, X, O, X, X, O, X, X,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    X, X, O, X, X, O, X, X,
    X, O, X, O, O, X, O, X,
    X, X, X, O, O, X, X, X
    ]
    
    _sense.set_pixels(snowFlake)
    
def showFire():
    X = [255, 0, 0]  # Red
    Y = [255, 165, 0] # Yellow
    O = [255, 255, 255]  # White

    fire = [
    O, O, O, O, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, Y, X, O, O, O,
    O, X, Y, Y, Y, X, O, O,
    O, X, Y, Y, Y, Y, X, O,
    O, X, Y, Y, Y, Y, X, O,
    O, O, X, Y, Y, X, O, O,
    O, O, O, X, X, O, O, O,
    ]

    _sense.set_pixels(fire)
    
def showSmile():
    X = [0, 0, 0]  # Clear
    Y = [255, 165, 0] # Yellow
    O = [255, 255, 255]  # White

    smile = [
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    Y, Y, X, Y, Y, X, Y, Y,
    Y, Y, X, Y, Y, X, Y, Y,
    Y, X, Y, Y, Y, Y, X, Y,
    Y, Y, X, Y, Y, X, Y, Y,
    O, Y, Y, X, X, Y, Y, O,
    O, O, Y, Y, Y, Y, O, O,
    ]

    _sense.set_pixels(smile)
    
def showThinkingAnimation(seconds):
    X = [255, 0, 0]  # Red
    O = [255, 255, 255]  # White

    questionMark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    
    _sense.set_pixels(questionMark)
    quitSecond = time() + seconds
    while time() < quitSecond:
        rotation = 0
        sleep(0.2)
        _sense.set_rotation(rotation)
        for i in range(3):
            sleep(0.2)
            rotation = rotation + 90
            _sense.set_rotation(rotation)
    
    _sense.set_rotation(0)
