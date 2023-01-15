import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

start_stop_key = KeyCode(char='s')
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.05)

def start_stop(key):
    if key == start_stop_key:
        global clicking
        clicking = not clicking

def main():
    click_thread = threading.Thread(target=clicker)
    click_thread.start()
    with Listener(on_press=start_stop) as listener:
        listener.join()

if __name__ == "__main__":
    main()