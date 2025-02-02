import threading
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# (off or on) soap_dispensed 

state = {
    'scores': [], 
    'current_state': 'off', # this can be on or off, on being a game is running and off is not
    'soap_dispensed': False, 
    'current_score': 0  
}

last_state = state['current_state'] 

# All flask routes defined here 
@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()
    
    # get all the data stored from the current session
    return jsonify({'message': 'success'})

@app.route('/test', methods=['GET'])
def test():
    # read from the last line of the file
    with open('info.txt', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]

    parsed = last_line.strip("\n").split(' ')
    print("PARSED LAST LINE:", parsed)

    active_game = parsed[0]
    soap_dispensed = parsed[1]

    state['current_state'] = active_game
    state['soap_dispensed'] = soap_dispensed
    last_state = state['current_state']

    return jsonify({'message': state})

if __name__ == '__main__': 
    app.run(port=5000, host='0.0.0.0')