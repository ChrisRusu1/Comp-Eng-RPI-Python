from gpiozero import LEDBoard
from time import sleep

t = 0.2
setting = 3
if (setting == 0):
    ledRow = LEDBoard(18,23,17,22,12,16,5,13)
    while True:
        for i in range(8):
            if (i != 0):
                ledRow[i].on()
                sleep(t)
                ledRow[i].off()
                sleep(t)
        for i in range(8):
            if (i != 0):
                ledRow[7-i].on()
                sleep(t)
                ledRow[7-i].off()
                sleep(t)
elif(setting ==1):
    ledHalfs = LEDBoard(18,13,23,5,17,16,22,12)
    while True:
        for i in range(8):
            ledHalfs[i].on()
            sleep(.2)
        sleep(1)
        for i in range(8):
            ledHalfs[7-i].off()
            sleep(.2)
        sleep(1)
elif (setting == 2):
    ledTetris = LEDBoard(18,23,17,22,12,16,5,13)
    while True:
        for i in range(8):
            for f in range(8-i):
                ledTetris[f].on()
                sleep(0.02)
                ledTetris[f].off()
                sleep(0.02)
            ledTetris[7-i].on()
elif (setting == 3):
    ledBin = LEDBoard(18,23,17,22,12,16,5,13)
    counter = 0
    for i in range(1, 256):
        count = 0
        print(bin(i)[2:][::-1])
        for c in bin(i)[2:][::-1]:
            if (c == "1"):
                ledBin[count].on()
            if (c == "0"):
                ledBin[count].off()
            count+=1
        sleep(.03)
                
        
