import os
from time import sleep
from SenseHat_Clear import ClearSenseHat
from SenseHat_DrawUtility import showSnowFlake, showFire, showSmile, showThinkingAnimation
from sense_hat import SenseHat

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

_sense = SenseHat()
_temp = 0
_timeToCalculate = 5

def GetTemperature():
    showThinkingAnimation(_timeToCalculate)
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
    else:
        showSmile()
        
    sleep(5)
    ClearSenseHat()
