import RPi.GPIO as GPIO
import Keypad
import time
import requests

ep = "http://18.224.37.203:8080/validate-pin"

ROWS = 4
COLS = 4
keys =  [   '1','2','3','A',
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [7,11,13,15]
colsPins = [8,10,12,16]

GPIO.setmode(GPIO.BOARD)

motor1 = [32,36,38,40]

for pin in motor1:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1],]

rev = [[0,0,0,1],
       [0,0,1,1],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [1,1,0,0],
       [1,0,0,0],
       [1,0,0,1],]

def unlock():
    for i in range(64):
        for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(motor1[pin],rev[halfstep][pin])
                time.sleep(0.001)

def lock():
    for i in range(64):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(motor1[pin],seq[halfstep][pin])
		time.sleep(0.001)

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

    msg = {"pin":pw, "user_id":"103"}
    val = requests.post(url=ep,data=msg)
    val = val.text

    if(val[1:6] == "valid"):
        print ("Password Correct")
        unlock()
        pw = ""
        while(pw != "A"):
            key = keypad.getKey()
            if(key != keypad.NULL):
               pw = "%c"%(key)
               print(pw)
            if(pw == "A"):
                lock()
    else:
        print ("Password Incorrect")


if __name__ == '__main__':
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:
        pass
        GPIO.cleanup()

    GPIO.cleanup()
