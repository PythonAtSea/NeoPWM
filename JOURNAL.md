# NeoPWM, the best LED controller in *FTC*

## 5/17/25, 4 hours
### General Idea
In the *FIRST* Tech Challenge, people often want LEDs on their robot for driver feedback and for looks. There isn't a great way to control neopixel, because I²C is *really* slow. REV made the [REV Blinkin](https://www.revrobotics.com/rev-11-1105/), which allows for control over PWM, but you can't do very much configuartion, and you have to run it on the main robot battery. For high level teams with tons of other devices, this isn't feasible. The NeoPWM will allow for advanced configuration over USB, super fast control using PWM, and power using a 5V USB power bank. 
![overall diagram](https://github.com/user-attachments/assets/74077d70-7bf5-4275-93e0-2e6ccef1b2a3)
### *FTC* Rule stuff
Because there will be two ground planes (the robot battery and the USB battery), I will need to use a optocoupler to pass the PWM signal to the MCU, which will be powered by the USB battery. Because it contains a programable MCU, in order for it to be legal, it needs to be a Commercial Off the Shelf (COTS) component, so essentially I need to design it, and then sell it and get a EIN and a bunch of annoying legal paperwork. :sob:
### USB-C Port
I want to use a USB-C port for firmware updates and such, as well as for power during standard operations. I think the [TYPE-C-31-M-12](https://jlcpcb.com/partdetail/Korean_HropartsElec-TYPE_C_31_M12/C165948) by Korean Hroparts Elec might be a decent option, it supports USB 2.0 and basic power mode config, so I can pull 15w of power by pulling CC1 and CC2 to ground.
### MCU
I think that a RP2040 is probably the right choice, given the amazing documatation and community support. It's also pretty cheap on JLC, being less than a dollar if you order more than 10. 
### KiCAD VCS
KiCAD 9.0 supports git, so I can just make the NeoPWM the base folder for the KiCAD project. Yay!
### Starting on the schematic
I started working on the RP2040 part of the device, and finshing the power input, USB-C port, the crystal oscillator, and the 16Mb flash module (which is a basic part on JLC yay!)
![schematic](https://github.com/user-attachments/assets/0e8739b9-67ba-4f71-9daf-3cff128294e6)

