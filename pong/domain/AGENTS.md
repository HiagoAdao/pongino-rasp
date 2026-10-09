# Instruções do domínio

- Mantenha o domínio independente de `gpiozero`, `serial_asyncio`, Tornado,
  Pydantic Settings e comandos de terminal.
- Coloque aqui invariantes, normalização, leituras e estado do jogo.
- Prefira funções determinísticas e objetos imutáveis quando isso simplificar o
  raciocínio.
- Teste limites, conversões e estados sem hardware ou rede.
