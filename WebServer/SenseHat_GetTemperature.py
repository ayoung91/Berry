import os
from time import sleep
from SenseHat_DrawUtility import ShowSnowFlake, ShowFire, ShowSmile, ShowThinkingAnimation, ShowRaspberry
from sense_hat import SenseHat

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

_sense = SenseHat()
_temp = 0
_timeToCalculate = 2

def GetTemperature():
    ShowThinkingAnimation(_timeToCalculate)
    t = _sense.get_temperature_from_humidity()
    #t = _sense.get_temperature()
    t_cpu = get_cpu_temp()
    h = _sense.get_humidity()
    p = _sense.get_pressure()

    # calculates the real temperature compesating CPU heating
    t_corr = t - ((t_cpu-t)/3.7)
    _temp = t_corr * 1.8 + 32
    _temp = t_corr * 1.8 + 32
    _sense.show_message(str(round(_temp, 1)))
      
    if (_temp < 32):
        ShowSnowFlake()
    elif (_temp > 90):
        ShowFire()
    else:
        ShowSmile()
        
    sleep(5)
    ShowRaspberry()
