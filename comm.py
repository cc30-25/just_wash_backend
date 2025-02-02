import serial


arduino = serial.Serial("COM7", 9600)



# clear file 
with open('info.txt', 'w') as f:
    f.write('')

# we need to track the current state of the game along with analyics 

state = { 
    'current_state': 'off', 
    'soap_dispensed': False, 
    'current_score': 0,
    'scores': [], 
    
}

while True:
    # Simulate reading from serial and updating state
    # read from serial
    data = arduino.readline().decode("utf-8").strip()
    
    

    # write to file named info.txt
    with open('info.txt', 'a') as f:
        f.write(data + '\n')
