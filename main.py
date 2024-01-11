import network
import time
from umqtt.simple import MQTTClient

# Parametry sieci Wi-Fi
ssid = ''
password = ''

# Parametry broker MQTT
mqtt_broker = ""
mqtt_port = 1883
mqtt_user = ""
mqtt_password = ""
mqtt_topic = b""

# Utwórz obiekt interfejsu sieciowego
wifi = network.WLAN(network.STA_IF)

# Włącz interfejs sieciowy
wifi.active(True)

# Sprawdź, czy interfejs jest włączony
if not wifi.isconnected():
    print("Łączenie z siecią Wi-Fi...")

    # Połącz z siecią Wi-Fi
    wifi.connect(ssid, password)

    # Czekaj, aż połączenie zostanie ustanowione
    while not wifi.isconnected():
        pass

# Wyświetl informację o połączeniu
print("Połączono z siecią Wi-Fi")
print("IP Address:", wifi.ifconfig()[0])

# Połącz się z brokerem MQTT
mqtt_client = MQTTClient("esp8266", mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_password)
mqtt_client.connect()

# Główna pętla programu
try:
    while True:
        # Publikuj wiadomość na temat co 10 sekund
        message = "Hello, MQTT!"
        mqtt_client.publish(mqtt_topic, message.encode(), qos=2)
        print("Wiadomość wysłana:", message)

        # Poczekaj 10 sekund przed wysłaniem kolejnej wiadomości
        time.sleep(10)

except KeyboardInterrupt:
    print("Program zatrzymany przez użytkownika")

finally:
    # Zamknij połączenie z brokerem MQTT
    mqtt_client.disconnect()

