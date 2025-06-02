---
title: "NeoPWM"
author: "Hudson"
description: "The best LED controller in FTC"
created_at: "2024-03-17"
---
# NeoPWM, the best LED controller in *FTC*
## Non-obvious TODO
- ~~Connect the NeoPixel, PWM, and CC data lines to pins on the rp2040 that makes sense.~~
- Add a reset button?
- Maybe add buttons for other stuff?
- ~~Add mounting holes to the PCB~~
- Make second PCB for intergrated led panel
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

## 5/20/25, 4 hours
### First pass of PCB
I made my first pass of routing the PCB, although there's still a bunch of tiny things i need to do, as well as fixing a *bunch* of DRC errors

![image](https://github.com/user-attachments/assets/26b21c0c-9c73-466a-99b1-3afce71a9fbc)
### Optocoupler swap
I swapped the optocoupler for the [LTV-217-B-G](https://jlcpcb.com/partdetail/liteon-LTV_217_BG/C115450), mainly cause it's a bsic part of JLC, which saves $3. Also it's a SMD part, which makes case design easier because I don't have stuff sticking out of the bottom of the board.

### PCB general layout done
I finished the general layout of the PCB, still need to add mounting holes and a reset button. Still conflicted on whether on not to add a status led. Also KiCAD's 3D view looks soooo cool with raytracing on!

![Raytraced](https://github.com/user-attachments/assets/551a68e3-29e7-4497-acdd-fe4dc3ea19b2)
### Mounting holes
I added some M2 mounting holes, these will attach the PCB to the 3D printed case!

![image](https://github.com/user-attachments/assets/7c372fe3-2e0d-49d4-ad55-1e4e39b13ece)

## 6/1/25, 4 hours
### Minor tweaks
Moved the oscillator around to save some space. Debating whether or not to move the PWM signal input over to save space and make the pcb smaller (and cheaper).

![image](https://github.com/user-attachments/assets/6e8caaf2-24d1-4860-9a69-20fd5fcf3fd2)
### Less minor tweaks
Moved the mounting holes to be in the corners and added a USB-C cable keepout zone. Also added some silkscreen stuff!