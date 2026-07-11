from machine import Pin, ADC
from dht import DHT22

# DHT22 no GPIO 15
dht = DHT22(Pin(15))

# MQ-2 no GPIO 34
mq2 = ADC(Pin(34))
mq2.atten(ADC.ATTN_11DB) # Faixa completa 0-3.3V


def ler_sensores():
  try:
    # Lê o DHT22
    dht.measure()

    temperatura = dht.temperature()
    umidade = dht.humidity()
    fumaca = mq2.read() # Lê o MQ-2

    print("-------------------------------")
    print("Temperatura:", temperatura, "°C")
    print("Umidade:", umidade, "%")
    print("Nivel de Gas/Fumaca:", fumaca)
    print("-------------------------------")

    return temperatura, umidade, fumaca

  except Exception as e:
    print ("Erro ao ler sensores:", e)
    return None, None, None