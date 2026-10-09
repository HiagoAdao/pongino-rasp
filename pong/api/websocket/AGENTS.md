# Instruções do WebSocket

- Preserve o formato das mensagens e o ciclo de conexão definido pelo cliente.
- `ConnectionManager` coordena conexões; não deve ler serial ou GPIO.
- O serializer deve converter estado de domínio sem alterar regras do jogo.
- Teste conexão, broadcast, desconexão e payloads inválidos com fakes.
