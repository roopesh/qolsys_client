import main
import appdaemon.plugins.hass.hassapi as hass

class qolsys_panel(hass.Hass):
    def initialize(self):
        main.main()