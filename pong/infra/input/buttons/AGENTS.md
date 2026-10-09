# Instruções dos botões GPIO

- Use `gpiozero` como import normal no topo do módulo; não use import dinâmico
  nem fallback para ocultar a dependência.
- Use numeração BCM, pull-up interno e ligação entre GPIO e GND.
- Os objetos GPIO só devem ser criados pelo modo `arduino_rasp` e precisam ser
  fechados no encerramento.
- Se o ambiente não for Raspberry Pi com Raspberry Pi OS, bloqueie a validação
  física e informe a limitação ao aluno.
- O adaptador deve implementar `ButtonReaderProtocol`, sem regras de jogo.
