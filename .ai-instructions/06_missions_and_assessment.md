# 06 — Missões e avaliação

Use esta sequência para conduzir o aluno pela implementação híbrida. Apresente
uma missão por vez, explique a responsabilidade e peça a evidência indicada;
nunca transforme a sequência em um patch ou solução completa.

## Sequência de implementação

### 1. Preservar o modo legado e definir a configuração

Leia primeiro `main` e o checkout atual para identificar o comportamento de dois
potenciômetros. O modo `arduino` deve continuar selecionando os dois canais e não
deve criar leitores GPIO. O objetivo adicional do checkout é `arduino_rasp`.

Em `pong/config.py`, o aluno deve introduzir `InputMode` com `ARDUINO` e
`ARDUINO_RASP`, manter o prefixo `PONG_` e declarar os campos seriais, de
potenciômetro, botões e servidor descritos em
`03_project_architecture.md`. Os botões precisam ter validação de pino BCM,
velocidade, intervalo, debounce e posição inicial. No modo híbrido, os dois pinos
são obrigatórios e diferentes; no modo legado, não são obrigatórios.

**Evidência:** explicar defaults, limites e por que a validação dos dois pinos
depende do modo. Cobrir defaults, variáveis `PONG_*`, valores inválidos, pinos
ausentes e pinos repetidos em `test/test_config.py`.

### 2. Generalizar o domínio para leituras de jogador

Em `pong/domain/`, manter `PongState` com sempre duas posições, mas permitir que
cada uma implemente `LeituraJogador`. A leitura precisa identificar jogador,
percentual, timestamp e tipo de entrada. A leitura de potenciômetro e a nova
leitura de botões devem satisfazer esse contrato.

Manter normalização ADC em uma função compartilhada. `ControleBotoes` é uma
entidade pura: valida estado inicial/velocidade, calcula variação usando tempo
decorrido, neutraliza ambos pressionados ou ambos soltos e limita a posição a
0–100%. `IdJogador.oponente` deve expressar a relação entre jogadores sem
aritmética numérica espalhada.

**Evidência:** demonstrar que `PongState` aceita leitura mista e que as regras de
botões não importam GPIO. Cobrir normalização, `oponente`, movimento, neutralidade,
limites e valores inválidos em `test/test_domain.py`: ADC 0 e 1023 mapeiam para 0%
e 100%, leituras fora da faixa e faixa mínima/máxima inválida são rejeitadas, e o
movimento dos botões é limitado. Confirmar as propriedades antigas de `PongState`
e que leituras mistas continuam sendo serializadas no contrato WebSocket em
`test/test_serialization.py`.

### 3. Separar o frame serial da leitura de jogador

Preservar o protocolo do sketch e a reconexão serial existente. A fonte serial
deve emitir `SerialPotentiometerFrame` com os dois percentuais normalizados e o
timestamp do par; ela não escolhe jogadores nem compõe `PongState`.

O parser recebe `A0`, `;`, `A1`, em linhas sucessivas, aceita ADC de 0 a 1023 e
descarta parcial inválido ou fora de ordem. A fonte serial mantém timeout por
linha, atraso de inicialização, limpeza do buffer, estado de conexão,
reconexão após erro de serial/OS e encerramento seguro da tarefa e writer.

**Evidência:** usar testes sem hardware para protocolo válido/inválido, reset,
normalização, timeout, reconexão, cancelamento e ciclo de vida em
`test/test_parser.py` e `test/test_serial_source.py`.

### 4. Implementar fontes e mapeamento dos dois modos

- `ArduinoInputSource` converte os dois canais do frame em leituras dos dois
  jogadores no modo `arduino`.
- `resolver_mapeamento_arduino_rasp` escolhe o jogador complementar e seu canal
  serial/pino. Para botões no jogador 1, usa canal 2/A1; para botões no jogador 2,
  usa canal 1/A0.
- `CompositorEstadoArduinoRasp` converte o canal escolhido em leitura serial,
  combina-a com `LeituraJogadorBotoes` na posição certa e rejeita leituras que
  pertençam ao jogador errado.
- A fábrica instancia somente os componentes do modo selecionado: dois
  potenciômetros para `arduino`; um potenciômetro complementar e leitores GPIO
  para `arduino_rasp`.

**Evidência:** cobrir os dois valores de `PONG_BUTTON_PLAYER`, os pinos/canais
esperados, composição nas duas ordens, rejeição de jogador incompatível, seleção
de modo, rejeição de modo não suportado e ausência de dependência GPIO no modo
legado. Referências:
`test/test_arduino_source.py`, `test/test_mapeamento_arduino_rasp.py`,
`test/test_composicao_arduino_rasp.py` e `test/test_input_factory.py`.

### 5. Integrar botões, composição e ciclo de vida

O adaptador GPIO implementa `LeitorBotoesProtocol` com pull-up, leitura do estado
e fechamento. O monitor híbrido cria dois leitores, amostra conforme o intervalo
configurado, calcula movimento com tempo decorrido e comunica mudanças de posição
ou estado. Ele não deve emitir quadros repetidos quando os controles estão
ociosos.

Use os caminhos atuais em português `pong/protocols/leitor_botoes.py` e
`pong/infra/input/botoes/`; atualize os imports e testes renomeados em vez de
manter uma segunda implementação em `button_reader` ou `buttons`.

`ArduinoRaspInputSource` coordena o monitor, a fonte serial e o compositor. Não
emita estado antes do primeiro frame serial. Na inicialização, falha ao abrir um
leitor ou ao iniciar a serial deve fechar os recursos já abertos. Na parada,
cancele/aguarde a tarefa e feche GPIO e serial; parada antes de iniciar deve ser
segura. Falha da tarefa GPIO deve chegar ao callback de falha.

**Evidência:** usar fakes de serial e GPIO em `test/test_leitor_botoes_gpio.py` e
`test/test_arduino_rasp_source.py` para movimento por tempo, estados neutros,
atualização serial, ausência de estado inicial, ociosidade, falhas de construção
e inicialização, propagação de erro e fechamento de recursos.

### 6. Atualizar diagnóstico e servidor

`pong/cli/input_diagnostics.py` substitui o diagnóstico anterior de
potenciômetros: apresenta a origem de cada jogador, conectividade/frescor serial,
posição percentual e estados/direções/pinos dos botões no modo híbrido. No modo
`arduino`, não mostra GPIO. Atualize a tarefa `cli` em `pyproject.toml` para
iniciar `pong.cli.input_diagnostics`; não mantenha um segundo fluxo de diagnóstico
exclusivo de potenciômetros. A CLI deve parar a fonte em encerramento normal e em
falha.

O servidor usa a fábrica e o contrato de fonte, não cria GPIO. Registre o modo e
o mapeamento ativo. Um callback de falha de entrada deve encerrar a espera do
servidor; o `finally` deve parar HTTP/fonte, fechar conexões WebSocket e remover
handlers de `SIGINT` e `SIGTERM`.

**Evidência:** conferir `test/test_input_diagnostics.py` e `test/test_server.py`
com fakes, incluindo os dois modos e encerramento por falha.

### 7. Dependências e validação integrada

`gpiozero` é dependência de execução e `rich` é necessária à CLI de diagnóstico
no grupo de desenvolvimento. Mudanças em dependências devem atualizar
`pyproject.toml` e `uv.lock` usando `uv`; não editar o lockfile manualmente.

Oriente o aluno a executar `uv run task test`, `uv run task lint` e
`uv run task type-check`. Os testes Python usam fakes, cobertura mínima de 95% e
não comprovam a fiação. Os testes JavaScript são separados:
`node --test pong/web/tests/*.test.js`.

Para a validação física, confirmar Raspberry Pi OS, Arduino enviando o protocolo,
porta serial real, dois botões em GPIO BCM com pull-up, acesso aos GPIOs e
diagnóstico funcional antes do servidor. Registrar separadamente evidências
automatizadas, operacionais e físicas conforme `07_workflow_and_evidence.md`.

## Perguntas de verificação

Adapte as perguntas à missão em andamento; são exemplos, não um questionário
fixo:

- Por que o parser ainda consome os dois canais no modo híbrido?
- Qual canal serial resta quando `PONG_BUTTON_PLAYER=1`? E quando é `2`?
- Por que `PongState` aceita tipos diferentes de leitura?
- Como o ciclo de vida garante que o primeiro leitor GPIO também seja fechado se
  a criação do segundo falhar?
- Por que um fake não comprova pull-up, aterramento ou acesso físico ao GPIO?

## Critérios de conclusão

- `arduino` preserva o comportamento de dois potenciômetros sem instanciar GPIO.
- `arduino_rasp` combina um canal serial complementar e dois botões GPIO sem
  alterar o protocolo do Arduino.
- O estado de cada jogador identifica corretamente origem, percentual e
  timestamp; o movimento por botão usa tempo, neutralidade e limites.
- Configuração inválida é rejeitada antes de iniciar o hardware.
- Inicialização, falha e encerramento liberam os recursos e informam o servidor.
- Testes automatizados usam fakes; validação física só é declarada com hardware
  real na Raspberry Pi OS.
