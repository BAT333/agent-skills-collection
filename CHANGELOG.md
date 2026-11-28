# Changelog

Todas as mudanças relevantes deste repositório serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog e adota Semantic Versioning quando houver versões publicadas.

## [Unreleased]

### Added

- Adicionou a Agent Skill `gerador-readme-tecnico` para análise baseada em evidências e geração revisada de README técnico.
- Adicionou documentação individual da Skill em `.github/skills/gerador-readme-tecnico/README.md`.

### Documentação

- Sincronizou o README com a estrutura real dos recursos.
- Corrigiu os caminhos do Custom Agent, das Agent Skills e das configurações MCP e Hook.
- Removeu exemplos fictícios de servidores MCP e diretórios não existentes como se fossem recursos ativos.
- Registrou o aviso de segurança do hook `sessionStart`, que executa `git add .`.
