import mlx90614  # Importa la librería para el sensor MLX90614
from machine import I2C, Pin  # Importa las clases I2C y Pin de la librería machine

# Configuración del bus I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))  # Crea un objeto I2C en los pines 5 (SCL) y 4 (SDA)

# Inicialización del sensor
sensor = mlx90614.MLX90614(i2c)  # Crea un objeto sensor con el bus I2C configurado

# Lectura de la temperatura ambiente
print(sensor.read_ambient_temp())  # Lee e imprime la temperatura ambiente en grados Celsius

# Lectura de la temperatura del objeto
print(sensor.read_object_temp())  # Lee e imprime la temperatura del objeto en grados Celsius

# Verifica si el sensor tiene zona dual
if sensor.dual_zone:  # Si el sensor tiene zona dual, imprime la temperatura del segundo objeto
    print(sensor.object2_temp)
