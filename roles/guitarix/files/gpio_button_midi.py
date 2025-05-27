import RPi.GPIO as GPIO
import time
import subprocess

BUTTON_PIN = {{ guitarix_gpio_pin }}
MIDI_NOTE = {{ guitarix_midi_note }}

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_midi_note_on(note):
    subprocess.call([
        "sendmidi", "dev", "Guitarix", "on", "ch=1", f"note={note}", "vel=127"
    ])

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            send_midi_note_on(MIDI_NOTE)
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()