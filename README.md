# Berry

This is my fun little hobby project called Berry. Its a raspberry pi connected with a sense hat that can do these things:
- Two player Tic Tac Toe
- Get the temperature (with CPU heat offset), displays the temperature in fahrenheit. If the temperature is colder than 32 degrees, a snowflake is displayed. If its hotter than 90 degrees a flame is displaye. Else, a smiley face.
- A lot more intersting stuff to come!

This is a headless pi, so you don't need a monitor. You can use your phone as long as the IP address and port number in the main.py matches your phone and pi.
The main.py runs a Flask web server. So the calls from the index.html file call the methods with the matching route.
This program runs automatically on startup on a service called berry.service. It needs to be added to the etc/systemd/system folder (with sudo privaleges)

I am currently attempting safely shutdown the pi if there is a voltage change (either too high or too low). The power bank I am using (Viros 10,000 mAh) alerts the pi when the power is throttles (changing while also powering). I am still looking into seeing if the pi is alerted when the power is low --probably not.
To Do this, I have a shell script called low_voltage_shutdown.sh (remember to make it executable). It runs a command that gets the throttle code 0x0 is good. Other commands not so much. I noticed when the power bank is changing and powering the pi, it gives a 0x5005 code.
If the code is anything other than 'throttle 0x0', it will call a python script that safely shuts down the pi. 
I am trying to get this to run in crontab every 2 seconds, but it sucks and it doesn't work. Crontab only has 1 minute intervals so this is my way around it. Those crazy symbols are asterisks. The preview isn't getting that and I dont care to fix it
@reboot cd /home/pi/low_power_shutdown.sh
* * * * * cd /home/pi/low_power_shutdown.sh
* * * * * sleep 2; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 4; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 6; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 8; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 10; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 12; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 14; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 16; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 18; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 20; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 22; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 24; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 26; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 28; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 28; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 30; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 32; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 34; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 36; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 38; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 40; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 42; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 44; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 46; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 48; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 28; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 30; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 32; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 34; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 36; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 38; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 40; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 42; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 44; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 46; cd /home/pi/low_power_shutdown.sh
* * * * * sleep 48; cd /home/pi/low_power_shutdown.sh
