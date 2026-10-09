# Instruções do frontend

- `web/` é executado no navegador e não deve conhecer GPIO, serial ou Python.
- Preserve o contrato HTTP/WebSocket definido pela API.
- Mantenha módulos JavaScript pequenos, com responsabilidades separadas e sem
  estado global desnecessário.
- Teste serialização visual, reconexão e interação de teclado no ambiente web.
