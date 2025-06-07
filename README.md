# NeoPWM
### The best led controller for FTC
> [!NOTE]
> This is a [Highway](https://highway.hackclub.com) project, if you're here from slack (or just want to see the process of development) see [JOURNAL.md](https://github.com/PythonAtSea/NeoPWM/blob/main/JOURNAL.md), for the BOM see [BOM.md](https://github.com/PythonAtSea/NeoPWM/blob/main/BOM.md)

##### What is it?
The NeoPWM is a PWM controlled, USB-C powered, highly configurable SK6812/WS2801 (NeoPixel) controller designed for the _FIRST_ Tech Challenge (FTC). It will have a web based tool to generate configuration files and send over a serial interface. It will have poweron and PWM signal loss states, which allow led patterns to be triggered after a match and during the transition period. It also has a optional intergrated LED panel with 12 SK6812 LEDs, which will have prebuilt patterns. 
##### Why did I make it?
In FTC, there was never a great way to control LEDs. YOu could control a strip of leds over I2C using a [I2C to NeoPixel driver](https://www.adafruit.com/product/5766), but the I2C ports on the [REV Control Hub ](https://www.revrobotics.com/rev-31-1595/) are slow, which ruins your loop times which causes problems with odometry. You could use the [REV Blinkin](https://www.revrobotics.com/rev-11-1105/)
 (no that's not a typo) which is controlled over I2C, but you can't do any configuration and it's powered from the main robot battery. The NeoPWM can be powered from a external USB-C battery and will have a web tool to configure the patterns, and it will have a intergrated LED panel like the [CTRE CANdle](https://store.ctr-electronics.com/products/candle), but it will be optional, saving costs for teams who just want a LED strip.
 
**NeoPWM in default configuration without LED panel.**

![image](https://github.com/user-attachments/assets/02de5055-ee8a-48e3-bc93-0edae5d21c3f)

**NeopPWM with intergrated LED panel**

![image](https://github.com/user-attachments/assets/fbd9ea74-4b09-47cd-ba83-390263514754)

**Both PCBs connected with 2mm mousebites**

![image](https://github.com/user-attachments/assets/01e59cb3-def7-4b32-93c8-bb38d14880ce)

**Main schematic**

![image](https://github.com/user-attachments/assets/7c027ed0-51b9-41ee-92bd-1e93dc6bed1c)

**RP2040 circuitry schematic**

![image](https://github.com/user-attachments/assets/50e62bd0-ee1c-43a4-a82c-1fd83d5b0bb9)

## BOM
| Name | Link | Price |
| --- | ---| --: |
| PCB | N/A | $2.00 |
| PCB Assembly | N/A | $31.64 |
| JLC Shipping | N/A | $52.31 |
| JLC Total | N/A | $76.95 |
| JST PH Connector | https://www.digikey.com/en/products/detail/jst-sales-america-inc/S3B-PH-K-S/926627 | $1.31 |
| DuPont connector | https://www.digikey.com/en/products/detail/amphenol-cs-fci/68604-403HLF/5206799 | $1.15 |
| Sk6812 Strip | https://www.digikey.com/en/products/detail/dfrobot/FIT0750/14322609 | $23.62 |
| DigiKey Shipping | N/A | $6.99 |
| DigiKey Total | N/A | $37.91 |
| M2 Screws | https://www.aliexpress.com/item/3256806025233809.html | $1.34 |
| M2 Standoffs | https://www.aliexpress.com/item/3256804631738035.html | $2.46 |
| Aliexpress Total | N/A | $3.80 |

> [!CAUTION]
> This project has not been built physically, so it may or may not work as intended.
