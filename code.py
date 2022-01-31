# Play .wav files from a microcontroller
import time, board, digitalio
from audiocore import WaveFile
from adafruit_debouncer import Debouncer

# This code tries to import AudioOut from various locations.
# except code runs if the ImportError is returned
# if both ImportErrors are returned, we print the error message.
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("This board does not support AudioOut")
        pass # Not all boards can play audio with AudioOut

# configure AudioOut & set path where sounds can be found
audio = AudioOut(board.A1)
path = "sounds/"

buttons = []
button_1_input = digitalio.DigitalInOut(board.D5)
button_1_input.switch_to_input(pull=digitalio.Pull.UP) # Button is pushed when button.value == False
button_1 = Debouncer(button_1_input)
buttons.append(button_1)

button_2_input = digitalio.DigitalInOut(board.D6)
button_2_input.switch_to_input(pull=digitalio.Pull.UP) # Button is pushed when button.value == False
button_2 = Debouncer(button_2_input)
buttons.append(button_2)

button_3_input = digitalio.DigitalInOut(board.D9)
button_3_input.switch_to_input(pull=digitalio.Pull.UP) # Button is pushed when button.value == False
button_3 = Debouncer(button_3_input)
buttons.append(button_3)

button_4_input = digitalio.DigitalInOut(board.D10)
button_4_input.switch_to_input(pull=digitalio.Pull.UP) # Button is pushed when button.value == False
button_4 = Debouncer(button_4_input)
buttons.append(button_4)

button_5_input = digitalio.DigitalInOut(board.D11)
button_5_input.switch_to_input(pull=digitalio.Pull.UP) # Button is pushed when button.value == False
button_5 = Debouncer(button_5_input)
buttons.append(button_5)

def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass # add code here that you want to run while sound is playing

sounds = ["mandarin.wav",
            "cantonese.wav",
            "vietnamese.wav",
            "korean.wav",
            "english.wav"]

while True:
    for i in range(len(buttons)):
        buttons[i].update() # checks a debounced button
        if buttons[i].fell: # if a button is pressed
            print(f"BUTTON{i} PRESSED!")
            play_sound(sounds[i])
