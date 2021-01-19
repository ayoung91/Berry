from flask import Flask, render_template, request
import subprocess
from SenseHat_TicTacToe import RunTicTacToe
from SenseHat_GetTemperature import GetTemperature
from SenseHat_Clear import ClearSenseHat
from SenseHat_DrawUtility import ShowShutdownAnimation, ShowRaspberry

app = Flask(__name__)

_numGames = 0

def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
    
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
        ShowShutdownAnimation()
        restart()
        
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
   
if __name__ == "__main__":
    ShowRaspberry()
    app.run(host='192.168.0.112', port=5000, debug=True)
   
   






