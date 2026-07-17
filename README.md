# Pico 2W SOS Morse Code LED 📟🆘

![Status](https://img.shields.io/badge/Status-COMPLETE%20-blue?style=for-the-badge)

A lightweight MicroPython program that flashes the onboard LED of the Raspberry Pi Pico 2W to signal "SOS" (`... --- ...`) in Morse code. This is one of my very first projects diving into physical computing and microcontrollers!

## 🚀 Features
* **Accurate Timing:** Uses standard Morse code timing ratios (1 unit for a dot, 3 units for a dash).
* **Hardware Native:** Built specifically to utilize the onboard LED of the Raspberry Pi Pico 2W.
* **Beginner Friendly:** Clean, straightforward code meant to explore loops, delays, and GPIO (General Purpose Input/Output) control.

## 🛠️ Hardware Required
* Raspberry Pi Pico 2W (or standard Pico, just change the LED pin if needed!)
* Micro-USB or USB-C cable (depending on your Pico board version)

## 💻 How to Run It

1. **Set up your IDE:** Download and install [Thonny IDE](https://thonny.org/) (or use the VS Code Pico extension).
2. **Flash MicroPython:** Make sure your Pico 2W is running the latest MicroPython firmware.
3. **Copy the Code:** Open `main.py` from this repository and copy it into your IDE.
4. **Run:** Save the file directly to your Raspberry Pi Pico as `main.py` so it runs automatically whenever the board gets power.

---

*Feel free to check out the code! I am actively learning, so if you have any tips on how to optimize loops or make the timing cleaner, open an issue or a pull request—I'd love to learn from it!*
