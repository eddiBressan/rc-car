import serial
import time

# La porta /dev/serial0 punta ai pin GPIO 14/15
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("Invio dati al Pico ogni secondo... Premi Ctrl+C per fermare.")

try:
    conteggio = 0
    while True:
        messaggio = f"Ciao Pico! Messaggio n. {conteggio}\n"
        ser.write(messaggio.encode('utf-8'))
        print(f"Inviato: {messaggio.strip()}")
        conteggio += 1
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
    print("\nTest terminato.")