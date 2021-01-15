import os
import time
from SenseHat_Clear import ClearSenseHat 
from sense_hat import SenseHat

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

def showSnowFlake():
    X = [0, 0, 255]  # Blue
    O = [255, 255, 255]  # White

    question_mark = [
    X, X, X, O, O, X, X, X,
    X, O, X, O, O, X, O, X,
    X, X, O, X, X, O, X, X,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    X, X, O, X, X, O, X, X,
    X, O, X, O, O, X, O, X,
    X, X, X, O, O, X, X, X
    ]

    _sense.set_pixels(question_mark)
    
def showFire():
    X = [255, 0, 0]  # Red
    Y = [255, 165, 0] # Yellow
    O = [255, 255, 255]  # White

    question_mark = [
    O, O, O, O, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, X, Y, X, O, O, O,
    O, X, Y, Y, Y, X, O, O,
    O, X, Y, Y, Y, Y, X, O,
    O, X, Y, Y, Y, Y, X, O,
    O, O, X, Y, Y, X, O, O,
    O, O, O, X, X, O, O, O,
    ]

    _sense.set_pixels(question_mark)

_sense = SenseHat()
_temp = 0

time.sleep(5)
t = _sense.get_temperature_from_humidity()
t_cpu = get_cpu_temp()
h = _sense.get_humidity()
p = _sense.get_pressure()

# calculates the real temperature compesating CPU heating
t_corr = t - ((t_cpu-t)/1.5)
_temp = t_corr * 1.8 + 32
print(_temp)
  
if (_temp < 32):
    showSnowFlake()
elif (_temp > 90):
    showFire()
    
time.sleep(5)
ClearSenseHat()