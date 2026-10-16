# 05 — SSH e operação remota

## Preparação e execução local

1. Use Python 3.12 ou superior e instale `uv`.
2. Na raiz do checkout, execute `uv sync` para instalar o pacote e as
   dependências declaradas em `pyproject.toml` e `uv.lock`.
3. Copie `.env.example` para `.env` e configure a porta serial, o modo de entrada
   e, no modo híbrido, o jogador e os dois GPIOs. Mantenha `.env` na raiz;
   variáveis `PONG_*` exportadas no shell têm precedência.
4. Para o hardware, siga `04_raspberry_hardware.md`; feche o Monitor Serial do
   Arduino antes de iniciar qualquer processo que leia a porta serial.
5. `uv run task cli` inicia o diagnóstico das entradas; encerre-o com Ctrl+C
   antes de iniciar o servidor.
6. `uv run task run` inicia HTTP e WebSocket. Abra `http://localhost:8888` na
   mesma máquina ou use o IP da máquina que hospeda o servidor.

O frontend é servido diretamente pelo Tornado. Não é necessário npm, build ou
servidor de desenvolvimento JavaScript para executar a aplicação.

## Validação do código

- Python: `uv run task test`, `uv run task lint` e `uv run task type-check`.
  `uv run task test` cobre os testes Python de `test/` e não exige hardware.
- Frontend: com Node.js instalado, execute
  `node --test pong/web/tests/*.test.js`. O comando usa o runner nativo
  `node:test` e não requer instalar pacotes npm.
- `uv run task format` aplica formatação Python e altera arquivos. Só oriente o
  aluno a executá-lo quando a etapa de implementação pedir formatação; o agente
  não deve executar formatação nem editar arquivos do projeto.

## Conexão

Nunca invente host, usuário ou senha. Solicite os dados ao aluno e prefira
autenticação por chave. O formato geral é:

```text
ssh <usuario>@<ip-da-raspberry>
```

Antes de executar comandos, confirme que a sessão está na Raspberry verificando
hostname, sistema operacional e versão do Python.

## Cópia do checkout atual

Se o código local ainda não foi publicado em um commit remoto, oriente a cópia
do checkout por um mecanismo explícito, como `rsync` ou `scp`, sempre usando um
diretório de destino conhecido. Se o repositório remoto já estiver atualizado,
prefira `git clone` ou `git pull` dentro da Raspberry.

Não copie `.venv`, caches, `.env` ou chaves privadas. O `.env` deve ser criado e
preenchido diretamente na Raspberry.
Variáveis `PONG_*` exportadas no shell têm precedência sobre os valores do `.env`;
ao diagnosticar configurações inesperadas, confira ambas as fontes.

## Execução remota

Depois de entrar na Raspberry:

1. instalar ou verificar `uv`, Python 3.12+ e Git;
2. usar obrigatoriamente `uv sync` para criar o ambiente e instalar as
   dependências, incluindo `gpiozero`;
3. criar `.env` a partir de `.env.example`;
4. executar `uv run task test`, `uv run task lint` e `uv run task type-check`;
5. validar as entradas com `uv run task cli`, sem o servidor aberto para não
   disputar a porta serial;
6. encerrar o diagnóstico e iniciar com `uv run task run`;
7. acessar a aplicação pelo IP da Raspberry na porta configurada.

Não use `pip`, `poetry`, `python -m venv` ou comandos Python diretos para
substituir o fluxo definido pelo projeto. Preserve `uv.lock`; alterações nele
devem ser feitas somente com `uv lock` quando forem necessárias.

Explique o propósito de cada comando antes de fornecê-lo. Não use `sudo` para
executar a aplicação sem necessidade. Para encerrar, use Ctrl+C na sessão do
servidor; não finalize todas as sessões SSH do usuário.

## Segurança

O bind padrão `0.0.0.0` permite acesso pela rede local. Não exponha a porta à
internet sem autorização, autenticação e compreensão do risco. Túneis reversos
devem ser tratados como uma etapa separada, não como requisito para testar o
hardware local.

Explique comandos SSH, `sudo`, instalação de pacotes e acesso à Raspberry antes
de orientar sua execução; mantenha-os no menor escopo possível. Não use comandos
destrutivos amplos como `rm -rf` em diretórios genéricos, nem `killall ssh`; não
encerre outras sessões SSH do aluno. Nunca copie ou registre `.env`, senhas,
tokens ou chaves privadas.
