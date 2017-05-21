# Home-Assistant-Config

This is the basis for my Home Assistant configuration.

## Commands

### Start/Stop/Restart Home Assistant
```
$ sudo systemctl start home-assistant@homeassistant.service
$ sudo systemctl stop home-assistant@homeassistant.service
$ sudo systemctl restart home-assistant@homeassistant.service
```

### Update Home Assistant
```
$ sudo systemctl stop home-assistant@homet.service 
$ sudo su -s /bin/bash homeassistant
$ source /srv/homeassistant/bin/activate
$ pip3 install --upgrade homeassistant
$ exit
$ sudo systemctl start home-assistant@homeassistant.service
```
### Updating N66U router

```

So here are the instructions that worked for me.
Connect the router to the computer.
Turn on/plug in the router.
Wait for your computer to connect.
Start the firmware recovery program.
Select the firmware.
Unplug the power from the router.
Holding down on the reset button, plug in the power to the router.
While still holding the button, press the upload button in the recovery program.
As soon as the recovery program starts counting out % upload, release the reset button.
Wait.
After a long time look at the error message and scratch your head.
Wait a good 5 minutes more. You'll probably see the lights flash indicating the router is rebooting.
Connect to 192.168.1.1 in your web browser.
Use whichever procedure you like to reset the nvram.
Configure the router and have fun.
```
