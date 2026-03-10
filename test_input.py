import serial
import time

# serial0 è la porta hardware dei pin GPIO 14/15
ser = serial.Serial('/dev/serial0', 9600)

try:
    while True:
        # Invia valori di prova: Sterzo 50, Motore 20
        ser.write(b"50,20\n")
        print("Inviato: 50,20")
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()