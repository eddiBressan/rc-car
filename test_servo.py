import serial
import time
import math

# Assicurati che /dev/serial0 sia abilitata da raspi-config
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("Inizio test servo... Premi Ctrl+C per fermare.")

try:
    i = 0
    while True:
        # Crea un'onda che va da -100 a 100
        angolo = int(math.sin(i) * 100)
        
        # Inviamo la stringa "STERZO,MOTORE\n"
        # Per ora il motore lo teniamo a 0
        comando = f"{angolo},0\n"
        
        ser.write(comando.encode('utf-8'))
        print(f"Inviato angolo: {angolo}", end='\r')
        
        i += 0.1
        time.sleep(0.05) # 20Hz
except KeyboardInterrupt:
    # Riporta il servo al centro prima di chiudere
    ser.write(b"0,0\n")
    ser.close()
    print("\nTest terminato.")