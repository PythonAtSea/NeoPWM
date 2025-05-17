# NeoPWM, the best LED controller in *FTC*

## 5/17/25 
### General Idea
In the *FIRST* Tech Challenge, people often want LEDs on their robot for driver feedback and for looks. There isn't a great way to control neopixel, because I²C is *really* slow. REV made the [REV Blinkin](https://www.revrobotics.com/rev-11-1105/), which allows for control over PWM, but you can't do very much configuartion, and you have to run it on the main robot battery. For high level teams with tons of other devices, this isn't feasible. The NeoPWM will allow for advanced configuration over USB, super fast control using PWM, and power using a 5V USB power bank. 
![overall diagram](https://github.com/user-attachments/assets/74077d70-7bf5-4275-93e0-2e6ccef1b2a3)
### Interesting details
Because there will be two ground planes (the robot battery and the USB battery), I will need to use a optocoupler to pass the PWM signal to the MCU, which will be powered by the USB battery. Because of the complexity of the device, in order for it to be legal, it needs to be a Commercial Off the Shelf (COTS) component, so essentially I need to design it, and then sell it :sob: and get a EIN and a bunch of annoying legal paperwork.
