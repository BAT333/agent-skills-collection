# AGENTS.md — Regras para Agent Skills

## 1. Objetivo

Este diretório armazena Agent Skills reutilizáveis, organizadas por especialidade e finalidade.

Cada Skill deve fornecer conhecimentos ou procedimentos que possam ser utilizados por agentes em diferentes tarefas.

## 2. Estrutura recomendada

Cada Skill deve possuir seu próprio diretório.

```text
skills/
└── nome-da-skill/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── assets/
```

Utilize apenas os diretórios complementares necessários.

O arquivo `SKILL.md` é o ponto de entrada da Skill.

## 3. Padrões de criação

- Utilize nomes descritivos em kebab-case.
- Defina claramente o propósito da Skill.
- Utilize frontmatter YAML conforme o padrão de Agent Skills.
- Escreva instruções objetivas e acionáveis.
- Organize procedimentos em etapas.
- Inclua exemplos quando contribuírem para a compreensão.
- Evite instruções genéricas ou ambíguas.
- Não concentre conhecimentos sem relação entre si na mesma Skill.

## 4. Reutilização

- Desenvolva Skills independentes sempre que possível.
- Evite dependências desnecessárias entre Skills.
- Reutilize referências existentes.
- Não duplique procedimentos já documentados.
- Utilize arquivos complementares quando o conteúdo principal ficar extenso.

## 5. Segurança

- Não inclua credenciais ou tokens.
- Analise comandos antes de recomendar sua execução.
- Identifique operações destrutivas.
- Não presuma permissões que o agente não possui.

## 6. Validação

Antes de considerar uma Skill concluída:

1. Verifique a estrutura de diretórios.
2. Valide o frontmatter YAML.
3. Confira o nome e a descrição.
4. Revise a clareza das instruções.
5. Verifique os caminhos dos arquivos complementares.
6. Confirme que os exemplos estão coerentes.
7. Identifique requisitos e limitações.

## 7. Documentação

Quando adicionar ou modificar uma Skill:

- Atualize a documentação principal, quando necessário.
- Explique o objetivo e a utilização da Skill.
- Informe dependências e limitações.
- Não declare que a Skill foi testada sem realizar a validação.
