# Adafruit MatrixPortal LED Message Board
## Purpose
Create an LED message display board that is connected to an MQTT broker to show variable message text and a border. In my personal use case, since I work from home full-time, I 
wanted a way to alert my family members that I was unavailable due to being in a virtual meeting/phone call.

In my setup, the MQTT broker is the Mosquitto broker add-on for an existing Home Assistant instance, but theoretically any MQTT broker and host could be made to work. I have only 
tested this with HomeAssistant, however.

## MatrixPortal Setup

This code is written for the Adafruit MatrixPortal M4 board, running CircuitPython 6.3.0. For information on this board and to download the correct CircuitPython version, visit
https://circuitpython.org/board/matrixportal_m4/

Then, follow the instructions on how to install CircuitPython on the board:
https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython#installing-circuitpython

## Dependencies
Download the CircuitPython libraries that are compatible with 6.3.0 from https://circuitpython.org/libraries

The list of libraries in that bundle needed to run the code in this repo is:
* adafruit_bus_device
* adafruit_display_shapes
* adafruit_display_text
* adafruit_esp32spi
* adafruit_io
* adafruit_matrixportal
* adafruit_minimqtt
* adafruit_portalbase
* adafruit_fakerequests.mpy
* adafruit_requests.mpy
* neopixel.mpy

## Configuration - Home Assistant
First, install and configure the Mosquitto Broker add-on for HomeAssistant if you've not already done so.

Next, we will configure two scripts in Home Assistant - one to send a message, and another to send the opposite of that message. Basically, the 'On' and 'Off' state of the board.
Create a pair of scripts that send a message - in this example "On a Call" or "Not On a Call", and an appropriate action - "on", or "off". These message/action payloads are 
published to the topic "homeassistant/message-board/1/meeting":

```
mqtt_in_a_meeting_on:
  alias: Publish "On a Call" notification
  sequence:
  - service: mqtt.publish
    data:
      topic: home-assistant/message-board/1/meeting
      payload: '{ "message": "On a Call", "action": "on" }'
  mode: single
mqtt_in_a_meeting_off:
  alias: Publish "Not On a Call" notification
  sequence:
  - service: mqtt.publish
    data:
      topic: home-assistant/message-board/1/meeting
      payload: '{ "message": "Not On a Call", "action": "off" }'
  mode: single
```

The 'message' of the payload is what gets displayed on the LED Matrix, and the 'action' determines whether or not Matrix is lit - "on" makes it show the border and text, "off" hides them. 
You could send the action "on" for both states, which would mean that one message would be shown or the other would be shown. I have mine simply turning off when I am "Not On a Call". 
Save these scripts to whatever file that houses other scripts in your Home Assistant instance. By default, I believe it is simply /config/scripts.yaml

Then, we will configure two entities in Home Assistant:
* An "input boolean" that will be used to track the 'state' of our message board; and
* A "template switch" that will toggle the state of the input boolean, and trigger the appropriate script for each 'state'

Create a new file called "/config/input_boolean.yaml" (if it does not already exist) and create a new entry in that file that looks something like:

```
in_a_meeting:
  name: On a Call
  initial: off
```

The main outdented value is the system name of this input_boolean, and the 'name' property will be used for display purposes.

Then, create a new file called "/config/switch.yaml" (if it does not already exist) and create a new entry in that file that ties the scripts and input_boolean together:

```
- platform: template
  switches:
    in_a_meeting:
      friendly_name: On a Call
      value_template: "{{ is_state('input_boolean.in_a_meeting', 'on') }}"
      turn_on:
        - service: input_boolean.turn_on
          entity_id: input_boolean.in_a_meeting
        - service: script.mqtt_in_a_meeting_on
      turn_off:
        - service: input_boolean.turn_off
          entity_id: input_boolean.in_a_meeting
        - service: script.mqtt_in_a_meeting_off
```

Basically, what this switch does, is toggle the 'state' of our 'in_a_meeting' input_boolean, and trigger the appropriate script for that 'state'. This switch will now be available 
on the Home Assistant UI dashboards as an entity card.

## Configuration - MatrixPortal
The code running on the MatrixPortal was written to be configurable in two ways. There is a 'secrets.py' file which is intended to house sensitive information like your WiFi credentials
as well as the MQTT credentials. This repo has a 'secrets-example.py' file that outlines the expected format. The CircuitPython libraries for connecting to WiFi expect an object called 
'secrets' with the properties 'ssid' and 'password'. This repo has also added an object called 'mqtt' that is used to configure the connection to your MQTT broker. The full file should 
look like this, with the appropriate values filled in:

```
secrets = {
    'ssid' : '', # WiFi network name
    'password' : '' # WiFi network password 
}

mqtt = {
    'broker': '', # MQTT broker url or ip address
    'user': '', # MQTT user name
    'password': '' # MQTT user password
}
```

Additionally, there is a 'config.py' file that is intended for less sensitive information. This is where you will create a new object called 'feeds' containing any MQTT topics you want the 
MatrixPortal to subscribe to. An example of this is also included in the repo - change the name to something meaningful, if desired, and value to match the topic you are publishing to from 
Home Assistant:

```
feeds = {
    'meetings': 'home-assistant/message-board/1/meeting'
}
```
