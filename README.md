# Video installation instructions:
https://drive.google.com/file/d/10iKy3b76b-TXIiM07xIRQXwXXXEDGK18/view

# Demo of the Image Recognition:
https://drive.google.com/file/d/1MpDJM1vwmq-47Gfrhqz_TaW3gFaYXgjd/view

# M2M project using ML For Image Recognition

Execute `ls /dev/ttyUSB*` to check if the device is found

**Update firmware :**

Download kflash_gui and you will get a zip file.
https://github.com/sipeed/kflash_gui/releases
Firmware files have the .bin or .kfpkg extension

**Check firmware version:**

Open serial terminal tool with `sudo minicom`, push reset button of board
configure serial tools : https://maixpy.sipeed.com/en/get_started/serial_tools.html


**To download pretrained models from maixhub :**

connect via terminal `sudo minicom`
flash the device with https://en.bbs.sipeed.com/uploads/default/original/1X/bca0832bed92a1ada63bd05327688784e2ef14d1.zip
you can find the bin in this repos in the folder MaixBit resources/get-maixPy-key
The key is printed in the terminal
[follow this tutorial for more details](https://blog.sipeed.com/p/1338.html)

It help us download pretrained facial recognition model : https://www.maixhub.com/index.php/index/index/detail/id/235

**Note:** 
That using the IDE is working only if the current firmware support that, which is not the case for the firmware running the model, so instead upload the code using the terminal.

**Quick guide for using Terminal to upload the code:**
- `sudo minicom`
-   Copy the code
-   Type in `Ctrl+E` to allow multiLine
-   Paste code
-   Type in `Ctrl+D` to execute code
