# Instruções das fontes de entrada

- `input/` escolhe e implementa fontes que produzem `PongState`.
- A fábrica é o ponto de seleção do modo; o servidor não instancia dispositivos.
- O contrato de entrada deve ser respeitado nos modos Arduino e Arduino +
  Raspberry.
- O modo híbrido deve consumir os dois valores seriais para preservar o
  sincronismo e usar somente o canal complementar aos botões.
- Teste fontes com fakes e valide hardware somente em Raspberry Pi OS.
