# Instruções da infraestrutura

- `infra/` implementa adaptadores concretos para os contratos do projeto.
- Dependências externas devem ficar nesta camada e ser convertidas para tipos
  do domínio ou protocolos locais.
- Todo recurso aberto precisa de `start()`/`stop()` ou ciclo de vida equivalente.
- Erros de hardware devem preservar contexto e não ser silenciosamente ignorados.
- Não mova regras de jogo para adaptadores de entrada.
