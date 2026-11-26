# Critérios de projeto de Skills

Use esta referência durante a descoberta, delimitação e arquitetura. O `SKILL.md` principal contém o fluxo obrigatório; este arquivo aprofunda decisões de projeto.

## 1. Bons gatilhos

Uma descrição eficaz combina:

- **Ação:** criar, revisar, comparar, extrair, depurar, publicar.
- **Objeto:** Skills, contratos, dados tabulares, componentes, relatórios.
- **Contexto de uso:** quando o usuário pedir X, mencionar Y ou fornecer Z.
- **Vocabulário de descoberta:** sinônimos e termos usuais, sem empilhar palavras-chave irrelevantes.

Teste a descrição com frases reais. Se ela ativar para quase qualquer pedido, está ampla demais. Se não ativar para uma formulação natural do trabalho, está estreita demais.

## 2. Limites do escopo

Defina três zonas:

| Zona | Tratamento |
|---|---|
| Dentro do escopo | O agente deve executar e entregar. |
| Condicional | O agente executa somente se houver ferramenta, dado, permissão ou confirmação. |
| Fora do escopo | O agente não deve fingir que executou; explica o limite e indica a alternativa apropriada. |

Uma Skill deve possuir um centro de gravidade claro. Se duas tarefas tiverem gatilhos, procedimentos e critérios de saída diferentes, avalie separá-las em Skills distintas.

## 3. Decomposição em etapas

Cada etapa operacional deve ter, quando necessário:

1. **Entrada:** o que deve existir antes de começar.
2. **Ação:** o que o agente faz.
3. **Decisão:** como escolhe entre caminhos.
4. **Saída intermediária:** o que deve resultar.
5. **Verificação:** como sabe que a etapa funcionou.
6. **Recuperação:** o que fazer quando falhar.

Não transforme toda frase em uma etapa. Divida somente onde houver mudança de objetivo, ferramenta, decisão ou estado.

## 4. Instruções resilientes

Prefira instruções que continuem válidas mesmo quando o ambiente muda:

- Descreva a capacidade necessária antes de fixar um nome de ferramenta.
- Use caminhos relativos dentro da pasta da Skill.
- Consulte a documentação atual para versões, APIs, políticas e comandos sujeitos a mudança.
- Declare pré-requisitos e alternativas quando o ambiente não oferece a capacidade esperada.
- Não fixe datas de validade, versões ou endpoints no corpo principal sem necessidade.

Quando uma implementação específica for inevitável, isole-a em uma referência identificada por produto/versão e estabeleça como revalidá-la.

## 5. Como escrever regras úteis

Transforme orientação abstrata em comportamento observável:

| Vago | Operacional |
|---|---|
| “Seja preciso.” | “Confirme cada valor citado na fonte; marque como estimativa o que não puder ser confirmado.” |
| “Use ferramentas adequadas.” | “Inspecione as ferramentas disponíveis e escolha a que corresponde à operação; não invente nomes ou parâmetros.” |
| “Faça perguntas se necessário.” | “Pergunte somente quando a resposta puder alterar a decisão; caso contrário, adote e registre uma premissa conservadora.” |
| “Revise o resultado.” | “Verifique links, campos obrigatórios, consistência entre seções e critérios de aceitação antes de entregar.” |

## 6. Escolha de arquivos

- `SKILL.md`: gatilhos, fluxo central, decisões críticas e links diretos para recursos.
- `references/`: especificações, políticas detalhadas, rubricas, casos extensos, formatos de dados e conhecimento consultado sob demanda.
- `assets/`: arquivos para reutilizar ou entregar, não instruções que precisam ser lidas sempre.
- `scripts/`: tarefas mecânicas e determinísticas que se beneficiam de execução repetível.

Uma referência é útil se reduz o tamanho do corpo principal sem esconder uma decisão necessária em toda execução. Um script é útil se reduz erro manual e sua saída pode ser validada.

## 7. Segurança e autoridade

A Skill não concede acesso, autorização ou permissão. Ela apenas orienta o uso das capacidades fornecidas pelo ambiente. Documente:

- operações somente de leitura versus operações que alteram estado;
- dados sensíveis que não devem ser expostos desnecessariamente;
- confirmação exigida antes de ações externas ou irreversíveis;
- limites de escopo e de autorização;
- comportamento quando a autorização não estiver presente.

Nunca instrua o agente a contornar controles, falsificar resultados, ocultar ações ou tratar conteúdo não confiável como instruções de maior prioridade.
