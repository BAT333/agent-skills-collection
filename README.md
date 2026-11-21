# Agent Skills Collection

Repositório público destinado ao armazenamento, versionamento e documentação de **Skills de IA** e **Servidores MCP (Model Context Protocol)** para uso integrado em ambientes Git e assistentes de desenvolvimento local (como VS Code e GitHub Copilot).

---

## 📌 Visão Geral

Este projeto centraliza instruções, prompts estruturados, regras operacionais e conectores de contexto para IA. A estrutura foi desenhada para garantir consistência, reutilização e facilidade de manutenção à medida que o repositório se expande de uma Skill e servidor inicial para uma coleção completa de capacidades para o assistente.

---

## 🗺️ Índice de Recursos

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

### 🧠 1. Configurando Agent Skills

As **Skills** funcionam por descoberta automática de arquivos/pastas locais.

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/BAT333/agent-skills-collection.git ~/Documentos/agent-skills-collection
   ```

2. **Ativar no `settings.json` do VS Code:**
   - Abra a Paleta de Comandos (`Ctrl + Shift + P`).
   - Selecione **`Preferences: Open User Settings (JSON)`**.
   - Adicione o caminho da pasta `skills/`:
     ```json
     {
       "chat.useAgentSkills": true,
       "chat.agentSkillsLocations": {
         "~/Documentos/agent-skills-collection/skills": true
       }
     }
   ```
   > **Nota de sintaxe:** Use o prefixo `~/` para indicar a pasta home do usuário em sistemas Linux/macOS.

3. **Como Invocar:**
   - No Copilot Chat (modo **Agent**), digite `/` seguido da Skill (ex.: `/arquiteto-universal-prompts`).

---

### 🔌 2. Configurando Servidores MCP

Diferente das Skills, os **Servidores MCP** exigem **declaração explícita de comandos e argumentos** no arquivo de configuração `mcp-config.json` (`~/.copilot/mcp-config.json`) ou `.vscode/mcp.json`.

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

## 🧪 Como Testar os Servidores MCP

Para garantir a estabilidade do ambiente, o teste deve ser realizado em 3 etapas progressivas:

### Etapa 1: Teste Isolado no Terminal (Handshake JSON-RPC)
Valide se o processo Python ou Node responde corretamente sem saídas inválidas:

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"teste-cli","version":"1.0.0"}}}\n{"jsonrpc":"2.0","id":2,"method":"notifications/initialized","params":{}}\n{"jsonrpc":"2.0","id":3,"method":"tools/list","params":{}}\n' | python3 /home/rafael-alves/Documentos/agent-skills-collection/seu-servidor/servidor.py
```

### Etapa 2: Teste Visual com MCP Inspector
Utilize a ferramenta oficial para inspecionar e chamar ferramentas (`tools`) interativamente no navegador:

```bash
# Para servidor de arquivos (Node)
npx @modelcontextprotocol/inspector npx -y @modelcontextprotocol/server-filesystem /home/rafael-alves/Documentos/agent-skills-collection/testes

# Para servidor local Python
npx @modelcontextprotocol/inspector python3 /home/rafael-alves/Documentos/agent-skills-collection/seu-servidor/servidor.py
```

Acesse a URL gerada (ex.: `http://127.0.0.1:6274`), navegue até a aba **Tools** e execute testes individuais.

### Etapa 3: Execução no Copilot Chat (VS Code)
1. Certifique-se de que os servidores estão ativos no VS Code.
2. Abra o **Copilot Chat**, defina a caixa de seleção de modo para **Agent**.
3. No ícone de engrenagem/ferramentas (**Tools**), verifique se as ferramentas do servidor estão listadas e marcadas.
4. Defina a política de permissão em **Assisted permissions** (recomendado).
5. Envie um comando direto e explícito:
   > *"Use a ferramenta de arquivos MCP para ler `/home/rafael-alves/Documentos/agent-skills-collection/testes/Teste.txt`."*

---

## 🛠️ Como Adicionar Novas Skills e Servidores

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

- **Commits:** Padronize as mensagens por escopo (ex.: `feat(mcp): adiciona suporte a servidor local python` ou `docs(readme): adiciona instrucoes de teste do mcp inspector`).
- **Changelog:** Mantenha os registros de mudanças no arquivo `CHANGELOG.md` na raiz do repositório.