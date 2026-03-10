# 1/8 Scale RC Chassis Conversion 🏎️
Converting a vintage internal combustion (IC) chassis into an electric rover.

## Architecture
The system follows a Master-Slave architecture:
- **Master:** Raspberry Pi Zero 2W (Linux/Python) - Handles high-level logic and Bluetooth/WiFi input.
- **Slave:** Raspberry Pi Pico (MicroPython) - Real-time PWM generation and safety failsafes.

## Tech Stack 
- **Languages:** Python 3, MicroPython
- **Communication:** UART @ 9600 bps
- **Control:** PWM (50Hz)