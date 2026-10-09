# Instruções dos testes

- Execute a suíte com `uv run task test`.
- Use fakes, monkeypatches e objetos determinísticos para serial, GPIO, relógio
  e rede; não exija Raspberry ou Arduino conectados.
- Cada teste deve verificar um comportamento observável e permanecer isolado.
- Alterações em configuração, protocolos ou fábrica devem incluir cobertura dos
  caminhos válidos e inválidos.
- Testes aprovados não substituem a evidência de execução física na Raspberry.
