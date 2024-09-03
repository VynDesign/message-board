import adafruit_minimqtt.adafruit_minimqtt as MQTT
import adafruit_esp32spi.adafruit_esp32spi_socket as socket

from secrets import mqtt

mqtt_service = MQTT.MQTT(
    broker=mqtt.get('broker'),
    username=mqtt.get('user'),
    password=mqtt.get('password'),
    port=1883,
)

def subscribe(radio):
    try:
        MQTT.set_socket(socket, radio)
        mqtt_service.is_connected()
    except MQTT.MMQTTException:
        mqtt_service.connect()

    from config import feeds
    for feed in feeds.values():
        mqtt_service.subscribe(feed, 1)

    return mqtt_service
