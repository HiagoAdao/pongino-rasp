# Instruções dos protocolos

- Protocolos definem contratos pequenos e independentes de implementação.
- Use `Protocol` para permitir fakes e substituição de hardware nos testes.
- Não coloque lógica de negócio, GPIO, serial ou dependências de framework nos
  contratos.
- Mudanças de contrato exigem revisar implementações, fábrica e testes.
