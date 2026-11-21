# Agent Skills Collection

Repositório público destinado ao armazenamento, versionamento e documentação de **Custom Agents**, **Skills de IA** e **Servidores MCP (Model Context Protocol)** para uso integrado em ambientes Git e assistentes de desenvolvimento local (como VS Code e GitHub Copilot).

---

## 📌 Visão Geral

Este projeto centraliza agentes customizados (`.agent.md`), instruções (`SKILL.md`), prompts estruturados, regras operacionais e conectores de contexto para IA. A estrutura foi desenhada para garantir consistência, reutilização e facilidade de manutenção à medida que o repositório se expande de um agente, skill e servidor inicial para uma coleção completa de capacidades para o assistente.

---

## 📁 Estrutura do Repositório

```text
agent-skills-collection/
├── agents/
│   └── java-specialist.agent.md          # Custom Agent especializado em Java
├── skills/
│   └── arquiteto-universal-prompts/
│       └── SKILL.md                      # Skill de engenharia de contexto e prompts
├── mcp-servers/                          # Servidores MCP customizados (quando aplicável)
├── testes/                               # Pasta de testes para servidor de arquivos MCP
├── README.md
└── CHANGELOG.md
```

---

## 🗺️ Índice de Recursos

### 🤖 Custom Agents
| Agente (`kebab-case`) | Domínio / Escopo | Caminho | Status |
| :--- | :--- | :--- | :--- |
| `Java-specialist` | Arquitetura, análise e refatoração modular em Java (leitura por padrão; edição apenas quando explicitamente solicitado, sem execução autônoma de terminal) | `agents/java-specialist.agent.md` | Ativo |

### 🧠 Agent Skills
| Skill (`kebab-case`) | Domínio | Caminho | Status |
| :--- | :--- | :--- | :--- |
| `arquiteto-universal-prompts` | Engenharia de Contexto e Prompts | `skills/arquiteto-universal-prompts/SKILL.md` | Ativa |

### 🔌 Servidores MCP (Model Context Protocol)
| Nome do Servidor | Tipo de Transporte | Descrição / Função | Requisitos |
| :--- | :--- | :--- | :--- |
| `teste-rapido-arquivos` | `stdio` (`npx`) | Acesso seguro a leitura/escrita de arquivos locais | Node.js / NPM e pasta de testes criada |
| `servidor-http-remoto` | `HTTP` (`url`) | Conexão a endpoints MCP remotos ou locais via HTTP | Serviço HTTP ativo e token de acesso |
| `google-drive` | `stdio` (`npx`) | Integração para leitura e busca no Google Drive | API Drive ativa no GCP e credenciais OAuth |
| `meu-servidor-local` | `stdio` (`python3`) | Servidor personalizado em Python para regras/tools customizadas | Python 3 e script `servidor.py` implementado |

---

## 🚀 Como Utilizar no VS Code (GitHub Copilot)

### 🤖 1. Configurando Custom Agents e Agent Skills

Tanto os **Custom Agents** (`.agent.md`) quanto as **Skills** (`SKILL.md`) funcionam por descoberta automática de pastas locais configuradas no VS Code.

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/BAT333/agent-skills-collection.git ~/Documentos/agent-skills-collection
   ```

2. **Garantir a existência das pastas `agents/` e `skills/`:**
   Confirme que existem os diretórios `~/Documentos/agent-skills-collection/agents` e `~/Documentos/agent-skills-collection/skills` (o nome da pasta no disco deve corresponder exatamente ao configurado no `settings.json`).

3. **Ativar no `settings.json` do VS Code (Nível de Usuário):**
   - Abra a Paleta de Comandos (`Ctrl + Shift + P`).
   - Selecione **`Preferences: Open User Settings (JSON)`**.
   - Adicione `chat.agentSkillsLocations` e `chat.agentFilesLocations` apontando para as pastas `skills` e `agents`:
     ```json
     {
       "chat.useAgentSkills": true,
       "chat.agentSkillsLocations": {
         "~/Documentos/agent-skills-collection/skills": true
       },
       "chat.agentFilesLocations": {
         "~/Documentos/agent-skills-collection/agents": true
       },
       "chat.viewSessions.orientation": "stacked"
     }
     ```
   > **Nota de sintaxe e escopo:** Use o prefixo `~/` para indicar a pasta home do usuário em sistemas Linux/macOS (caso o ambiente não expanda `~`, utilize `/home/rafael-alves/...`). Configurar no `settings.json` do usuário disponibiliza os agentes e skills em todos os workspaces. Convenções gerais específicas de um repositório devem ficar em `.github/copilot-instructions.md` dentro do próprio projeto.

4. **Carregar e Invocar no Copilot Chat:**
   - Após criar ou alterar arquivos/configurações, abra a Paleta de Comandos (`Ctrl + Shift + P`), execute **`Developer: Reload Window`** (se necessário) e valide em **`Chat: Open Customizations`**.
   - **Agente (`Java-specialist`):** no Copilot Chat, abra o seletor de agentes/modos e escolha **`Java-specialist`**. Opera em leitura por padrão e realiza edição apenas quando explicitamente solicitado.
   - **Skill (`arquiteto-universal-prompts`):** no Copilot Chat (modo **Agent**), digite `/` seguido da Skill (ex.: `/arquiteto-universal-prompts`).

---

### 🔌 2. Configurando Servidores MCP

Diferente das Skills e Agentes baseados em Markdown, os **Servidores MCP** exigem **declaração explícita de comandos e argumentos** no arquivo de configuração `mcp-config.json` (`~/.copilot/mcp-config.json`) ou `.vscode/mcp.json`.

#### Estrutura Recomendada do `mcp-config.json`

```json
{
	"mcpServers": {
		"teste-rapido-arquivos": {
			"command": "npx",
			"args": [
				"-y",
				"@modelcontextprotocol/server-filesystem",
				"/home/rafael-alves/Documentos/agent-skills-collection/testes"
			]
		},
		"servidor-http-remoto": {
			"url": "http://localhost:3000/mcp",
			"headers": {
				"Authorization": "Bearer SEU_TOKEN_AQUI"
			}
		},
		"google-drive": {
			"command": "npx",
			"args": [
				"-y",
				"@modelcontextprotocol/server-gdrive"
			],
			"env": {
				"GDRIVE_CREDENTIALS_PATH": "/home/rafael-alves/.config/gdrive/gcp-oauth.keys.json"
			}
		},
		"meu-servidor-local": {
			"command": "python3",
			"args": [
				"/home/rafael-alves/Documentos/agent-skills-collection/seu-servidor/servidor.py"
			]
		}
	}
}
```

> ⚠️ **Atenção em Servidores `stdio`:** Evite utilizar comandos como `print()` no Python ou `console.log()` no Node enviando texto livre para a saída padrão (`stdout`), pois isso corrompe o protocolo JSON-RPC do MCP. Escreva mensagens de depuração em `stderr` ou em arquivos de log.

---

## 🧪 Como Testar os Agentes e Servidores MCP

### 🤖 Testando o Custom Agent `Java-specialist` no VS Code

1. **Descoberta e carregamento:** abra **`Chat: Open Customizations`** (`Ctrl + Shift + P`) e confirme que **`Java-specialist`** aparece listado na seção de agentes do usuário sem erros de YAML.
2. **Leitura e diagnóstico sem escrita:** com um projeto Java aberto no VS Code, selecione **`Java-specialist`** no Copilot Chat e peça análise do `pom.xml` (ou `build.gradle`) e de `src/main/java`. Valide que ele não altera arquivos, não executa comandos no terminal sem autorização, separa **Fatos / Inferências / Recomendações** e sinaliza informações ausentes com `[PREENCHER_VALOR]`.
3. **Trava de segurança contra edição não solicitada:** peça uma sugestão de melhoria em uma classe sem autorizar escrita e confirme que nenhum arquivo em disco é modificado.
4. **Edição cirúrgica autorizada:** solicite explicitamente uma alteração pontual em um arquivo/método específico e valide que apenas o escopo autorizado foi alterado.

---

### 🔌 Testando os Servidores MCP

Para garantir a estabilidade do ambiente, o teste dos servidores MCP deve ser realizado em 3 etapas progressivas:

#### Etapa 1: Teste Isolado no Terminal (Handshake JSON-RPC)
Valide se o processo Python ou Node responde corretamente sem saídas inválidas:

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"teste-cli","version":"1.0.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"notifications/initialized","params":{}}\n{"jsonrpc":"2.0","id":3,"method":"tools/list","params":{}}\n' | python3 /home/rafael-alves/Documentos/agent-skills-collection/seu-servidor/servidor.py
```

#### Etapa 2: Teste Visual com MCP Inspector
Utilize a ferramenta oficial para inspecionar e chamar ferramentas (`tools`) interativamente no navegador:

```bash
# Para servidor de arquivos (Node)
npx @modelcontextprotocol/inspector npx -y @modelcontextprotocol/server-filesystem /home/rafael-alves/Documentos/agent-skills-collection/testes

# Para servidor local Python
npx @modelcontextprotocol/inspector python3 /home/rafael-alves/Documentos/agent-skills-collection/seu-servidor/servidor.py
```

Acesse a URL gerada (ex.: `http://127.0.0.1:6274`), navegue até a aba **Tools** e execute testes individuais.

#### Etapa 3: Execução no Copilot Chat (VS Code)
1. Certifique-se de que os servidores estão ativos no VS Code.
2. Abra o **Copilot Chat**, defina a caixa de seleção de modo para **Agent**.
3. No ícone de engrenagem/ferramentas (**Tools**), verifique se as ferramentas do servidor estão listadas e marcadas.
4. Defina a política de permissão em **Assisted permissions** (recomendado).
5. Envie um comando direto e explicito:
   > *"Use a ferramenta de arquivos MCP para ler `/home/rafael-alves/Documentos/agent-skills-collection/testes/Teste.txt`."*

---

## 🛠️ Como Adicionar Novos Agentes, Skills e Servidores

### Criando um Novo Agente

Crie um arquivo `<nome-do-agente>.agent.md` em `agents/` com frontmatter YAML (`name`, `description` e `tools`) e instruções operacionais em Markdown:

```text
agents/
└── <nome-do-agente>.agent.md
```

### Criando uma Nova Skill

Crie uma pasta em `skills/<nome-da-skill>/` contendo obrigatoriamente um arquivo `SKILL.md`:

```text
skills/
└── <nome-da-skill>/
    ├── SKILL.md                     # (Obrigatório) Instruções e regras principais da Skill
    ├── frameworks.md                # (Opcional) Estruturas técnicas e padrões
    ├── regras-anti-alucinacao.md    # (Opcional) Guardrails e critérios de validação
    └── exemplos-ouro.md             # (Opcional) Casos de uso de referência
```

### Criando um Novo Servidor MCP

1. Adicione a implementação do seu servidor em uma pasta dedicada (ex.: `mcp-servers/<nome-do-servidor>/`).
2. Adicione o novo bloco em `mcpServers` no arquivo `mcp-config.json`.
3. Atualize as tabelas do **Índice de Recursos** neste `README.md`.

---

## 📝 Versionamento e Histórico

- **Commits:** Padronize as mensagens por escopo (ex.: `feat(agents): adiciona custom agent java-specialist`, `feat(mcp): adiciona suporte a servidor local python` ou `docs(readme): adiciona instrucoes de teste do mcp inspector`).
- **Changelog:** Mantenha os registros de mudanças no arquivo `CHANGELOG.md` na raiz do repositório.