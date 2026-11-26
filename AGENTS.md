# AGENTS.md — Agent Skills Collection

## 1. Contexto do projeto

Este repositório centraliza recursos para desenvolvimento, personalização e extensão de assistentes de Inteligência Artificial.

Os principais recursos mantidos são:

- Custom Agents.
- Agent Skills.
- Hooks.
- Servidores MCP.
- Instruções e documentação técnica.

O objetivo é manter uma coleção modular, organizada, segura, documentada e reutilizável em diferentes projetos e ambientes de desenvolvimento.

## 2. Organização do repositório

Respeite a estrutura existente:

- `agents/`: agentes personalizados.
- `skills/`: conhecimentos e procedimentos reutilizáveis.
- `hooks/`: automações e scripts associados.
- `mcp-servers/`: configurações e recursos de servidores MCP.
- `testes/`: experimentos e testes controlados.
- `README.md`: documentação e índice principal.
- `CHANGELOG.md`: histórico de alterações relevantes.

Antes de criar diretórios ou reorganizar arquivos, analise a estrutura atual e justifique a necessidade.

## 3. Diretrizes de desenvolvimento

- Analise os arquivos relacionados antes de implementar alterações.
- Respeite as convenções existentes.
- Priorize modularidade e reutilização.
- Evite duplicação de funcionalidades e instruções.
- Mantenha cada recurso com uma responsabilidade bem definida.
- Não altere arquivos fora do escopo solicitado.
- Não substitua configurações sem avaliar suas dependências.
- Não invente funcionalidades, ferramentas ou capacidades.
- Diferencie implementações reais de exemplos e experimentos.

## 4. Responsabilidade dos recursos

### Custom Agents

Representam especialistas com responsabilidades, ferramentas e limites de atuação definidos.

### Agent Skills

Representam conhecimentos e procedimentos reutilizáveis que podem ser utilizados pelos agentes conforme a necessidade.

### Hooks

Executam automações em eventos específicos do ciclo de vida dos agentes.

### MCP

Disponibiliza ferramentas e fontes de contexto externas por meio do Model Context Protocol.

Não misture as responsabilidades desses mecanismos.

## 5. Segurança

- Nunca exponha senhas, tokens, chaves privadas ou credenciais.
- Não versione arquivos contendo segredos.
- Utilize variáveis de ambiente para configurações sensíveis.
- Avalie permissões concedidas aos servidores MCP.
- Analise os comandos executados pelos Hooks.
- Evite operações destrutivas sem autorização explícita.
- Não execute comandos com efeitos relevantes sem compreender seus impactos.

## 6. Documentação

- Utilize Markdown.
- Mantenha nomes de arquivos e diretórios consistentes.
- Documente instalação, configuração, utilização e limitações.
- Atualize o README quando adicionar ou remover recursos.
- Atualize o CHANGELOG quando houver alterações relevantes.
- Evite documentações duplicadas ou contraditórias.

## 7. Processo de trabalho

Antes de implementar:

1. Entenda a solicitação.
2. Analise os arquivos existentes.
3. Identifique dependências e impactos.
4. Defina uma abordagem adequada.

Durante a implementação:

1. Preserve a organização existente.
2. Faça alterações relacionadas ao objetivo.
3. Reutilize recursos disponíveis.
4. Evite modificações não solicitadas.

Após implementar:

1. Verifique os arquivos modificados.
2. Valide a sintaxe e as configurações.
3. Execute testes apropriados, quando disponíveis.
4. Informe as alterações realizadas.
5. Apresente os resultados das validações.
6. Informe limitações ou pendências.

Nunca declare que um teste foi executado sem realmente executá-lo.

## 8. Versionamento

Utilize Conventional Commits, preferencialmente em inglês.

Exemplos:

- `feat(agents): add java specialist`
- `feat(skills): add skill creation workflow`
- `feat(hooks): add validation hook`
- `feat(mcp): add filesystem server configuration`
- `docs(readme): update resource documentation`
- `fix(skills): correct metadata`

## 9. Comportamento esperado

Atue como um engenheiro de software responsável pela evolução desta coleção.

Priorize:

- Precisão técnica.
- Segurança.
- Organização.
- Reutilização.
- Modularidade.
- Compatibilidade.
- Manutenibilidade.
- Documentação.
- Validação baseada em evidências.

Explique decisões técnicas relevantes e não implemente mudanças estruturais sem compreender seus impactos.