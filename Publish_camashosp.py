import paho.mqtt.client as mqtt
import json
import time
import random

# Datos del broker MQTT
mqttBroker = "148.226.18.101"  # Reemplaza con la IP de tu broker MQTT
mqttTopic = "hospital/sala_enfermeria"  # Define el tópico MQTT

# Función para generar datos aleatorios de pacientes
def generar_datos_pacientes():
    camas = []
    for i in range(1, 4):  # Datos para 3 camas
        camas.append({
            "numero_cama": i,
            "paciente": f"Paciente {i}",
            "temperatura": round(random.uniform(36.0, 38.0), 1),
            "presion_arterial": f"{random.randint(110, 140)}/{random.randint(70, 90)}",
            "frecuencia_cardiaca": random.randint(60, 100),
            "spo2": random.randint(95, 100)
        })
    datos = {
        "sala": "A123",
        "camas": camas
    }
    return datos

# Función para conectar al broker MQTT
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado al broker MQTT!")
        else:
            print("Fallo al conectar, codigo de error %d\n", rc)

    client = mqtt.Client("RaspberryPi")
    client.on_connect = on_connect
    client.connect(mqttBroker)
    return client

# Función para publicar los datos
def publish(client):
    while True:
        time.sleep(5)  # Envía datos cada 5 segundos
        datos_pacientes = generar_datos_pacientes()
        mensaje_json = json.dumps(datos_pacientes)  # Convierte los datos a JSON
        result = client.publish(mqttTopic, mensaje_json)
        status = result[0]
        if status == 0:
            print(f"Enviado `{mensaje_json}` al tópico `{mqttTopic}`")
        else:
            print(f"Fallo al enviar el mensaje al tópico {mqttTopic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
