import serial
import time
import math

# Aggiungiamo un piccolo timeout per non intasare la seriale
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

# Puliamo il buffer prima di iniziare
ser.flush()

try:
    for i in range(500):
        s = int(math.sin(i * 0.1) * 100)
        m = int(math.cos(i * 0.1) * 100)
        
        # Fondamentale: la stringa deve finire con \n
        comando = f"{s},{m}\n" 
        ser.write(comando.encode('utf-8'))
        
        # Non scendere sotto i 0.05 (20Hz) per ora, 
        # altrimenti il Pico non sta dietro alla stampa a video
        time.sleep(0.05) 
except KeyboardInterrupt:
    ser.close()