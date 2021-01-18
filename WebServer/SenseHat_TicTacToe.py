from sense_hat import SenseHat
from time import sleep
from SenseHat_Clear import ClearSenseHat

_sense = SenseHat()
_colWhite = [255, 255, 255]
_colBlue = [0, 0, 255]
_rdColBlue = [0, 0, 248]
_colRed = [255, 0, 0]
_rdColRed = [248, 0, 0]
_colClear = [0, 0, 0]
_defaultX = 3
_defaultY = 3
_x = _defaultX
_y = _defaultY
_player = 1
_previousSpot = _colClear

def reset():
    global _previousSpot
    _sense.clear()
    _previousSpot = _colClear
    for i in range(8):
        _sense.set_pixel(i, 2, _colWhite)
        _sense.set_pixel(i, 5, _colWhite)
        _sense.set_pixel(2, i, _colWhite)
        _sense.set_pixel(5, i, _colWhite)
        
    if (_player == 1):
        p1(_defaultX, _defaultY)
    if (_player == 2):
        p2(_defaultX, _defaultY)
        
def p1(x, y):
    _sense.set_pixel(x, y, _colBlue)
    _sense.set_pixel(x, y + 1, _colBlue)
    _sense.set_pixel(x + 1, y, _colBlue)
    _sense.set_pixel(x + 1, y + 1, _colBlue)
    
def p2(x, y):
    _sense.set_pixel(x, y, _colRed)
    _sense.set_pixel(x, y + 1, _colRed)
    _sense.set_pixel(x + 1, y, _colRed)
    _sense.set_pixel(x + 1, y + 1, _colRed)
    
def clearSpot(x, y):
    _sense.set_pixel(x, y, _colClear)
    _sense.set_pixel(x, y + 1, _colClear)
    _sense.set_pixel(x + 1, y, _colClear)
    _sense.set_pixel(x + 1, y + 1, _colClear)
    
def blinkOnce(x, y):
    _sense.set_pixel(x, y, _colClear)
    _sense.set_pixel(x, y + 1, _colClear)
    _sense.set_pixel(x + 1, y, _colClear)
    _sense.set_pixel(x + 1, y + 1, _colClear)
    sleep(0.2)
    setCoordinates(x, y, _player)

def moveLeft(x, y):
    global _previousSpot
    
    blinkOnce(x, y);
    if x > 1:
        newX = x - 3
        resetSpot(x, y)
        _previousSpot = _sense.get_pixel(newX, y)
        setCoordinates(newX, y, _player)
        return newX
    else:
        blinkRapid(x, y)
    return x

def moveUp(x, y):
    global _previousSpot
    
    blinkOnce(x, y);
    if y > 1:
        newY = y - 3
        resetSpot(x, y)
        _previousSpot = _sense.get_pixel(x, newY)
        setCoordinates(x, newY, _player)
        return newY
    else:
        blinkRapid(x, y)
    return y
        
def moveRight(x, y):
    global _previousSpot
    
    blinkOnce(x, y);
    if x < 6:
        newX = x + 3
        resetSpot(x, y)
        _previousSpot = _sense.get_pixel(newX, y)
        setCoordinates(newX, y, _player)
        return newX
    else:
        blinkRapid(x, y)
    return x

def moveDown(x, y):
    global _previousSpot
    
    blinkOnce(x, y);
    if y < 6:
        newY = y + 3
        resetSpot(x, y)
        _previousSpot = _sense.get_pixel(x, newY)
        setCoordinates(x, newY, _player)
        return newY
    else:
        blinkRapid(x, y)
    return y

def blinkRapid(x, y):
    for i in range(2):
        _sense.set_pixel(x, y, _colWhite)
        _sense.set_pixel(x, y + 1, _colWhite)
        _sense.set_pixel(x + 1, y, _colWhite)
        _sense.set_pixel(x + 1, y + 1, _colWhite)
        sleep(0.1)
        clearSpot(x, y)
        sleep(0.1)
    
    setCoordinates(x, y, _player)
        
def setCoordinates(x, y, p):  
    if p == 1:
        p1(x, y)
    elif p == 2:
        p2(x, y)
    else:
        clearSpot(x, y)

def resetSpot(x, y):
    if _previousSpot == _rdColBlue:
        setCoordinates(x, y, 1)
    elif _previousSpot == _rdColRed:
        setCoordinates(x, y, 2)
    else:
        clearSpot(x, y)
        
def hasError(x, y):
    currentSpot = _sense.get_pixel(x, y)
    if currentSpot != _colClear:
        return True
    
def setTurn():
    global _player
    global _x
    global _y

    if _player == 1:
        _player = _player + 1
    elif _player == 2:       
       _player = _player - 1
        
    _x = _defaultX
    _y = _defaultY
    
def isGameOver():    
    if _sense.get_pixel(0, 0) == _sense.get_pixel(3, 3) == _sense.get_pixel(6, 6) and _sense.get_pixel(6, 6) != _colClear:
        blinkWinner(0, 0)
        blinkWinner(3, 3)
        blinkWinner(6, 6)
        return True
    elif _sense.get_pixel(6, 0) == _sense.get_pixel(3, 3) == _sense.get_pixel(0, 6) and _sense.get_pixel(0, 6) != _colClear:
        blinkWinner(6, 0)
        blinkWinner(3, 3)
        blinkWinner(0, 6)
        return True
    elif _sense.get_pixel(0, 0) == _sense.get_pixel(3, 0) == _sense.get_pixel(6, 0) and _sense.get_pixel(6, 0) != _colClear:
        blinkWinner(0, 0)
        blinkWinner(3, 0)
        blinkWinner(6, 0)
        return True
    elif _sense.get_pixel(0, 3) == _sense.get_pixel(3, 3) == _sense.get_pixel(6, 3) and _sense.get_pixel(6, 3) != _colClear:
        blinkWinner(0, 3)
        blinkWinner(3, 3)
        blinkWinner(6, 3)
        return True
    elif _sense.get_pixel(0, 6) == _sense.get_pixel(3, 6) == _sense.get_pixel(6, 6) and _sense.get_pixel(6, 6) != _colClear:
        blinkWinner(0, 6)
        blinkWinner(3, 6)
        blinkWinner(6, 6)
        return True
    elif _sense.get_pixel(0, 0) == _sense.get_pixel(0, 3) == _sense.get_pixel(0, 6) and _sense.get_pixel(0, 6) != _colClear:
        blinkWinner(0, 0)
        blinkWinner(0, 3)
        blinkWinner(0, 6)
        return True
    elif _sense.get_pixel(3, 0) == _sense.get_pixel(3, 3) == _sense.get_pixel(3, 6) and _sense.get_pixel(3, 6) != _colClear:
        blinkWinner(3, 0)
        blinkWinner(3, 3)
        blinkWinner(3, 6)
        return True
    elif _sense.get_pixel(6, 0) == _sense.get_pixel(6, 3) == _sense.get_pixel(6, 6) and _sense.get_pixel(6, 6) != _colClear:
        blinkWinner(6, 0)
        blinkWinner(6, 3)
        blinkWinner(6, 6)
        return True
    elif isScratch():
        return True
    else:
        return False

def blinkWinner(x, y):
    blinkRapid(x, y)
    if (_player == 1):
        setCoordinates(x, y, 2)
    if (_player == 2):
        setCoordinates(x, y, 1)
        
def isScratch():
    isEmptyPosition = False
    list = _sense.get_pixels()
    for i in range(len(list)):
        if list[i] == _colClear:
            isEmptyPosition = True
    
    if not isEmptyPosition:
        allWhite = []
        for i in range(len(list)):
            allWhite.append(_colWhite)
        for i in range(5):
                _sense.set_pixels(allWhite)
                sleep(0.1)
                _sense.clear()
                sleep(0.1)
        return True
    else:
        return False
def RunTicTacToe(numGames):
    global _previousSpot
    global _x
    global _y
    
    gameCount = 0
    reset()
    while True:
        if gameCount >= numGames:
            break
        for stick in _sense.stick.get_events():
            if stick.direction == "middle" and stick.action == "pressed":
                if (_previousSpot != _colClear):
                    blinkRapid(_x, _y)
                else:
                    setTurn()
                    if isGameOver():
                        gameCount = gameCount + 1
                        reset()
                    else:
                        _previousSpot = _sense.get_pixel(_defaultX, _defaultY)
                        setCoordinates(_defaultX, _defaultY, _player)
            elif stick.direction == "left" and stick.action == "pressed":   
                _x = moveLeft(_x, _y)
            elif stick.direction == "up" and stick.action == "pressed":
                _y = moveUp(_x, _y)
            elif stick.direction == "right" and stick.action == "pressed":
                _x = moveRight(_x, _y)
            elif stick.direction == "down" and stick.action == "pressed":
                _y = moveDown(_x, _y)
                    
    ClearSenseHat()