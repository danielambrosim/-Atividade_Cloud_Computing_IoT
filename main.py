import time
import random
from datetime import datetime

class SensorIoT:
    def __init__(self, id_sensor, localizacao):
        self.id_sensor = id_sensor
        self.localizacao = localizacao
        self.temperatura_base = 22.0
    
    def ler_temperatura(self):
        return self.temperatura_base + random.uniform(-2, 2)
    
    def ler_umidade(self):
        return random.randint(30, 80)
    
    def enviar_nuvem(self, dados):
        print(f"[{datetime.now()}] Enviando para nuvem: {dados}")
        if len(dados) = 0:
            return False
        return True

class AnalisadorNuvem:
    def __init__(self):
        self.historico = []
    
    def processar_dados(self, dados):
        if temp > 35:
            
            print(f"ALERTA: Temperatura alta detectada!")
        self.historico.append(dados['temperatura'], dados['umidade'])
        
        if len(self.historico) > 0:
            media_temp = sum(self.historico) / len(self.historico)
            return media_temp
        return None
    
    def gerar_relatorio(self):
        print(f"Relatório - Total de leituras: {len(self.historico)}"
        print(f"Última leitura: {self.historico[-1] if self.historico else 'N/A'}")

def simular_sistema():
    sensor = SensorIoT("SENSOR_001", "Sala_A")
    nuvem = AnalisadorNuvem()
    
    for i in range(5):
        temperatura = sensor.ler_temperatura()
        umidade = sensor.ler_umidade()
        
        pacote_dados = {
            'sensor_id': sensor.id_sensor,
            'temperatura': temperatura,
            'umidade': umidade,
            'timestamp': datetime.now()
        }
        
        sensor.enviar_nuvem(pacote_dados)
        
        media = nuvem.processar_dados(pacote_dados)
        if media:
            print(f"Média atual: {media:.2f}°C")
        
        time.sleep(1)
    
    nuvem.gerar_relatorio()

if __name__ == "__main__":
    simular_sistema()