# Frameworks Universais de Prompting

## Regra de Montagem (Obrigatório vs. Condicional)
Todo prompt gerado deve conter os **5 blocos obrigatórios** e adicionar apenas os **blocos condicionais** exigidos pelo tipo de tarefa:

- **Tarefa geral, operação ou negócio:** Apenas os **5 blocos obrigatórios**.
- **Lógica, matemática, arquitetura, decisões complexas ou debugging:** 5 blocos obrigatórios + `<raciocinio_obrigatorio>`.
- **Estilo específico, classificação ou formatação rígida:** 5 blocos obrigatórios + `<exemplos>`.
- **Criação de uma nova Skill (`SKILL.md` + arquivos de apoio):** 5 blocos obrigatórios + `<especificacao_skill>`.

---

## Esqueleto Modular Completo

```xml
<!-- === BLOCOS OBRIGATÓRIOS === -->
<papel>
Especialidade exata, nível de senioridade/experiência e postura operacional (ex.: direto, analítico, didático).
</papel>

<contexto>
Cenário real, público-alvo ou consumidor do resultado, insumos disponíveis e objetivo final.
</contexto>

<tarefa>
Ação principal descrita com verbos objetivos (Analisar, Extrair, Comparar, Estruturar, Gerar).
</tarefa>

<regras_e_restricoes>
- O que NÃO fazer (proibições explícitas).
- Limites de tamanho, tom de voz e nível técnico.
- Critérios de incerteza (o que fazer quando faltarem dados).
</regras_e_restricoes>

<formato_saida>
Formato exato esperado (tabela Markdown, JSON, lista numerada, código) com campos ou colunas definidos.
</formato_saida>

<!-- === BLOCOS CONDICIONAIS (Incluir apenas quando aplicável) === -->
<raciocinio_obrigatorio>
Antes de escrever a resposta final, analise o problema internamente em etapas:
1. Levante as premissas e restrições críticas.
2. Identifique possíveis ambiguidades, exceções ou pontos de falha.
3. Valide a lógica ou os cálculos antes de concluir.
Apresente apenas o resultado final validado, a menos que o usuário peça o passo a passo explícito.
</raciocinio_obrigatorio>

<exemplos>
<exemplo_1>
<entrada>[EXEMPLO_DE_ENTRADA_1]</entrada>
<saida_esperada>[EXEMPLO_DE_SAIDA_ESPERADA_1]</saida_esperada>
</exemplo_1>

<exemplo_2>
<entrada>[EXEMPLO_DE_ENTRADA_2]</entrada>
<saida_esperada>[EXEMPLO_DE_SAIDA_ESPERADA_2]</saida_esperada>
</exemplo_2>
</exemplos>

<especificacao_skill>
- Nome curto em kebab-case (ex.: revisor-arquitetura-api) e descrição focada em gatilho + escopo.
- Responsabilidade única: o que essa Skill faz e o que fica fora dela.
- Arquivos de apoio necessários (.md) e quando cada um deve ser consultado.
- Fluxo de execução passo a passo e formato de saída obrigatório.
- Critérios de aceitação: como testar se a Skill funciona bem em 3 cenários reais.
</especificacao_skill>
