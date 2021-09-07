import board
import displayio
import terminalio
import json
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.matrixportal import MatrixPortal
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

import borders
import mqtt_service

def center_label(label: label.Label):
    bbx, bby, bbwidth, bbh = label.bounding_box
    # Center the label
    label.x = round(display.width / 2 - bbwidth / 2)
    label.y = display.height // 2

last_data = {}
bitmap = displayio.Bitmap(64, 32, 2)  # Create a bitmap object,width, height, bit depth

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=False)
display = matrixportal.display
color = displayio.Palette(3)  # Create a color palette
color[0] = 0x000000  # black background
color[1] = 0xFF0000  # red
color[2] = 0xCC4000  # amber

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)

parent_group = displayio.Group()  # Create a Group
parent_group.append(tile_grid)  # Add the TileGrid to the Group

message_label = label.Label(terminalio.FONT, text='Connecting', color=color[2])
center_label(message_label)
parent_group.append(message_label)
display.show(parent_group)

network = matrixportal.network
network.connect()
if (network._wifi.is_connected):
    message_label.hidden = True
    print('Connected to wifi')

border_group = borders.caution(color[2])
border_group.hidden = True
parent_group.append(border_group)

def message_received(client, topic, message):
    print('Received {} for {}'.format(message, topic))
    last_data[topic] = message
    payload = json.loads(message)
    action = payload.get('action')

    if (action == 'on'):
        message_label.text = payload.get('message')
        message_label.color = color[1]
        center_label(message_label)
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
