import board
import mqtt_service
from adafruit_matrixportal.matrixportal import MatrixPortal
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

last_data = {}

def message_received(client, topic, message):
    print('Received {} for {}'.format(message, topic))
    last_data[topic] = message

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=False)
network = matrixportal.network
network.connect()

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
