# 05 — SSH e operação remota

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

## Execução remota

Depois de entrar na Raspberry:

1. instalar ou verificar `uv`, Python 3.12+ e Git;
2. usar obrigatoriamente `uv sync` para criar o ambiente e instalar as
   dependências, incluindo `gpiozero`;
3. criar `.env` a partir de `.env.example`;
4. executar testes e verificações de qualidade sempre com `uv run`;
5. iniciar com `uv run task run`;
6. acessar a aplicação pelo IP da Raspberry na porta configurada.

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
