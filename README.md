# Agent Skills Collection

Repositório público destinado ao armazenamento, versionamento e documentação de Skills de IA para uso integrado em ambientes Git e assistentes de desenvolvimento local (como VS Code e GitHub Copilot).

## 📌 Visão Geral

Este projeto centraliza instruções, prompts estruturados e regras operacionais para IA. A estrutura foi desenhada para garantir consistência, reutilização e facilidade de manutenção à medida que o repositório se expande de uma Skill inicial para uma coleção completa.

## 🗺️ Índice de Skills

| Skill (`kebab-case`) | Domínio | Caminho | Status |
| :--- | :--- | :--- | :--- |
| `arquiteto-universal-prompts` | Engenharia de Contexto e Prompts | `skills/arquiteto-universal-prompts/SKILL.md` | Ativa |

## 🚀 Como Utilizar no VS Code (GitHub Copilot)

Para que o GitHub Copilot reconheça e carregue estas Skills automaticamente em qualquer projeto, siga os passos abaixo:

### 1. Clonar o Repositório

Abra o terminal e baixe este repositório para uma pasta fixa no seu computador (por exemplo, dentro de `Documentos`):

```bash
git clone https://github.com/BAT333/agent-skills-collection.git ~/Documentos/agent-skills-collection
```

### 2. Ativar as Skills no `settings.json` do VS Code

O VS Code precisa saber onde encontrar a pasta `skills/`. Para configurar:

1. No VS Code, abra a Paleta de Comandos (`Ctrl + Shift + P` no Windows/Linux ou `Cmd + Shift + P` no Mac).
2. Digite e selecione **`Preferences: Open User Settings (JSON)`** (para ativar em todos os seus projetos) ou **`Preferences: Open Workspace Settings (JSON)`** (para ativar apenas no projeto atual).
3. Adicione as seguintes configurações no seu arquivo JSON:

```json
{
  "chat.useAgentSkills": true,
  "chat.agentSkillsLocations": {
    "~/Documentos/agent-skills-collection/skills": true
  }
}
```

> **Aviso de sintaxe:** O esquema do VS Code rejeita caminhos absolutos completos (como `/home/usuario/...`). Use sempre o prefixo `~/` (pasta home do usuário) ou um caminho relativo ao workspace.

### 3. Usar e Atualizar no Dia a Dia

* **Como invocar:** Abra o Copilot Chat, mude para o modo **Agent** e digite `/` seguido do nome da Skill (ex.: `/arquiteto-universal-prompts`), ou faça um pedido direto relacionado às atribuições da Skill.
* **Atualização em tempo real:** Qualquer modificação feita nos arquivos dentro da pasta `skills/` é lida automaticamente. Basta abrir um Novo Chat (`+`) para recarregar o índice.
* **Limpeza de duplicatas:** Se você copiou Skills anteriormente para pastas como `~/.copilot/skills/`, remova-as para evitar duplicação no menu `/`.

### Uso em Outros Repositórios Git

* Você pode copiar a pasta de uma Skill específica (`skills/<nome-da-skill>/`) para o repositório do seu projeto caso prefira versionar a Skill junto ao código-fonte.

## 🛠️ Como Adicionar uma Nova Skill

Toda nova contribuição deve seguir a estrutura e as convenções abaixo para manter a compatibilidade automatizada:

### Estrutura de Pastas

Qualquer nova pasta criada em `skills/` contendo um arquivo `SKILL.md` será detectada pelo assistente:

```text
skills/
└── <nome-da-skill>/
    ├── SKILL.md                     # (Obrigatório) Instruções e regras principais da Skill
    ├── frameworks.md                # (Opcional) Estruturas técnicas e padrões
    ├── regras-anti-alucinacao.md    # (Opcional) Guardrails e critérios de validação
    └── exemplos-ouro.md             # (Opcional) Casos de uso de referência
```

### Regras de Nomenclatura e Formatação

1. **Nomenclatura:** Utilize apenas `kebab-case` para pastas e arquivos (ex.: `arquiteto-universal-prompts`).
2. **Arquivo Principal:** O ponto de entrada de cada Skill deve se chamar exatamente `SKILL.md`.
3. **Portabilidade:** Utilize apenas caminhos relativos para referenciar outros arquivos dentro da pasta da Skill.
4. **Atualização do Índice:** Registre toda nova Skill na tabela do **Índice de Skills** neste `README.md`.

## 📝 Versionamento e Histórico

* **Commits:** Padronize as mensagens por escopo (ex.: `feat(arquiteto-universal-prompts): adiciona regras anti-alucinacao` ou `docs(readme): atualiza instrucoes do vscode`).
* **Changelog:** Mantenha os registros de mudanças no arquivo `CHANGELOG.md` na raiz do repositório.