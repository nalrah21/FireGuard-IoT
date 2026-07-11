from machine import Pin, PWM
import time

# LEDs
led_verde = Pin(18, Pin.OUT)
led_amarelo = Pin(19, Pin.OUT)
led_vermelho = Pin(23, Pin.OUT)

# Buzzer no GPIO 25
buzzer = PWM(Pin(25))
buzzer.duty(0)


def atualizar_leds(status):
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

    if status == "SEGURO":
        led_verde.on()
    elif status == "ATENCAO":
        led_amarelo.on()
    elif status == "EMERGENCIA":
        led_vermelho.on()


def controlador_buzzer(status):
    if status == "SEGURO":
        buzzer.duty(0)
    elif status == "ATENCAO":
        buzzer.freq(1000)
        buzzer.duty(512)
        time.sleep(0.2)
        buzzer.duty(0)
    elif status == "EMERGENCIA":
        buzzer.freq(2000)
        buzzer.duty(512)