# 03 — Arquitetura real do Pongino

## Fluxo principal

```text
Settings
  → make_input_source
    → SerialInputSource ou ArduinoRaspInputSource
      → PongState
        → ConnectionManager
          → WebSocket
            → módulos JavaScript do jogo
```

## Camadas existentes

- `pong/config.py`: configurações `PONG_*`, incluindo `input_mode`.
- `pong/domain/`: entidades e normalização, sem dependência de hardware.
- `pong/infra/input/serial/`: protocolo serial do Arduino e reconexão assíncrona.
- `pong/infra/input/buttons/`: adaptador GPIO baseado em `gpiozero`.
- `pong/infra/input/arduino_rasp/`: composição serial + botões.
- `pong/infra/input/factory.py`: seleciona uma única fonte de entrada.
- `pong/protocols/`: contratos para fonte de entrada e leitor de botão.
- `pong/cli/server.py`: bootstrap do servidor, sem conhecer detalhes GPIO.
- `pong/cli/pots.py`: diagnóstico das leituras.
- `pong/api/`: HTTP, WebSocket e transmissão do estado.
- `pong/web/`: interface e controles locais por teclado.

## Modos de entrada

### `arduino`

O Arduino envia dois valores no formato existente `valor1`, `;`, `valor2`. Os
dois valores formam o `PongState`.

### `arduino_rasp`

O Arduino continua enviando os dois valores. O parser consome ambos para manter
o sincronismo, mas a fonte utiliza somente o jogador do potenciômetro que
permaneceu no Arduino. O jogador configurado em `PONG_BUTTON_PLAYER` é produzido
pelos dois botões GPIO.

O servidor não deve instanciar GPIO diretamente. A fábrica seleciona a fonte e
a própria fonte cria os leitores durante `start()`.

## Regras de dependência

- O domínio não importa `gpiozero`, `serial_asyncio`, Tornado ou código de CLI.
- O servidor depende do contrato de fonte, não de um dispositivo específico.
- A dependência GPIO deve ser carregada apenas no caminho `arduino_rasp`.
- Fakes e testes não devem exigir uma Raspberry conectada.
