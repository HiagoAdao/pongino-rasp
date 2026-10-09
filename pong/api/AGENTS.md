# Instruções da API

- `api/` contém transporte HTTP e WebSocket, não regras de negócio nem GPIO.
- Preserve handlers pequenos e assíncronos; não bloqueie o event loop.
- Use `PongState` e os serializers existentes para transportar estado.
- Não importe `gpiozero`, `serial_asyncio` ou fontes concretas nesta camada.
- Teste conexões, mensagens e encerramento usando objetos fake.
