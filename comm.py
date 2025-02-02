import serial
import time 

arduino = serial.Serial("COM6", 9600)

scores = [] 

cum_sum = 0 # reset when we stat a new game 
past_state = False
curr_state = False
soap_state = False 

# clear file 
with open('info.txt', 'w') as f:
    f.write('')


def update_states(): 
    global curr_state
    global past_state
    global soap_state 
    data = arduino.readline().decode("utf-8").strip()
    game_state = data.split(" ")
    if (len(game_state) <= 1):
        return
    print("Data: ", game_state)
    print("THIS IS GAME STATE")
    past_state = curr_state # past update 
    if (game_state[1] == "1"):
        soap_state = True
    else:
        soap_state = False
    if (game_state[0] == "1"):
        curr_state = True
    else:
        curr_state = False
    print(past_state, curr_state)

while True:
    # Simulate reading from serial and updating state
    # read from serial
    update_states()

    if (curr_state and not past_state):
        print("Starting game")
        time.sleep(3)
        cum_sum = 0
        while True:
            update_states() # if button pressed our thing will exit 
            if (soap_state):
                print("Pumped") 
                if (cum_sum == 0) :
                    cum_sum += 50



            if (not curr_state) :
                print("Exited Loop")
                time.sleep(1) 
                scores.append(cum_sum)
                f = open("info.txt", "a")
                f.write(cum_sum)
                f.close()

                
                break

    
