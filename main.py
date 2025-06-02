from machine import Pin, ADC
import time
import dht


PINO_SENSOR = 26 

pin_rele = 27  
rele = Pin(pin_rele, Pin.OUT)


NUMERO_AMOSTRAS = 5

def ler_umidade_solo():
    pino_sensor = Pin(PINO_SENSOR, Pin.IN)
    adc = ADC(pino_sensor)
    adc.atten(ADC.ATTN_11DB)

    somatoria = 0

    for i in range(1, NUMERO_AMOSTRAS + 1):
        leitura_sensor = adc.read()
        somatoria += leitura_sensor
        tensao = leitura_sensor * (5 / 1023)
        print("Amostra {} | Leitura: {} | Tensao: {:.2f}".format(i, leitura_sensor, tensao))
        time.sleep_ms(1000)

    media = somatoria / NUMERO_AMOSTRAS
    return leitura_sensor

def acionar_rele():
    rele.value(1)  
    print("Irrigação ligada")
    time.sleep(5)  
    rele.value(0)  
    print("Irrigação desligada")

while True:
    umidade = ler_umidade_solo()
    print("Umidade do solo:", umidade)

    if umidade > 1500:  
        acionar_rele()

    time.sleep(1)  
