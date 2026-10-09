# Instruções da entrada Arduino + Raspberry

- Componha `SerialInputSource` e os leitores GPIO sem alterar o protocolo
  serial.
- Consuma os dois valores enviados pelo Arduino, mas use apenas o jogador que
  não foi substituído pelos botões.
- O jogador dos botões é definido por `PONG_BUTTON_PLAYER`.
- Movimento contínuo deve usar tempo decorrido, debounce, direção neutra e
  limites de 0% a 100%.
- Crie os leitores no `start()` e feche tarefa, GPIO e serial no `stop()`.
- Testes usam fakes; a aceitação física exige Raspberry Pi OS, Arduino e
  montagem comprovados.
