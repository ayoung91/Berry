from SenseHat_DrawUtility import ShowShutdownAnimation
import subprocess

def Shutdown():
    command = "/usr/bin/sudo /sbin/shutdown now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

def ShutdownPi():
    ShowShutdownAnimation()
    Shutdown()