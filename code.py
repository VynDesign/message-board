import json
import adafruit_minimqtt.adafruit_minimqtt as MQTT

import borders
import mqtt_service
import matrixportal_service

print('     MatrixPortal Message Board')

last_data = {}

matrixportal = matrixportal_service.create_matrixportal()
display = matrixportal.display
network = matrixportal.network
colors = matrixportal_service.set_colors()
parent_group = matrixportal_service.create_grid(colors)
message_label = matrixportal_service.create_text_label(colors[2], parent_group, display)
border_group = borders.caution(colors[2])
border_group.hidden = True
parent_group.append(border_group)
display.show(parent_group)

matrixportal_service.set_label_text(message_label, 'Connecting', colors[2], display, False)

network.connect()
if (network._wifi.is_connected):
    message_label.hidden = True
    print('Connected to wifi')

def message_received(client, topic, message):
    print('Received {} for {}'.format(message, topic))
    last_data[topic] = message
    payload = json.loads(message)
    action = payload.get('action')
    hide = action != 'on'
    text = '' if hide else payload.get('message')
    matrixportal_service.set_label_text(message_label, text, colors[1], display, hide)
    border_group.hidden = hide
    parent_group.hidden = hide

# --- MQTT setup ---
queue = mqtt_service.subscribe(network._wifi.esp)
queue.on_message = message_received

# --- main loop ---
while True:
    try:
        queue.is_connected()
        queue.loop()
    except (MQTT.MMQTTException, RuntimeError):
        network.connect()
        queue.reconnect()
