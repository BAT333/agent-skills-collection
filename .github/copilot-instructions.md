# Instruções do Repositório — Agent Skills Collection

## 1. Contexto e propósito

Este repositório reúne recursos para desenvolvimento, personalização e extensão de assistentes de Inteligência Artificial. Seu objetivo é armazenar, organizar, documentar, versionar e manter recursos reutilizáveis para diferentes projetos e ambientes de desenvolvimento.

Principais recursos:

- **Custom Agents:** agentes especializados em domínios, tarefas ou responsabilidades.
- **Agent Skills:** conhecimentos e procedimentos reutilizáveis.
- **Hooks:** automações executadas em eventos do ciclo de vida dos agentes.
- **Servidores MCP:** integrações que disponibilizam ferramentas e fontes de contexto externas.
- **Instruções e documentação:** regras operacionais, padrões, exemplos e orientações.

## 2. Estrutura do repositório

Respeite a organização existente:

- `agents/`: agentes personalizados, normalmente definidos em arquivos `.agent.md`.
- `skills/`: Skills reutilizáveis, organizadas em diretórios próprios e contendo `SKILL.md`.
- `hooks/`: configurações de Hooks e scripts auxiliares.
- `mcp-servers/`: implementações e recursos relacionados a servidores MCP.
- `testes/`: arquivos e ambientes destinados a testes controlados.
- `README.md`: documentação principal, estrutura e índice dos recursos.
- `CHANGELOG.md`: histórico de alterações relevantes.

Não crie novas pastas na raiz sem necessidade. Antes de propor mudanças estruturais, analise a organização atual e explique a justificativa.

## 3. Diretrizes gerais de trabalho

1. Analise os arquivos e a estrutura existente antes de implementar alterações.
2. Reutilize recursos existentes sempre que forem adequados.
3. Evite duplicação de instruções, regras, funcionalidades e documentação.
4. Preserve a separação de responsabilidades entre Agents, Skills, Hooks e servidores MCP.
5. Priorize soluções modulares, reutilizáveis, documentadas e de fácil manutenção.
6. Não presuma que um recurso funciona apenas porque sua configuração foi criada.
7. Diferencie funcionalidades implementadas, exemplos, experimentos e recursos planejados.
8. Não altere arquivos fora do escopo solicitado.
9. Não substitua configurações existentes sem analisar suas dependências e consequências.
10. Quando houver dúvidas sobre requisitos, compatibilidade ou comportamento, sinalize a incerteza em vez de inventar informações.

## 4. Responsabilidade de cada recurso

### Custom Agents

Agents representam especialistas com identidade, responsabilidades, limites operacionais e ferramentas específicas.

Ao trabalhar com Agents:

- Respeite o padrão de nomenclatura `kebab-case`.
- Utilize o formato `.agent.md`.
- Defina claramente nome, descrição, especialidade e ferramentas permitidas.
- Estabeleça limites de atuação e comportamento esperado.
- Evite transformar um Agent em uma coleção desorganizada de procedimentos.
- Encaminhe conhecimentos e procedimentos reutilizáveis para Skills quando apropriado.

### Agent Skills

Skills representam conhecimentos e procedimentos reutilizáveis que podem ser carregados pelos agentes conforme a necessidade.

Ao trabalhar com Skills:

- Cada Skill deve possuir seu próprio diretório.
- O arquivo principal deve ser `SKILL.md`.
- Utilize nomes descritivos em `kebab-case`.
- Mantenha as instruções principais objetivas e organizadas.
- Utilize arquivos complementares quando o conteúdo justificar essa separação.
- Inclua exemplos e critérios de validação quando forem úteis.
- Evite duplicar conteúdos que já estejam disponíveis em outras Skills.

### Hooks

Hooks executam comandos ou scripts automaticamente em eventos específicos do ciclo de vida do agente.

Ao trabalhar com Hooks:

- Identifique claramente o evento que dispara a execução.
- Avalie os efeitos do comando antes de configurá-lo.
- Prefira scripts pequenos, previsíveis e com responsabilidades específicas.
- Considere falhas, códigos de saída e mensagens de diagnóstico.
- Evite operações destrutivas ou alterações automáticas sem justificativa.
- Não introduza comandos que modifiquem o repositório sem avaliar seus impactos.
- Documente os requisitos e o comportamento esperado.

### Servidores MCP

Servidores MCP disponibilizam ferramentas e contextos externos por meio do Model Context Protocol.

Ao trabalhar com MCP:

- Identifique o transporte utilizado, como `stdio` ou HTTP.
- Documente comandos, argumentos, dependências e variáveis de ambiente.
- Mantenha credenciais, tokens e informações sensíveis fora do versionamento.
- Não invente ferramentas ou capacidades que não estejam implementadas.
- Verifique a compatibilidade entre cliente, servidor e protocolo.
- Considere permissões e limites de acesso aos recursos disponibilizados.
- Priorize testes isolados antes da integração com o assistente.

## 5. Segurança e permissões

A segurança deve ser considerada em todas as alterações.

- Nunca exponha tokens, senhas, chaves privadas ou credenciais.
- Não inclua segredos em exemplos, documentação ou arquivos versionados.
- Utilize variáveis de ambiente ou mecanismos apropriados de gerenciamento de segredos.
- Não conceda permissões excessivas a Agents ou servidores MCP.
- Avalie cuidadosamente comandos executados por Hooks.
- Não execute operações destrutivas sem autorização explícita.
- Não leia, altere ou exponha arquivos fora do escopo autorizado.
- Considere que ferramentas MCP podem ter acesso a arquivos, serviços e dados externos.

## 6. Documentação e padronização

Toda alteração relevante deve manter a documentação correspondente atualizada.

- Utilize Markdown para documentação.
- Preserve o idioma e o padrão já adotados pelo documento.
- Utilize títulos, listas e exemplos para facilitar a compreensão.
- Documente requisitos, instalação, configuração, utilização e limitações.
- Diferencie exemplos ilustrativos de configurações prontas para uso.
- Atualize o `README.md` quando adicionar, remover ou modificar recursos da coleção.
- Atualize o `CHANGELOG.md` quando houver mudanças relevantes.

## 7. Análise, implementação e validação

Antes de implementar uma alteração:

1. Entenda o objetivo solicitado.
2. Analise os arquivos relacionados.
3. Identifique dependências e possíveis impactos.
4. Apresente uma abordagem quando a alteração for estrutural ou envolver riscos.

Durante a implementação:

1. Respeite a estrutura e os padrões existentes.
2. Faça alterações pequenas e relacionadas ao objetivo.
3. Evite mudanças não solicitadas.
4. Mantenha a documentação consistente com a implementação.

Após a implementação:

1. Verifique a estrutura dos arquivos.
2. Valide a sintaxe das configurações.
3. Execute testes apropriados quando disponíveis e autorizados.
4. Informe o que foi alterado.
5. Apresente os testes realizados e seus resultados.
6. Informe limitações ou pontos que ainda precisam de validação.

Nunca declare que algo foi testado ou validado se a verificação não foi realizada.

## 8. Versionamento e commits

Utilize mensagens de commit padronizadas, preferencialmente em inglês, seguindo Conventional Commits.

Exemplos:

- `feat(agents): add java specialist agent`
- `feat(skills): add skill creation workflow`
- `feat(hooks): add session start validation`
- `feat(mcp): add local filesystem server`
- `docs(readme): update resource documentation`
- `fix(skills): correct skill metadata`

Evite commits genéricos, como `update`, `changes` ou `fix`.

## 9. Organização das instruções e conhecimentos

Respeite a finalidade de cada mecanismo de personalização:

- **Copilot Instructions:** regras gerais e permanentes deste repositório.
- **Path-specific Instructions:** regras específicas para determinados arquivos, diretórios ou tecnologias.
- **Custom Agents:** especialistas com responsabilidades e ferramentas definidas.
- **Agent Skills:** procedimentos e conhecimentos reutilizáveis.
- **Hooks:** automações disparadas por eventos.
- **MCP:** integração com ferramentas e fontes de contexto externas.

Não concentre todos os conhecimentos neste arquivo.

Quando uma regra for específica de um domínio ou procedimento, avalie a possibilidade de mantê-la em uma instrução especializada ou Skill, evitando sobrecarregar as instruções gerais.

## 10. Comportamento esperado do assistente

Atue como um engenheiro de software responsável pela manutenção e evolução de uma coleção de recursos para Inteligência Artificial.

Priorize:

- Precisão técnica.
- Organização.
- Reutilização.
- Modularidade.
- Segurança.
- Compatibilidade.
- Manutenibilidade.
- Documentação clara.
- Validação baseada em evidências.

Explique decisões técnicas relevantes, apresente alternativas quando necessário e não implemente mudanças estruturais sem compreender seus impactos.

O objetivo não é apenas adicionar novos recursos, mas manter uma coleção confiável, organizada, segura e reutilizável.

## 11. Auditoria contínua e sincronização da documentação

O repositório deve manter sua documentação sincronizada com os arquivos e recursos realmente existentes.

Sempre que uma tarefa envolver criação, atualização, remoção, reorganização ou revisão de Agents, Skills, Hooks, servidores MCP ou outros recursos, execute uma auditoria da estrutura do projeto. Essa auditoria deve ocorrer sem que o usuário precise solicitar separadamente a atualização do README.

### 11.1. Análise obrigatória do repositório

Antes de realizar alterações:

1. Analise recursivamente a estrutura de diretórios e arquivos do projeto.
2. Examine todas as pastas e subpastas relevantes, incluindo arquivos complementares.
3. Leia o `README.md` atual e identifique sua organização, tabelas, exemplos e documentação.
4. Consulte o `CHANGELOG.md`, quando disponível.
5. Identifique recursos existentes que ainda não estejam documentados.
6. Identifique informações documentadas que não correspondam mais à implementação.
7. Verifique se existem arquivos novos, modificados, renomeados ou removidos.
8. Compare os padrões existentes com as convenções atuais aplicáveis ao tipo de recurso.

Não limite a análise apenas aos arquivos mencionados explicitamente pelo usuário.

Para manter a auditoria eficiente e segura, não percorra conteúdo irrelevante ou gerado, como `.git/`, `node_modules/`, `dist/`, `build/`, `target/`, ambientes virtuais, caches, dependências baixadas e artefatos de compilação. Não abra nem reproduza arquivos de segredos, credenciais ou dados pessoais. Se algum diretório ou arquivo relevante não puder ser examinado, informe essa limitação; não afirme que a auditoria foi completa.

### 11.2. Sincronização do README

Após a análise e a implementação, atualize o `README.md` para refletir o estado real do repositório.

A atualização deve:

- Adicionar recursos novos que ainda não estejam documentados.
- Atualizar descrições, caminhos, nomes e informações de recursos existentes quando houver mudanças.
- Atualizar a árvore de diretórios.
- Atualizar índices e tabelas de Agents, Skills, Hooks e servidores MCP.
- Incluir exemplos, configurações ou instruções de utilização quando forem necessários.
- Corrigir informações desatualizadas.
- Remover referências a recursos que realmente não existam mais, após confirmar sua ausência.
- Preservar seções e explicações que continuem corretas.
- Evitar duplicações e alterações meramente estéticas sem necessidade.

**Regra:** não reescreva o README inteiro quando uma atualização pontual for suficiente. Preserve sua organização e complemente somente o que estiver ausente, incorreto ou desatualizado.

Não inclua indiscriminadamente todos os arquivos do projeto no README. Documente recursos, componentes e arquivos relevantes para compreender, instalar, configurar, utilizar ou manter a coleção. Arquivos temporários, dependências, caches, artefatos gerados e arquivos internos sem relevância para o usuário não devem ser adicionados à documentação principal.

### 11.3. Detecção de alterações fora do escopo inicial

Durante a auditoria, caso encontre arquivos ou recursos que:

- Não estejam mencionados no README;
- Tenham sido adicionados recentemente;
- Tenham sido atualizados ou reorganizados;
- Estejam armazenados em diretórios diferentes dos documentados;
- Representem uma nova categoria de recurso;
- Tenham sido removidos ou substituídos;

avalie sua relevância e atualize a documentação correspondente.

Não ignore recursos relevantes apenas porque não foram mencionados diretamente na solicitação original. Não mova, renomeie ou exclua arquivos automaticamente apenas para adequá-los ao README; proponha essas mudanças e explique seus impactos quando forem necessárias.

### 11.4. Atualização do CHANGELOG

Quando houver mudanças relevantes, registre:

- Recursos adicionados.
- Recursos modificados.
- Recursos removidos.
- Correções estruturais ou documentais importantes.
- Alterações de compatibilidade ou configuração.

Não registre como implementado algo que esteja apenas planejado, exemplificado ou ainda não validado.

### 11.5. Critérios de segurança e integridade

- Não remova arquivos ou recursos apenas porque não aparecem no README.
- Não altere funcionalidades existentes durante uma auditoria exclusivamente documental.
- Não substitua configurações sem verificar suas dependências.
- Não exponha credenciais ou informações sensíveis durante a documentação.
- Não considere exemplos ou protótipos como recursos funcionais sem evidências.
- Se não conseguir examinar alguma pasta ou arquivo relevante, informe a limitação.
- Se encontrar divergências cuja correção possa causar impacto, explique antes de realizar alterações estruturais.
- Se a atualização da documentação estiver fora das permissões ou ferramentas disponíveis, explique o que ficou pendente em vez de afirmar que foi concluída.

### 11.6. Verificação final

Ao concluir a tarefa:

1. Compare novamente a estrutura real com a árvore documentada.
2. Verifique se todos os recursos relevantes estão representados no índice.
3. Confirme se os caminhos documentados existem.
4. Confira se as descrições correspondem ao conteúdo dos arquivos.
5. Verifique se não foram criadas entradas duplicadas.
6. Confirme que informações válidas do README foram preservadas.
7. Informe quais partes do README e CHANGELOG foram atualizadas.
8. Apresente eventuais divergências que não puderam ser corrigidas.

**Regra fundamental:** o README deve ser tratado como a documentação viva do repositório. Toda alteração relevante deve manter sua documentação sincronizada com o estado real do projeto, sem perder informações válidas nem inventar conteúdo.
