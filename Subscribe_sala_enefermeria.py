import paho.mqtt.client as mqtt  # Importa la librería para el cliente MQTT
import time                      # Importa la librería para el manejo del tiempo

# Datos del broker MQTT
mqttBroker = "148.226.18.101"  # Reemplaza con la IP de tu broker MQTT
mqttTopic = "hospital/sala_enfermeria"  # Define el tópico MQTT

# Función que se ejecuta al recibir un mensaje
def on_message(client, userdata, message):
    mensaje_json = str(message.payload.decode("utf-8"))  # Decodifica el mensaje JSON
    print(f"Mensaje recibido: {mensaje_json}")  # Imprime el mensaje recibido
    # Aquí puedes agregar código para procesar el mensaje JSON
    # Por ejemplo, extraer los datos de los pacientes y mostrarlos en una interfaz gráfica

# Crea una instancia del cliente MQTT
client = mqtt.Client("EstacionEnfermeras")  # Define un ID para el cliente
client.on_message = on_message  # Asigna la función on_message al evento de recepción de mensajes
client.connect(mqttBroker)  # Conecta al broker MQTT

client.loop_start()  # Inicia el bucle de red en segundo plano
client.subscribe(mqttTopic)  # Suscribe al tópico de la sala de enfermeras
print(f"Suscrito al tópico: {mqttTopic}")

try:  # Manejo de excepciones para detener el programa con Ctrl+C
    while True:  # Bucle infinito para mantener el cliente escuchando
        time.sleep(1)  # Espera 1 segundo
except KeyboardInterrupt:
    print("Deteniendo el cliente...")
    client.loop_stop()  # Detiene el bucle de red
    print("Cliente detenido.")
