# Agent Skills Collection

Coleção pública de recursos personalizados para assistentes de IA em ambientes de desenvolvimento, incluindo Custom Agents, Agent Skills, instruções do repositório, Hooks e configuração MCP.

## Estado atual

| Tipo | Implementação atual | Caminho |
| :--- | :--- | :--- |
| Custom Agent | Java-specialist | [.github/agents/java-specialist.agent.md](.github/agents/java-specialist.agent.md) |
| Agent Skill | Arquitetura e padronização de prompts | [.github/skills/arquiteto-universal-prompts/](.github/skills/arquiteto-universal-prompts/) |
| Agent Skill | Criação, revisão e validação de Skills | [.github/skills/criador-de-skills/](.github/skills/criador-de-skills/) |
| Hook | `sessionStart` que prepara o workspace para staging | [.github/hooks/Commit.json](.github/hooks/Commit.json) |
| Servidor MCP | Servidor de arquivos local via `npx` | [.mcp.json](.mcp.json) |
| Instruções | Regras gerais do repositório | [AGENTS.md](AGENTS.md) |
| Instruções Copilot | Regras específicas para GitHub Copilot | [.github/copilot-instructions.md](.github/copilot-instructions.md) |

Os diretórios `agents/`, `skills/`, `hooks/` e `mcp-servers/` não existem na raiz. Os recursos ativos estão organizados conforme a estrutura de descoberta do VS Code/GitHub Copilot em `.github/`.

## Estrutura real

```text
agent-skills-collection/
├── .github/
│   ├── agents/
│   │   └── java-specialist.agent.md
│   ├── hooks/
│   │   └── Commit.json
│   ├── skills/
│   │   ├── AGENTS.md
│   │   ├── arquiteto-universal-prompts/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   └── criador-de-skills/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       ├── assets/
│   │       ├── references/
│   │       └── scripts/
│   └── copilot-instructions.md
├── .mcp.json
├── AGENTS.md
├── README.md
└── testes/
```

## Recursos

### Custom Agent

| Recurso | Finalidade | Comportamento |
| :--- | :--- | :--- |
| `Java-specialist` | Desenvolvimento, revisão arquitetural e refatoração em Java | Somente leitura por padrão; edição somente mediante solicitação explícita; não usa terminal automaticamente |

Arquivo: [.github/agents/java-specialist.agent.md](.github/agents/java-specialist.agent.md)

O arquivo contém a entrada `[PREENCHER_VALOR]` para versão do JDK, build tool e framework até esses dados serem definidos pelo projeto alvo.

### Agent Skills

| Recurso | Finalidade | Arquivos complementares |
| :--- | :--- | :--- |
| `arquiteto-universal-prompts` | Criar, auditar e padronizar prompts multi-modelo | `references/frameworks.md`, `references/regras-anti-alucinacao.md`, `references/exemplos-ouro.md` |
| `criador-de-skills` | Criar, revisar, organizar e testar Agent Skills | `references/`, `assets/` e `scripts/validate_skill.py` |

Arquivos principais:

- [.github/skills/arquiteto-universal-prompts/SKILL.md](.github/skills/arquiteto-universal-prompts/SKILL.md)
- [.github/skills/criador-de-skills/SKILL.md](.github/skills/criador-de-skills/SKILL.md)

### Hook

O arquivo [.github/hooks/Commit.json](.github/hooks/Commit.json) registra um hook `sessionStart` com o seguinte comando:

```text
git rev-parse --is-inside-work-tree >/dev/null 2>&1 && git add . || true
```

> **Aviso de segurança:** esse hook pode adicionar a todos os arquivos não ignorados à área de staging assim que uma sessão iniciar. Revise o comando e o repositório antes de ativá-lo. Para evitar staging automático, remova o hook, desabilite-o no cliente ou substitua o comando por uma operação sem efeitos no Git.

Não há scripts auxiliares de Hook implementados neste repositório.

### Servidor MCP

A configuração [.mcp.json](.mcp.json) define um único servidor:

| Servidor | Transporte | Configuração atual |
| :--- | :--- | :--- |
| `teste-rapido-arquivos` | `stdio` via `npx` | `@modelcontextprotocol/server-filesystem` com acesso à pasta `testes/` |

Exemplo já declarado no repositório:

```json
{
  "mcpServers": {
    "teste-rapido-arquivos": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "~/Documentos/agent-skills-collection/testes"
      ]
    }
  }
}
```

O argumento com `~` pode não ser expandido por todos os clientes. Se necessário, use o caminho absoluto da pasta `testes/` no ambiente.

## Uso no VS Code

### Descoberta dos recursos deste repositório

Abra este repositório no VS Code. Recursos em `.github/agents/`, `.github/skills/` e `.github/copilot-instructions.md` podem ser descobertos pelo GitHub Copilot conforme o suporte da versão instalada do VS Code.

Depois de alterar ou instalar os recursos:

1. Execute **Developer: Reload Window** pela Paleta de Comandos.
2. Abra **Chat: Open Customizations**.
3. Confirme que `Java-specialist` e as duas Skills aparecem sem erros.

No Copilot Chat:

- Selecione `Java-specialist` no seletor de agentes/modos.
- Solicite explicitamente antes de permitir edição de arquivos.
- Para as Skills, use o nome da Skill no cliente que suportar acionamento manual por nome ou deixe o Copilot descobrir o recurso pelo contexto da solicitação.

Se o projeto usar outra configuração de discovery, aponte as Skills e agentes para os diretórios reais:

- Skills: `.github/skills/`
- Custom Agent: `.github/agents/`
- Instruções: `.github/copilot-instructions.md`

Os nomes e locais acima são os definidos pelo estado atual deste repositório; não presuma suporte a uma convenção que não tenha sido verificada na versão do cliente.

### Servidor MCP

1. Confirme que Node.js e `npx` estão disponíveis.
2. Reabra o workspace após adicionar ou alterar `.mcp.json`.
3. Abra **Chat: Open Customizations** ou a configuração MCP suportada pela versão do VS Code.
4. Verifique se `teste-rapido-arquivos` está ativo e se as ferramentas de arquivos aparecem para o modo Agent.

Se o cliente não expandir `~` no argumento, substitua o valor por um caminho absoluto.

```bash
npx -y @modelcontextprotocol/server-filesystem \
  /home/rafael-alves/Documentos/agent-skills-collection/testes
```

Use permissões assistidas e conceda acesso apenas à pasta necessária.

## Validação

### Skills

Ambas as Skills foram validadas com o script auxiliar incluído no repositório:

```bash
python3 .github/skills/criador-de-skills/scripts/validate_skill.py \
  .github/skills/arquiteto-universal-prompts

python3 .github/skills/criador-de-skills/scripts/validate_skill.py \
  .github/skills/criador-de-skills
```

O script realiza verificações auxiliares de estrutura e frontmatter. Ele não substitui `skills-ref validate`, o parser do cliente nem testes funcionais no agente de destino.

Se estiver disponível no ambiente, use também:

```bash
skills-ref validate .github/skills/arquiteto-universal-prompts
skills-ref validate .github/skills/criador-de-skills
```

### Custom Agent

Validação manual recomendada:

1. Abra `Chat: Open Customizations` e confirme que `Java-specialist` aparece.
2. Solicite uma análise Java sem autorizar escrita.
3. Confirme que nenhum arquivo foi alterado e que o resultado separa fatos, inferências e recomendações.
4. Solicite explicitamente uma edição pontual e valide que apenas o trecho autorizado foi alterado.

### MCP

Validação funcional mínima:

1. Inicie o servidor MCP pela configuração do cliente.
2. Confirme que o servidor aparece como ativo e que suas ferramentas estão disponíveis.
3. Peça ao agente para listar ou ler um arquivo existente dentro da pasta `testes/`.
4. Não conceda acesso a diretórios fora da pasta configurada.

Não há servidores HTTP, Google Drive ou servidores Python implementados neste repositório no estado atual.

## Como adicionar recursos

### Novo Custom Agent

Crie `.github/agents/<nome-do-agente>.agent.md` com frontmatter YAML válido e instruções operacionais. Use `kebab-case` para o nome do arquivo e mantenha as ferramentas declaradas alinhadas às capacidades reais.

### Nova Agent Skill

Crie `.github/skills/<nome-da-skill>/SKILL.md`. Adicione `references/`, `assets/` ou `scripts/` somente quando justificarem uso.

Regras principais:

- frontmatter com `name` e `description`;
- nome em `kebab-case`, sem caracteres acentuados;
- descrição com propósito e gatilhos de acionamento;
- links relativos válidos;
- critérios de qualidade e recuperação de erros;
- validação estática e casos positivos, negativos e ambíguos.

Consulte [.github/skills/criador-de-skills/SKILL.md](.github/skills/criador-de-skills/SKILL.md) para o fluxo completo.

### Novo Hook

Crie `.github/hooks/<nome>.json` ou configure o hook no escopo de usuário suportado pelo cliente.

Antes de publicar, revise os efeitos do comando, trate erros e evite operações destrutivas ou alterações automáticas no repositório sem autorização.

### Novo servidor MCP

Adicione a configuração em `.mcp.json` ou em outro arquivo de MCP suportado pelo cliente. Documente transporte, comando, argumentos, dependências, variáveis de ambiente e limite de acesso.

Não adicione credenciais a arquivos versionados. Use variáveis de ambiente ou mecanismos seguros do cliente.

## Versionamento

Use Commits Convencionais em inglês para alterações relevantes:

- `feat(agents): add Java specialist`
- `feat(skills): add skill creator`
- `feat(hooks): add session start hook`
- `feat(mcp): add local filesystem server`
- `docs(readme): synchronize repository documentation`

Mudanças relevantes são registradas em [CHANGELOG.md](CHANGELOG.md).
