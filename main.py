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
state_lock = threading.Lock()


# All flask routes defined here 
@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()
    
    # get all the data stored from the current session

    return jsonify({'message': 'success'})

@app.route('/test', methods=['GET'])
def test():
    with state_lock:
        current_state = state

    return jsonify({'message': current_state})



# All serial logic present in this function
def read_serial():
    global state
    while True:
        # Simulate reading from serial and updating state
        # read from serial 
        

        with state_lock:
            state['scores'].append('data')
            time.sleep(1) 

def start_flask():
    app.run(port=5000, host='0.0.0.0')

if __name__ == '__main__':
    thread = threading.Thread(target=read_serial)
    thread2 = threading.Thread(target=start_flask)
    thread.start()
    thread2.start()