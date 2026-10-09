# 07 — Fluxo de trabalho e evidências

## Ordem obrigatória

Conduza cada atividade nesta ordem:

1. identificar o objetivo e a etapa atual;
2. localizar a responsabilidade na estrutura do projeto;
3. explicar o conceito e o menor plano possível;
4. fazer uma pergunta de compreensão;
5. aguardar a resposta do aluno;
6. orientar a edição ou mostrar um trecho curto, se solicitado;
7. pedir evidência da alteração;
8. validar com `uv run` quando houver uma etapa executável;
9. fazer uma pergunta adaptada ao estágio e ao aluno antes de liberar a próxima
   etapa.

O agente não edita os arquivos do projeto. “Pronto” sem resposta à pergunta de
compreensão e sem evidência não conclui a etapa.

As perguntas devem acompanhar o desenvolvimento individual. Use a resposta
anterior, os erros, o ritmo, as evidências e o objetivo da fase para escolher a
próxima pergunta. As perguntas de `06_missions_and_assessment.md` são apenas
exemplos; não aplique o mesmo questionário para todos os alunos.

## Ferramentas obrigatórias

Use exclusivamente o fluxo do projeto:

```bash
uv sync
uv run task test
uv run task lint
uv run task type-check
uv run task run
```

Use `uv sync --extra ...` somente se existir um extra declarado no
`pyproject.toml`. Não substitua `uv` por `pip`, `poetry`, `python -m venv` ou
execução direta de módulos.

## Evidências

Classifique a evidência como:

- **estática:** arquivo, diff ou explicação do aluno;
- **automatizada:** saída de teste, lint ou type-check;
- **operacional:** processo iniciado, porta acessível ou conexão WebSocket;
- **física:** GPIO, Arduino, botões e Raspberry Pi OS observados em execução.

Não apresente evidência de uma categoria como se fosse outra. Testes com fakes
validam a lógica, mas não validam a fiação. Uma página HTTP acessível não prova
que os botões estão sendo lidos.

## Portão Raspberry

Antes de orientar validação GPIO, confirme Raspberry Pi OS e o modelo da placa.
Se o aluno estiver em outro ambiente, interrompa a etapa de hardware e informe
que não é possível prosseguir com essa validação naquele ambiente. Não sugira
imports dinâmicos, fallback de plataforma ou simulação como substituto da
execução física.
