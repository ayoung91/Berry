from flask import Flask, render_template, request
import subprocess
import serial
from SenseHat_TicTacToe import RunTicTacToe
from SenseHat_GetTemperature import GetTemperature
from SenseHat_Clear import ClearSenseHat
from SenseHat_DrawUtility import ShowShutdownAnimation, ShowRaspberry
from shutdown import ShutdownPi

app = Flask(__name__)
ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
    
_numGames = 0
    
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
        
    templateData = {
      'title' : 'Berry'
    }
    return render_template('index.html', **templateData)

@app.route("/tictactoe", methods=['POST'])
def numGames():
    global _numGames
    req = request.form
    _numGames = int(req.get("numGames"))
    RunTicTacToe(_numGames)
    
    templateData = {
      'title' : 'Berry'
    }
    return render_template('index.html', **templateData)

@app.route("/moveForward", methods=['GET','POST'])
def moveForward():
    ser.write(b"Move forward\n")
    return ser.readline()

@app.route("/turnLeft", methods=['GET','POST'])
def turnLeft():
    ser.write(b"Turn left\n")
    return ser.readline()

@app.route("/turnRight", methods=['GET','POST'])
def turnRight():
    ser.write(b"Turn right\n")
    return ser.readline()

@app.route("/moveBackward", methods=['GET','POST'])
def moveBackward():
    ser.write(b"Move backward\n")
    return ser.readline()

@app.route("/stopMoving", methods=['GET','POST'])
def stopMoving():
    ser.write(b"Stop moving\n")
    return ser.readline()
   
if __name__ == "__main__":
    ShowRaspberry()
    app.run(host='192.168.0.112', port=5000, debug=True)
   