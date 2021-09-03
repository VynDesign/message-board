import adafruit_minimqtt.adafruit_minimqtt as MQTT

from secrets import mqtt

mqtt_service = MQTT.MQTT(
    broker=mqtt.get('broker'),
    username=mqtt.get('user'),
    password=mqtt.get('password'),
    port=1883,
)

def subscribe(socket, network):
    try:
        MQTT.set_socket(socket, network._wifi.esp)
        mqtt_service.is_connected()
    except MQTT.MMQTTException:
        mqtt_service.connect()

    from config import feeds
    for feed in feeds.values():
        mqtt_service.subscribe(feed, 1)

    return mqtt_service
