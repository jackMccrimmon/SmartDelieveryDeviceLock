import RPi.GPIO as GPIO
import Keypad 

ROWS = 4
COLS = 4
keys =  [   '1','2','3','A',
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [7,11,13,15]
colsPins = [8,10,12,16]

def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)
    keypad.setDebounceTime(50)
    pw = ""
    temp = ""
    count = 0
    while(count != 4):
        key = keypad.getKey()
        if(key != keypad.NULL):
            temp = "%c"%(key)
            pw = pw + temp
            print(pw)
            count = count + 1
    if(pw == "1234"):
       print ("Password Correct")
    else:
       print ("Password Incorrect")
            
if __name__ == '__main__':  
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt: 
        pass
        GPIO.cleanup()  