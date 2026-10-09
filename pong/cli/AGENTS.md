# Instruções da CLI

- `cli/` é ponto de composição e entrada da aplicação.
- `server.py` deve conhecer configurações, fábrica, API e ciclo de vida, mas não
  detalhes de GPIO ou serial.
- `pots.py` deve permanecer um diagnóstico reutilizando a fábrica de entrada.
- Preserve inicialização e encerramento assíncronos, sinais e logging.
- Execute a aplicação e os diagnósticos com `uv run task ...`.
