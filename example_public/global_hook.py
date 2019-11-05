import keyboard

print('Press and release your desired hotkey: ')
hotkey = keyboard.read_hotkey()
print('Hotkey selected: ', hotkey)

def on_triggered():
    print("Triggered!")

keyboard.add_hotkey(hotkey, on_triggered)
print("Press ESC to stop.")

import time
while True:
    time.sleep(1)
