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
$ sudo systemctl stop home-assistant@homeassistant.service 
$ sudo su -s /bin/bash homeassistant
$ source /srv/homeassistant/bin/activate
$ pip3 install --upgrade homeassistant
$ exit
$ sudo systemctl start home-assistant@homeassistant.service
```

