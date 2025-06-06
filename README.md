# NeoPWM
### The best led controller for FTC
> [!NOTE]
> This is a [Highway](https://highway.hackclub.com) project, if you're here from slack (or just want to see the process of development) see [JOURNAL.md](https://github.com/PythonAtSea/NeoPWM/blob/main/JOURNAL.md), for the BOM see INSERT LINK HERE

The NeoPWM is a PWM controlled, USB-C powered, highly configurable SK6812/WS2801 (NeoPixel) controller designed for the _FIRST_ Tech Challenge (FTC). It will have a web based tool to generate configuration files and send over a serial interface. It will have poweron and PWM signal loss states, which allow led patterns to be triggered after a match and during the transition period. It also has a optional intergrated LED panel with 12 SK6812 LEDs, which will have prebuilt patterns. 

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

> [!CAUTION]
> This project has not been built physically, so it may or may not work as intended.
