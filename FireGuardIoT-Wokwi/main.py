from sensores import ler_sensores
from atuadores import atualizar_leds, controlador_buzzer
from monitoramento import avaliar_risco
import time


print("================================")
print(" FireGuard IoT - MicroPython")
print("================================")

status_anterior = None

contador_seguro = 0
contador_atencao = 0
contador_emergencia = 0

while True:
    temperatura, umidade, gas = ler_sensores()

    status, motivos = avaliar_risco(temperatura, gas)

    if status != status_anterior:
        print("================================")
        print("Status alterado para:", status)
        print("================================")

    print("Motivos:")
    if len(motivos) == 0:
        print("- Ambiente dentro dos parametros")
    else:
        for motivo in motivos:
            print("-", motivo)
        
    
    status_anterior = status

    atualizar_leds(status)

    controlador_buzzer(status)

    print("Status:", status)
    
    if status == "SEGURO":
        contador_seguro += 1
    elif status == "ATENCAO":
        contador_atencao += 1
    elif status == "EMERGENCIA":
        contador_emergencia += 1

    print("=================================")
    print("Seguro:", contador_seguro)
    print("Atencao:", contador_atencao)
    print("Emergencia:", contador_emergencia)
    print("=================================")
    print("\n\n\n\n\n")
    time.sleep(2)