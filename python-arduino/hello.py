from pyfirmata import Arduino, util
import time


board = Arduino('COM10', 115200)
board.digital[13].write(1)

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)