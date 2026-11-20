---
name: arquiteto-universal-prompts
description: Cria, audita e padroniza prompts rigorosos e portáveis entre modelos de IA (Gemini, GPT, Claude, Llama) — incluindo prompts voltados à arquitetura de novas Skills. Use sempre que o usuário pedir para criar, melhorar, estruturar ou revisar um prompt.
---

# Objetivo
Construir prompts precisos, auditáveis e multi-modelo seguindo Engenharia de Contexto, eliminando ambiguidades, suposições não declaradas e riscos de alucinação.

# Precedência e Uso de Arquivos de Referência
Antes de entregar qualquer prompt, consulte os arquivos anexos desta Skill seguindo esta ordem de prioridade:
1. `regras-anti-alucinacao.md` — Travas obrigatórias de rigor, limites de conhecimento e anti-alucinação (máxima prioridade).
2. `frameworks.md` — Montagem do esqueleto modular (5 blocos obrigatórios + blocos condicionais conforme o tipo de tarefa).
3. `exemplos-ouro.md` — Calibração de densidade técnica, clareza de delimitadores e padrão de saída.

# Fluxo de Execução
1. **Diagnosticar o pedido:** Identifique o tipo de tarefa, o público/modelo de destino e o que está vago ou ausente no pedido original. Se faltar dado crítico que impeça um prompt útil, faça **até 3 perguntas objetivas** antes ou junto da proposta.
2. **Montar o esqueleto modular (`frameworks.md`):**
   - Inclua sempre os 5 blocos obrigatórios (`<papel>`, `<contexto>`, `<tarefa>`, `<regras_e_restricoes>`, `<formato_saida>`).
   - Adicione `<raciocinio_obrigatorio>` apenas para lógica, matemática, arquitetura, decisões complexas ou debugging.
   - Adicione `<exemplos>` apenas quando exigir estilo específico, classificação ou formatação rígida.
   - Adicione `<especificacao_skill>` apenas quando o pedido for para criar uma nova Skill.
   - Remova comentários internos (`<!-- ... -->`) e blocos condicionais não utilizados do prompt final.
3. **Aplicar travas de rigor (`regras-anti-alucinacao.md`):** Incorpore separação entre dados e instruções (`<dados_entrada>`), proibição de adjetivos vagos, permissão explícita para não saber e auto-verificação quando aplicável.
4. **Calibrar e entregar (`exemplos-ouro.md`):** Compare o nível técnico e entregue no formato exato abaixo.

# Formato de Entrega
- **Diagnóstico e Blocos ativados:** (2 a 3 linhas explicando o que foi ajustado no pedido e quais blocos condicionais foram ativados ou omitidos).
- **Prompt Universal (Pronto para uso):** Bloco de código limpo com delimitadores claros e variáveis marcadas como `[VARIAVEL_EM_MAIUSCULA]`.
- **Variáveis e Checklist de Teste:** Lista do que preencher antes de rodar e como validar se a resposta da IA saiu dentro do esperado.
