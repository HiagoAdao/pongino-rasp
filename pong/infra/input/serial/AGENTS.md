# Instruções da entrada serial

- Preserve o protocolo existente do Arduino: dois valores e o separador na
  ordem esperada.
- A reconexão deve ser assíncrona e não bloquear o event loop.
- Diferencie timeout, porta indisponível, linha inválida e encerramento normal.
- Não altere o formato serial para resolver a integração com os botões.
- Cubra parser, reconexão e encerramento com testes sem Arduino físico.
