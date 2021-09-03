import board
import displayio
import terminalio
import json
from adafruit_display_text.label import Label
from adafruit_matrixportal.matrixportal import MatrixPortal
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

import borders
import mqtt_service

last_data = {}

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=False)
display = matrixportal.display
network = matrixportal.network
network.connect()

group = displayio.Group()  # Create a Group
bitmap = displayio.Bitmap(64, 32, 2)  # Create a bitmap object,width, height, bit depth
color = displayio.Palette(3)  # Create a color palette
color[0] = 0x000000  # black background
color[1] = 0xFF0000  # red
color[2] = 0xCC4000  # amber

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
group.append(tile_grid)  # Add the TileGrid to the Group

message_label = Label(terminalio.FONT)
border_group = displayio.Group()
border = borders.caution(color[2])
for item in border:
    border_group.append(item)
border_group.hidden = True

group.append(message_label)
group.append(border_group)
display.show(group)

def message_received(client, topic, message):
    print('Received {} for {}'.format(message, topic))
    last_data[topic] = message
    payload = json.loads(message)
    action = payload.get('action')

    if (action == 'on'):
        message_label.text = payload.get('message')
        message_label.color = color[1]
        bbx, bby, bbwidth, bbh = message_label.bounding_box
        # Center the label
        message_label.x = round(display.width / 2 - bbwidth / 2)
        message_label.y = display.height // 2
        message_label.hidden = False
        border_group.hidden = False
    else:
        message_label.hidden = True
        border_group.hidden = True

# --- MQTT setup ---
queue = mqtt_service.subscribe(socket, network)
queue.on_message = message_received

# --- main loop ---
while True:
    try:
        queue.is_connected()
        queue.loop()
    except (MQTT.MMQTTException, RuntimeError):
        network.connect()
        queue.reconnect()
