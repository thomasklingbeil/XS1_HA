import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

import requests
import json

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'xs1'

# configuration keys
KEY_HOST = 'host'
KEY_USER = 'user'
KEY_PASSWORD = 'password'

# configuration values
HOST = ''
USER = ''
PASSWORD = ''

# define configuration parameters
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(KEY_HOST): cv.string
    }),
}, extra=vol.ALLOW_EXTRA)


# XS1 API commands
COMMAND_GET_LIST_ACTUATORS = 'get_list_actuators'
COMMAND_GET_LIST_SENSORS = 'get_list_sensors'

def setup(hass, config):
    # read configuration
    global HOST
    global USER
    global PASSWORD
    
    HOST = config[DOMAIN].get(KEY_HOST)
    USER = config[DOMAIN].get(KEY_USER, '')
    PASSWORD = config[DOMAIN].get(KEY_PASSWORD, '')
    
    # set host
    hass.states.set('xs1.host', HOST)
    
    initializeActuators(hass);
    
    initializeSensors(hass);

    return True

"""
Requests the list of actuators and updates their status on home assistant
"""
def initializeActuators(hass):
    actuators = sendRequest(COMMAND_GET_LIST_ACTUATORS)
    
    for actuator in actuators['actuator']:
        name = actuator['name']
        id = actuator['id']
        type = actuator['type']
        value = actuator['value']
        newValue = actuator['newvalue']
        unit = actuator['unit']
        
        if type != 'disabled':
            hass.states.set('xs1.actuator_' + str(id) + '_' + str(name), str(value))
        
        
"""
Requests the list of sensors and updates their status on home assistant
"""
def initializeSensors(hass):
    sensors = sendRequest(COMMAND_GET_LIST_SENSORS)
    
    for sensor in sensors['sensor']:
        name = sensor['name']
        id = sensor['id']
        type = sensor['type']
        value = sensor['value']
        unit = sensor['unit']
        timestamp = sensor['utime']
        
        if type != 'disabled':
            hass.states.set('xs1.sensor_' + str(id) + '_' + str(name), str(value))
    

"""
Sends a request to the XS1 Gateway and returns the answer as a JSON object
"""
def sendRequest(command):
    # create request url
    requestURL = 'http://' + HOST + \
                    '/control?user=' + USER + \
                    '&pwd=' + PASSWORD + \
                    '&cmd=' + command + \
                    '&callback=cname'
    
    # make request
    response = requests.get(requestURL, auth=(USER, PASSWORD))
    responseText = str(response.text)
    responseText = responseText[responseText.index('{'):responseText.rindex('}')+1]  # cut out valid json response
    
    return json.loads(responseText) # convert to json object
    
    
    
    
    
    
    