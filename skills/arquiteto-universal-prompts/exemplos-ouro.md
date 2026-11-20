# Exemplos de Calibração (Padrão Ouro)

Use estes exemplos como referência para calibrar a clareza dos delimitadores, o nível de rigor e o uso dos blocos obrigatórios e condicionais definidos em `frameworks.md` e `regras-anti-alucinacao.md`.

---

## Exemplo A: Prompt para Criar Outra Skill (5 Blocos + `<especificacao_skill>`)
- **Quando usar como referência:** Quando o objetivo do usuário for desenhar uma nova Skill modular (`SKILL.md` + arquivos `.md` de apoio).
- **Pedido bruto:** "Quero um prompt para criar uma skill que ajuda a revisar código SQL e sugerir melhorias."

```xml
<papel>
Especialista sênior em Engenharia de Contexto e arquitetura de Skills modulares para LLMs, com foco em escopo bem definido, regras verificáveis e arquivos auxiliares limpos.
</papel>

<contexto>
O objetivo é criar uma Skill reutilizável no padrão SKILL.md (com arquivos .md complementares quando necessário) para auditar consultas e scripts SQL enviados pelo usuário, identificando gargalos de performance, riscos de segurança e falhas de lógica.
</contexto>

<tarefa>
Projete a estrutura completa da Skill [NOME_DA_SKILL], definindo o SKILL.md principal, os arquivos de apoio (.md) e os critérios de qualidade da revisão SQL.
</tarefa>

<regras_e_restricoes>
- Mantenha a Skill focada exclusivamente em revisão e otimização de SQL; não inclua criação de aplicações backend, dashboards ou administração de infraestrutura de servidores.
- Exija que cada problema apontado na consulta informe: trecho/linhas afetadas, severidade (Alta / Média / Baixa), motivo técnico e versão otimizada do SQL.
- Baseie-se estritamente no código SQL e no contexto de banco informados. Se faltar informação crítica (como dialeto SQL, volume de dados ou índices existentes), responda "Informação insuficiente nos dados fornecidos" ou use [PREENCHER_VALOR] em vez de presumir o schema.
- Não use adjetivos vagos ("código limpo", "otimizado ao máximo", "análise profunda"); exija critérios objetivos e verificáveis.
- Antes de entregar a resposta final, revise sua saída contra <regras_e_restricoes> e <formato_saida> e corrija qualquer desvio.
</regras_e_restricoes>

<formato_saida>
Entregue:
1. O conteúdo completo do SKILL.md (com frontmatter `name` e `description`, fluxo de execução e regras).
2. A relação dos arquivos .md auxiliares recomendados e a responsabilidade exata de cada um.
3. Um exemplo prático completo mostrando uma consulta SQL de entrada e a saída esperada da Skill.
</formato_saida>

<especificacao_skill>
- Nome curto em kebab-case (ex.: revisor-sql-performance) e descrição clara com gatilho de uso + escopo.
- Responsabilidade única: o que entra no escopo da Skill e o que fica de fora.
- Arquivos de apoio necessários (.md) e ordem/condição de leitura de cada arquivo.
- Fluxo de execução numerado e formato de saída obrigatório.
- Critérios de aceitação: como testar a Skill em 3 cenários reais (consulta lenta, risco de injeção/lógica e dados incompletos).
</especificacao_skill>
