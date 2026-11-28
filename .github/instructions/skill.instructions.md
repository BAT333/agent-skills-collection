---
applyTo: "**"
---

# Governança de Criação de Skills

## 1. Objetivo

Estabelecer um processo obrigatório de aprovação, organização, criação, documentação, validação e versionamento de Skills sempre que a Skill `/criador-de-skills` for acionada.

Cada Skill deverá possuir sua própria documentação, armazenada dentro de sua respectiva pasta.

O README principal não deverá ser utilizado como documentação individual obrigatória das Skills.

## 2. Aprovação obrigatória

Antes de iniciar a implementação:

1. Apresentar o objetivo da Skill.
2. Descrever sua finalidade.
3. Apresentar suas funcionalidades.
4. Propor sua estrutura de arquivos e diretórios.
5. Solicitar aprovação explícita do usuário.

Não iniciar a criação sem aprovação.

## 3. Análise da governança de pastas

Após a aprovação:

1. Analisar a estrutura atual do repositório.
2. Identificar onde as Skills existentes estão armazenadas.
3. Examinar a organização das pastas existentes.
4. Identificar padrões de nomenclatura.
5. Identificar convenções de organização.
6. Verificar como Skills semelhantes foram estruturadas.
7. Identificar os diretórios adequados para a nova Skill.

A estrutura existente deve ser considerada a referência oficial.

Não presumir caminhos ou criar uma nova estrutura de organização sem necessidade.

## 4. Criação da pasta da Skill

Após analisar a governança atual:

1. Criar a pasta principal da Skill no local correto.
2. Utilizar nomenclatura consistente com as demais Skills.
3. Criar o arquivo SKILL.md.
4. Identificar quais subpastas são necessárias.
5. Criar somente as subpastas justificadas pela finalidade da Skill.

Exemplos de subpastas possíveis:

- references/: documentação complementar.
- scripts/: scripts executáveis.
- assets/: recursos e arquivos auxiliares.
- templates/: modelos reutilizáveis.

Esses diretórios são exemplos, não requisitos obrigatórios.

Não criar pastas vazias ou desnecessárias.

## 5. README individual obrigatório

Toda Skill criada deverá possuir seu próprio README.md dentro da pasta principal.

Exemplo:

skills/nome-da-skill/
├── SKILL.md
├── README.md
├── references/
├── scripts/
└── assets/

O README.md deverá documentar:

1. Nome da Skill.
2. Objetivo.
3. Finalidade.
4. Funcionalidades.
5. Quando utilizar.
6. Como acionar.
7. Exemplos de utilização.
8. Estrutura de diretórios.
9. Descrição dos arquivos.
10. Descrição das subpastas.
11. Dependências e requisitos, quando aplicável.

### Regras

- O README deve corresponder à estrutura real da Skill.
- Não documentar arquivos que não existem.
- Não deixar de documentar arquivos e subpastas relevantes.
- Seguir o padrão de documentação identificado no repositório.
- Manter a documentação dentro da própria pasta da Skill.
- Atualizar o README sempre que a estrutura ou funcionalidade da Skill mudar.

## 6. Validação da estrutura

Após a criação:

1. Verificar se a pasta principal está no local correto.
2. Verificar se o SKILL.md está presente.
3. Verificar se o README.md está presente.
4. Validar todas as subpastas criadas.
5. Verificar os arquivos complementares.
6. Conferir referências e caminhos.
7. Conferir se o README representa fielmente a estrutura.
8. Verificar se não existem arquivos duplicados ou desnecessários.

Corrigir problemas encontrados antes de concluir.

## 7. Validação documental

Verificar se:

- O README explica corretamente a finalidade da Skill.
- As instruções de utilização estão claras.
- Os exemplos são válidos.
- Os arquivos estão documentados.
- As subpastas estão documentadas.
- A documentação corresponde à implementação.

O README individual é obrigatório para todas as Skills criadas.

## 8. Commit obrigatório

Após a validação:

1. Revisar o git status.
2. Revisar o git diff.
3. Identificar os arquivos pertencentes à nova Skill.
4. Não incluir alterações não relacionadas.
5. Criar um commit específico.

Seguir o padrão de commits existente no repositório.

Caso não exista, utilizar Conventional Commits.

Exemplo:

feat(skills): cria skill de automação de documentação

O commit deve explicar:

- Qual Skill foi criada.
- Para que serve.
- Quais funcionalidades foram implementadas.
- Quais arquivos e estruturas foram adicionados.
- Qual documentação foi criada.

Não realizar push automaticamente.

Se não houver autorização ou condições para criar o commit, informar a pendência.

## 9. Relatório final

Apresentar:

### Skill criada
Nome e finalidade.

### Localização
Caminho da pasta principal.

### Estrutura criada
Árvore de diretórios e arquivos.

### Documentação
Localização do README individual.

### Validação
Resultado das verificações realizadas.

### Commit
Hash e mensagem do commit.

### Pendências
Problemas ou etapas não concluídas.

## 10. Princípios obrigatórios

- Aprovação antes da implementação.
- Respeito à governança atual de pastas.
- Estrutura organizada e consistente.
- Subpastas criadas conforme necessidade.
- README individual obrigatório.
- Documentação fiel à implementação.
- Validação antes da conclusão.
- Commit descritivo.
- Transparência sobre etapas não executadas.

**Princípio central: cada Skill é um componente independente, organizado, documentado e versionado dentro de sua própria estrutura.**