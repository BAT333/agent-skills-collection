# Gerador de README Tecnico

## Nome

`gerador-readme-tecnico`

## Objetivo

Documentar projetos de software existentes com base em arquivos, codigo e informacoes fornecidos pelo usuario.

## Finalidade

A Skill cria um README.md tecnico revisado em etapas. Ela explica arquivos relevantes individualmente e o funcionamento conjunto do projeto sem implementar ou alterar codigo.

## Quando utilizar

Use esta Skill quando o usuario pedir para:

- criar ou revisar um README.md;
- explicar componentes e arquitetura;
- documentar configuracao, instalacao ou execucao;
- gerar documentacao baseada em evidencias anexadas ou coladas.

## Como acionar

Peça ao agente para usar `gerador-readme-tecnico` ou solicite diretamente a analise de um projeto para gerar seu README. A Skill exige anexos ou codigo disponiveis e autorizacao explicita antes de iniciar.

## Fluxo

1. Confirma insumos e autorizacao.
2. Inventaria e analisa arquivos acessiveis.
3. Explica componentes, arquitetura, fluxo e lacunas.
4. Apresenta uma previa completa para revisao.
5. Incorpora feedback em novas previas.
6. Entrega o README final em Markdown somente apos aprovacao.

## Funcionalidades

- separacao entre fatos observaveis, inferencias e lacunas;
- explicacao de arquivos relevantes e suas relacoes;
- descricao de arquitetura, fluxo de dados e logica de negocio;
- identificacao de configuracao e instrucoes verificaveis;
- perguntas objetivas para lacunas criticas;
- aprovacao explicita antes da entrega final.

## Estrutura

```text
gerador-readme-tecnico/
├── SKILL.md
└── README.md
```

## Arquivos

- `SKILL.md`: instrucoes operacionais, fluxo de aprovacao, regras de evidencia, modelo de README e cenarios de validacao.
- `README.md`: finalidade, acionamento, fluxo e estrutura desta Skill.

Nao ha arquivos auxiliares neste pacote. O fluxo cabe em um `SKILL.md` conciso e nao exige modelos ou referencias separadas.

## Limites

- nao presume que arquivos foram anexados ou que a analise foi autorizada;
- nao executa codigo, testes, builds ou comandos;
- nao implementa ou altera o projeto;
- nao inventa versoes, comandos, variaveis, endpoints ou requisitos;
- nao entrega a versao final sem aprovacao da previa.

## Validacao

Casos cobertos:

1. usuario sem arquivos ou autorizacao;
2. projeto com insumos suficientes;
3. projeto com dados insuficientes ou previa rejeitada.

Os criterios detalhados estao na secao `Cenarios de validacao` do `SKILL.md`.
