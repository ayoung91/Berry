from flask import Flask, render_template, request
from SenseHat_TicTacToe import RunTicTacToe 
from SenseHat_GetTemperature import GetTemperature
from SenseHat_Clear import ClearSenseHat
from SenseHat_DrawUtility import ShowShutdownAnimation

app = Flask(__name__)
        
def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

def getTemplateData():
    return {
      'title' : 'Berry'
    }
    
@app.route("/")
def index():
    templateData = {
      'title' : 'Berry'
    }
    return render_template('index.html', **templateData)
   
@app.route("/<activity>")
def action(activity):
    if activity == "tictactoe":
        print("main")
        RunTicTacToe()        
        return render_template('index.html', **templateData)
    elif activity == "gettemperature":
        GetTemperature()
    elif activity == "shutdown":
        ShowShutdownAnimation()
        restart()
        
    templateData = {
      'title' : 'Berry'
    }

if __name__ == "__main__":
   app.run(host='192.168.0.112', port=5000, debug=True)
   
   
   
   






