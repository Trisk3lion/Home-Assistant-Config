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
2. Connect the router to the computer.
3. Turn on/plug in the router.
4. Wait for your computer to connect.
5. Start the firmware recovery program.
6. Select the firmware.
7. Unplug the power from the router.
8. Holding down on the reset button, plug in the power to the router.
9. While still holding the button, press the upload button in the recovery program.
10. As soon as the recovery program starts counting out % upload, release the reset button.
11. Wait.
12. After a long time look at the error message and scratch your head.
13. Wait a good 5 minutes more. You'll probably see the lights flash indicating the router is rebooting.
14. Connect to 192.168.1.1 in your web browser.
15. Use whichever procedure you like to reset the nvram.
16. Configure the router and have fun.
```
### Update Pi-Hole

```
pihole -up
```

### New updating commands

```
hassctl update-hass && hassctl config && hassctl restart
```
```
hassctl update-hass
hassctl start
hassctl stop
hassctl error
```
