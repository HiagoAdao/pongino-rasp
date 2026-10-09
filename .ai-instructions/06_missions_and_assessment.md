# 06 — Missões e avaliação

## Sequência sugerida

1. Confirmar que o modo `arduino` continua funcionando.
2. Explicar `InputSourceProtocol` e `ButtonReaderProtocol`.
3. Validar configuração e seleção exclusiva pela fábrica.
4. Testar debounce, repetição, direção neutra e limites.
5. Preparar Raspberry Pi OS e conectar o Arduino.
6. Ligar os dois botões com pull-up e GND.
7. Executar o modo `arduino_rasp` via SSH.
8. Registrar evidências automatizadas e físicas.

## Perguntas de verificação

- Por que o parser ainda consome dois valores no modo `arduino_rasp`?
- Qual jogador é preservado quando `PONG_BUTTON_PLAYER=1`?
- Por que o servidor usa uma fábrica, mesmo com `gpiozero` sendo uma dependência
  normal do projeto?
- O que o debounce evita?
- Por que a velocidade deve usar o tempo decorrido, e não apenas o número de
  iterações do loop?
- Qual é a diferença entre validar a lógica com fake e validar o circuito real?

## Critérios de conclusão

- Os dois modos iniciam sem alterar o protocolo serial do Arduino.
- O modo com botões movimenta somente o jogador configurado.
- O botão mantido pressionado produz movimento contínuo e limitado.
- Os testes não exigem Raspberry nem GPIO real.
- `uv run task test`, `uv run task lint` e `uv run task type-check` passam.
- A execução física é comprovada com a Raspberry, o Arduino e os botões ligados.
