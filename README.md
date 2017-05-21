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

1. So here are the instructions that worked for me.
1. Connect the router to the computer.
1. Turn on/plug in the router.
1. Wait for your computer to connect.
1. Start the firmware recovery program.
1. Select the firmware.
1. Unplug the power from the router.
1. Holding down on the reset button, plug in the power to the router.
1. While still holding the button, press the upload button in the recovery program.
1. As soon as the recovery program starts counting out % upload, release the reset button.
1. Wait.
1. After a long time look at the error message and scratch your head.
1. Wait a good 5 minutes more. You'll probably see the lights flash indicating the router is rebooting.
1. Connect to 192.168.1.1 in your web browser.
1. Use whichever procedure you like to reset the nvram.
1. Configure the router and have fun.
```
### Update Pi-Hole

```
pihole -up
```
