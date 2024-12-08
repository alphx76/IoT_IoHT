# JOSE ALFONSO DOMINGUEZ CHAVEZ 1/DIC2024
# EJEMPLO DE USO MQTT Y JSON PARA UNA APLICACIÓN IOHT
# CÓDIGO PARA PUBLICAR

import paho.mqtt.client as mqtt  # Importa la librería para el cliente MQTT
import json                      # Importa la librería para manejar JSON
import time                      # Importa la librería para el manejo del tiempo
import random                    # Importa la librería para generar datos aleatorios

# Datos del broker MQTT
mqttBroker = "148.226.18.101"  # Reemplaza con la IP de tu broker MQTT
mqttTopic = "hospital/sala_enfermeria"  # Define el tópico MQTT

# Función para generar datos aleatorios de pacientes
def generar_datos_pacientes():
    camas = []  # Lista para almacenar los datos de cada cama
    for i in range(1, 4):  # Genera datos para 3 camas
        camas.append({  # Agrega un diccionario con los datos de la cama a la lista
            "numero_cama": i,
            "paciente": f"Paciente {i}",
            "temperatura": round(random.uniform(36.0, 38.0), 1),  # Genera temperatura aleatoria
            "presion_arterial": f"{random.randint(110, 140)}/{random.randint(70, 90)}",  # Genera presión arterial aleatoria
            "frecuencia_cardiaca": random.randint(60, 100),  # Genera frecuencia cardíaca aleatoria
            "spo2": random.randint(95, 100)  # Genera SpO2 aleatorio
        })
    datos = {  # Crea un diccionario con los datos de la sala
        "sala": "A123",
        "camas": camas
    }
    return datos  # Devuelve el diccionario con los datos

# Función para conectar al broker MQTT
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):  # Función que se ejecuta al conectar al broker
        if rc == 0:  # Si el código de retorno es 0, la conexión fue exitosa
            print("Conectado al broker MQTT!")
        else:
            print("Fallo al conectar, codigo de error %d\n", rc)

    client = mqtt.Client("RaspberryPi")  # Crea una instancia del cliente MQTT con un ID
    client.on_connect = on_connect  # Asigna la función on_connect al evento de conexión
    client.connect(mqttBroker)  # Conecta al broker MQTT
    return client  # Devuelve el objeto cliente

# Función para publicar los datos
def publish(client):
    while True:  # Bucle infinito para enviar datos continuamente
        time.sleep(5)  # Espera 5 segundos
        datos_pacientes = generar_datos_pacientes()  # Genera los datos de los pacientes
        mensaje_json = json.dumps(datos_pacientes)  # Convierte los datos a JSON
        result = client.publish(mqttTopic, mensaje_json)  # Publica el mensaje JSON en el tópico
        status = result[0]  # Obtiene el código de resultado de la publicación
        if status == 0:  # Si el código de resultado es 0, la publicación fue exitosa
            print(f"Enviado `{mensaje_json}` al tópico `{mqttTopic}`")
        else:
            print(f"Fallo al enviar el mensaje al tópico {mqttTopic}")

def run():
    client = connect_mqtt()  # Conecta al broker MQTT
    client.loop_start()  # Inicia el bucle de red en segundo plano
    publish(client)  # Publica los datos

if __name__ == '__main__':  # Ejecuta la función run() si el script se ejecuta directamente
    run()
