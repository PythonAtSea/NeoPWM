# NeoPWM, the best LED controller in *FTC*
## Non-obvious TODO
- Connect the NeoPixel, PWM, and CC data lines to pins on the rp2040 that makes sense.
- Add a reset button?
- Maybe add buttons for other stuff?
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

## 5/19/25, 5 hours
### Power (ahhhhhhh)
Leds consume a *lot* of power. I want to support using a USB-C battery bank, which should allow this to have minimal performance impact. To do this I have 2 options, use USB PD or pull the CC pins to ground with 5.1kΩ resistors. Using USB PD would allow for a lot of power, up to 5a at 12v = 60w, but it is also very complicated and expensive to implement. The simpler only supplies 3a at 5v = 15w, but that is enough to power 50 leds at full white which should be enough. I will add a software system to manage the power used to ensure it stays below 15w by dimming the LEDs, but this seems like the best idea.
### Optocoupler
I have elected use the LTV-357T for passing the PWM signal from the control hub ground level to the rp2040 ground level, mainly due it's availability on JLC. 
![optocoupler](https://github.com/user-attachments/assets/d499cc51-6d9f-4778-af9e-94dad1f09c68)
### Bom
I went through and got most of the BOM done, still need to add whatever parts I'm gonna be using for the case though. Also whatever parts I realize I need to add in a week.
### 3D Models
I've started to add 3D models to some of the footprints that don't have them, this is mianly to assist in making the case down the road (wow im thinking about future self thats crazy)

![screwterminal](https://github.com/user-attachments/assets/5d45c454-17b1-40fa-977c-55b1701c48e1)
![allmodels](https://github.com/user-attachments/assets/bc9de72c-45de-476d-9b40-7bacfb570281)

### Done with schematic!
I finished the schematic, assigned all the footprints, and made sure it transferred without issue!!
