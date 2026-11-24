# Criador de Skills

Pacote de uma Agent Skill para projetar, escrever, revisar e testar outras Skills reutilizáveis.

## Conteúdo

- `SKILL.md`: fluxo principal e critérios operacionais.
- `references/criterios-de-projeto.md`: escopo, gatilhos, decomposição, arquitetura e segurança.
- `references/validacao-e-testes.md`: camadas de revisão, casos de teste e critérios de aprovação.
- `assets/modelo-skill.md`: ponto de partida para novas Skills.
- `assets/matriz-de-testes.md`: matriz reutilizável de testes comportamentais.
- `scripts/validate_skill.py`: validador auxiliar sem dependências externas.

## Uso

1. Disponibilize a pasta `criador-de-skills` no diretório de Skills suportado pelo seu agente.
2. Peça para criar, revisar ou testar uma Skill.
3. Use o modelo e a matriz somente quando forem úteis; a Skill orienta quando carregar cada recurso.
4. Para validação de formato mais rigorosa, execute `skills-ref validate ./criador-de-skills` caso o CLI oficial esteja instalado.

Validação auxiliar local:

```bash
python scripts/validate_skill.py ./criador-de-skills
```

O validador incluído detecta erros frequentes, mas não substitui um parser YAML completo, o validador oficial ou testes no agente de destino.
