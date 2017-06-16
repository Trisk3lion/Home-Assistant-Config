import logging
import threading
import time
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_MAC, CONF_NAME, EVENT_HOMEASSISTANT_STOP)
from nuimo import Controller, ControllerManager, ControllerListener, LedMatrix

REQUIREMENTS = ['nuimo==0.3.2']

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'nuimo_controller'
EVENT_NUIMO = 'nuimo_input'

DEFAULT_NAME = 'None'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_MAC): cv.string,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    conf = config[DOMAIN]
    mac = conf.get(CONF_MAC)
    name = conf.get(CONF_NAME)
    NuimoThread(hass, mac, name).start()
    return True

class NuimoListener(ControllerListener):
    def __init__(self, controller, hass, name):
        _LOGGER.debug("listener started")
        self.controller = controller
        self._hass = hass
        self._name = name
        self.nuimomode = 1
        self.HOMEASSIST_LOGO = (
                 "    .    " +
                 "   ...   " +
                 "  .....  " +
                 " ....... " +
                 "..... ..." +
                 " ....... " +
                 " .. .... " +
                 " .. .... " +
                 ".........")
        self.PRESS_1_LOGO = (
                 "         " +
                 "         " +
                 "    .    " +
                 "  .   .  " +
                 " .     . " +
                 "  .   .  " +
                 "    .    " +
                 "         " +
                 "         ")
        self.PRESS_2_LOGO = (
                 "         " +
                 "         " +
                 "    .    " +
                 "  .....  " +
                 " ....... " +
                 "  .....  " +
                 "    .    " +
                 "         " +
                 "         ")
        self.TURN_UP_LOGO = (
                 "         " +
                 "    .    " +
                 "  . . .  " +
                 " .  .  . " +
                 ".   .   ." +
                 "    .    " +
                 "    .    " +
                 "    .    " +
                 "         ")
        self.TURN_DOWN_LOGO = (
                 "         " +
                 "    .    " +
                 "    .    " +
                 "    .    " +
                 ".   .   ." +
                 " .  .  . " +
                 "  . . .  " +
                 "    .    " +
                 "         ")
        self.MODE_ONE= (
                 "         " +
                 "    .    " +
                 "   ..    " +
                 "  . .    " +
                 " .  .    " +
                 "    .    " +
                 "    .    " +
                 " ....... " +
                 "         ")
        self.MODE_TWO = (
                 "         " +
                 "   . .   " +
                 " .    .  " +
                 "      .  " +
                 "     .   " +
                 "    .    " +
                 "  .      " +
                 " ....... " +
                 "         ")

    def connect_succeeded(self):
        _LOGGER.debug("Sending matrix")
        self.controller.display_matrix(LedMatrix(self.HOMEASSIST_LOGO), interval=3.0, brightness=1.0, fading=True)

    def received_gesture_event(self, event):
        _LOGGER.debug(event)
        if str(event.gesture) == "Gesture.ROTATION":
            if event.value > 0:
                self._hass.bus.fire(EVENT_NUIMO,{'name': str(event.gesture), 'value': 'RIGHT', 'mode': str(self.nuimomode)})
                self.controller.display_matrix(LedMatrix(self.TURN_UP_LOGO), interval=0.5, brightness=1.0, fading=True)
            else:
                self._hass.bus.fire(EVENT_NUIMO,{'name': str(event.gesture), 'value': 'LEFT', 'mode': str(self.nuimomode)})
                self.controller.display_matrix(LedMatrix(self.TURN_DOWN_LOGO), interval=0.5, brightness=1.0, fading=True)
        elif str(event.gesture) == "Gesture.BUTTON_PRESS":
            self._hass.bus.fire(EVENT_NUIMO,{'name': str(event.gesture), 'mode': str(self.nuimomode)})
            self.controller.display_matrix(LedMatrix(self.PRESS_1_LOGO), interval=0.5, brightness=1.0, fading=True)
        elif str(event.gesture) == "Gesture.BUTTON_RELEASE":
            self.controller.display_matrix(LedMatrix(self.PRESS_2_LOGO), interval=0.5, brightness=1.0, fading=True)
        elif "SWIPE" in str(even.gesture):
            if self.nuimomode == 2:
                self.nuimomode = 1
                self.controller.display_matrix(LedMatrix(self.MODE_ONE), interval=0.5, brightness=1.0, fading=True)
            if self.nuimomode == 1:
                self.nuimomode = 2
                self.controller.display_matrix(LedMatrix(self.MODE_TWO), interval=0.5, brightness=1.0, fading=True)

    def stop(self):
        _LOGGER.debug("Disconnected from nuimo")
        self.controller.disconnect()


class NuimoThread(threading.Thread):
    def __init__(self, hass, mac, name):
        super(NuimoThread, self).__init__()
        _LOGGER.debug("started thread")
        self._hass = hass
        self._mac = mac
        self._name = name
        self._hass_is_running = True
        self._nuimo = None
        hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, self.stop)

    def stop(self):
        self._hass_is_running = False

    def run(self):
        while self._hass_is_running:
            if not self._nuimo:
                _LOGGER.debug("starting to conenct")
                self._connect()
            else:
                if not self._nuimo.is_connected():
                    self._nuimo = None
                time.sleep(1)

        if self._nuimo:
            if self._nuimo.listener:
                _LOGGER.debug("disconnecting")
                self._nuimo.listener.stop()
                if manager:
                    manager.stop()
            self._nuimo = None

    def _connect(self):
        manager = ControllerManager(adapter_name='hci0')
        _LOGGER.debug("attempting to connect to %s", self._mac)
        try:
            self._nuimo = Controller(mac_address=self._mac, manager=manager)
            _LOGGER.debug("starting listener class")
            self._nuimo.listener = NuimoListener(controller=self._nuimo, hass=self._hass, name=self._name)
            self._nuimo.connect()
            if self._nuimo.is_connected():
                _LOGGER.debug("connected")
                manager.run()
            else:
                _LOGGER.debug("failed to connect")
                self._nuimo = None
        except Exception as er:
            _LOGGER.debug(er)