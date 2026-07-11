# 🔥 FireGuard IoT

Sistema Inteligente de Detecção de Incêndio desenvolvido como projeto prático para aplicar os conhecimentos adquiridos durante a trilha do programa **PNAAT**.

## 📖 Sobre o projeto

O FireGuard IoT é um sistema de monitoramento capaz de identificar possíveis situações de risco de incêndio através da leitura de sensores de temperatura, umidade e gases inflamáveis.

O projeto foi desenvolvido utilizando uma simulação no **Wokwi** com uma placa **ESP32** programada em **MicroPython**, além de um **Dashboard Web** criado com **Flask**, HTML, CSS e JavaScript para visualizar as informações.

O objetivo principal foi integrar conceitos de eletrônica, programação embarcada e desenvolvimento web em um único projeto.


## 🎯 Objetivos

- Aplicar na prática os conhecimentos adquiridos nos cursos do **PNAAT**;
- Desenvolver um sistema IoT utilizando ESP32;
- Trabalhar com sensores simulados no Wokwi;
- Criar um Dashboard Web para visualização dos dados;
- Integrar diferentes tecnologias em um único projeto.


## ⚙️ Tecnologias utilizadas

- ESP32
- MicroPython
- Wokwi
- Flask
- Python
- HTML5
- CSS3
- JavaScript
- JSON


## 🧩 Componentes simulados

- ESP32
- Sensor DHT22 (Temperatura e Umidade)
- Sensor MQ-2 (Gás/Fumaça)
- LEDs indicadores
- Buzzer


## 🚨 Funcionamento

O sistema realiza a leitura dos sensores e classifica o ambiente em três níveis:

- 🟢 Seguro
- 🟡 Atenção
- 🔴 Emergência

Dependendo da situação, os LEDs e o buzzer são acionados para indicar o nível de risco.

O Dashboard apresenta informações como:

- Temperatura
- Umidade
- Nível de gás
- Nível de risco
- Status do ambiente


## 🚧 Melhorias futuras

Durante o desenvolvimento, a proposta inicial era fazer com que os dados gerados pelo ESP32 no Wokwi fossem enviados automaticamente para o Dashboard Web em tempo real.

Nesta primeira versão, o Dashboard utiliza um arquivo JSON para simular a chegada dessas informações.

Como evolução do projeto, pretendo implementar:

- Comunicação em tempo real entre o ESP32 e o Dashboard;
- Envio automático dos dados utilizando HTTP ou MQTT;
- Atualização instantânea da interface;
- Histórico de medições;
- Banco de dados para armazenamento das leituras.


## 👨‍💻 Autor

**Harlan Sá**

Projeto desenvolvido como prática dos cursos do **PNAAT**, com o objetivo de consolidar conhecimentos em Internet das Coisas (IoT), programação embarcada e desenvolvimento web.