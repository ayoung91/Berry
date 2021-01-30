from flask import Flask, render_template, request, redirect
import serial
from time import sleep
from SenseHat_TicTacToe import RunTicTacToe
from SenseHat_GetTemperature import GetTemperature
from SenseHat_Clear import ClearSenseHat
from SenseHat_DrawUtility import ShowShutdownAnimation, ShowRaspberry
from shutdown import ShutdownPi

app = Flask(__name__)
ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
    
_numGames = 0
_isMoving = True
    
@app.route("/")
def index():
    templateData = {
      'title' : 'Berry'
    }
    return render_template('index.html', **templateData)

@app.route("/<activity>")   
def action(activity):
    if activity == "gettemperature":
        GetTemperature()
    elif activity == "shutdown":
        ShutdownPi()
        
    return redirect('')

@app.route("/tictactoe", methods=['POST'])
def numGames():
    global _numGames
    req = request.form
    _numGames = int(req.get("numGames"))
    RunTicTacToe(_numGames)
    
    return redirect('')

@app.route("/move", methods=['GET','POST'])
def move():
    global _isMoving
    _isMoving = True
    speed = 100
    
    print(request.get_json())
    direction = request.get_json()
    while _isMoving:
        speed = speed + 3        
        strSpeed = str(speed)
        message = direction+strSpeed+"\n"
        ser.write(bytes(message, 'utf-8'))
        sleep(0.5)
    return ser.readline()

@app.route("/stopMoving", methods=['GET','POST'])
def stopMoving():
    global _isMoving
    _isMoving = False
    ser.write(b"s\n")
    return ser.readline()
   
if __name__ == "__main__":
    ShowRaspberry()
    app.run(host='192.168.0.112', port=5000, debug=True)
   