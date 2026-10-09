# 04 — Integração com Raspberry Pi

## Ligações

- Use numeração BCM nos pinos configurados.
- Cada botão deve ligar um GPIO ao GND.
- O código usa pull-up interno; pressionado significa nível lógico baixo.
- Não aplique 5 V a um GPIO da Raspberry.
- Os pinos padrão do projeto são GPIO 17 para subir e GPIO 27 para descer,
  mas o `.env` deve ser a fonte de verdade.

## Configuração

No modo físico, revisar:

- `PONG_INPUT_MODE=arduino_rasp`;
- `PONG_SERIAL_PORT=/dev/ttyACM0` ou `/dev/ttyUSB0` conforme o Arduino;
- `PONG_BUTTON_PLAYER=1` ou `2`;
- `PONG_BUTTON_UP_PIN` e `PONG_BUTTON_DOWN_PIN`;
- velocidade, intervalo de leitura e debounce.

Não usar ADC para os botões. O Arduino continua responsável pelo potenciômetro.

## Comportamento esperado

- botão de subir reduz o percentual;
- botão de descer aumenta o percentual;
- manter pressionado gera movimento incremental baseado em tempo;
- soltar interrompe o movimento;
- ambos pressionados resultam em direção neutra;
- a posição é limitada entre 0% e 100%.

## Diagnóstico

Antes de culpar o código, verificar alimentação, GND comum, numeração BCM,
porta serial, permissões do usuário no grupo `dialout` e a instalação do extra
`raspberry`. Um teste com fake valida a lógica, mas não prova que a montagem
física está correta.
