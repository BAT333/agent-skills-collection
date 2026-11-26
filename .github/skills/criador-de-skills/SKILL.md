---
name: criador-de-skills
description: Cria, estrutura, revisa e testa Agent Skills reutilizáveis no formato SKILL.md. Use quando o usuário pedir uma nova Skill, melhoria de uma Skill existente, revisão de instruções, organização de referências, modelos e automações ou transformação de um processo recorrente em uma capacidade reutilizável para agentes.
---

# Criador de Skills

## Missão

Projetar Skills que façam um agente executar um tipo de trabalho com consistência, segurança e pouco desperdício de contexto. Entregue instruções operacionais, não apenas textos bem escritos: a Skill deve deixar claro **quando ativar, o que fazer, como decidir, como lidar com falhas e como verificar o resultado**.

## Princípios inegociáveis

1. **Comece pelo trabalho, não pelo arquivo.** Entenda o comportamento que precisa se tornar repetível antes de escolher estrutura ou escrever instruções.
2. **Prefira a menor solução suficiente.** Uma Skill curta e precisa é melhor que uma arquitetura elaborada sem benefício demonstrável.
3. **Use divulgação progressiva.** Mantenha no `SKILL.md` apenas o necessário para executar o fluxo. Carregue referências e modelos somente quando forem relevantes.
4. **Escreva para execução.** Use verbos de ação, condições observáveis, entradas, saídas, critérios de conclusão e caminhos de recuperação.
5. **Não invente capacidades.** Ferramentas, comandos, integrações, caminhos, APIs e permissões precisam existir ou ser explicitamente tratados como exemplos/hipóteses.
6. **Separe o estável do volátil.** Regras duradouras ficam na Skill; versões, endpoints, políticas e detalhes sujeitos a mudança exigem verificação em fonte atual.
7. **Teste o comportamento, não só a formatação.** Uma Skill válida no formato ainda pode ser ambígua, não disparar quando deveria ou disparar indevidamente.
8. **Seja transparente.** Diferencie o que foi criado, o que foi validado automaticamente, o que foi testado na prática e o que depende do ambiente do usuário.

## Quando ativar

Ative esta Skill quando o usuário solicitar, por exemplo:

- criar uma Skill ou um `SKILL.md`;
- melhorar, revisar, corrigir ou otimizar uma Skill existente;
- converter um procedimento recorrente em instruções reutilizáveis para um agente;
- organizar uma Skill com `references/`, `scripts/` ou `assets/`;
- avaliar qualidade, compatibilidade, acionamento ou testes de uma Skill.

Não a use para uma tarefa isolada que pode ser resolvida diretamente, para escrever um prompt pontual sem intenção de reutilização ou para criar uma integração/app quando o pedido exigir uma ferramenta executável e não apenas instruções. Nesses casos, explique a alternativa apropriada e não force a criação de uma Skill.

## Fluxo de trabalho

### 1. Descobrir o objetivo e o contexto

Extraia do pedido, sem perguntar novamente o que já foi informado:

- **Resultado:** qual trabalho o agente deve concluir?
- **Acionamento:** quais pedidos, termos, arquivos ou situações devem ativar a Skill?
- **Usuário e contexto:** para quem é o resultado e em qual ambiente/agente a Skill será usada?
- **Entradas:** quais dados, arquivos, parâmetros ou permissões são necessários?
- **Saídas:** o que deve ser entregue e em qual formato?
- **Limites:** o que está fora do escopo, o que não pode ser presumido e quais ações exigem autorização?
- **Qualidade:** como reconhecer uma execução correta?

Use o contexto da conversa e os arquivos disponíveis antes de perguntar. Faça no máximo três perguntas objetivas, somente quando uma resposta puder alterar materialmente a arquitetura, o comportamento ou a segurança. Agrupe perguntas realmente independentes. Não transforme preferências secundárias em bloqueios.

Quando faltarem detalhes não críticos, escolha padrões conservadores, registre as premissas relevantes e prossiga. Se o pedido for amplo, produza uma primeira versão funcional em vez de interromper o trabalho com um questionário.

### 2. Decidir se uma Skill é a solução certa

Crie uma Skill quando houver um processo reutilizável com pelo menos parte destes sinais:

- aparece em mais de uma situação ou tende a se repetir;
- exige sequência, critérios ou decisões que vale a pena preservar;
- tem gatilhos identificáveis;
- produz saídas relativamente previsíveis;
- ganha consistência ao ser executado por um agente.

Não crie uma Skill apenas porque a tarefa é longa. Para um pedido pontual, entregue diretamente o resultado ou um prompt/modelo simples. Para uma integração, aplicação ou ferramenta com comportamento próprio, esclareça que uma Skill documenta procedimentos e não cria, por si só, novas permissões ou ferramentas.

### 3. Delimitar o contrato da Skill

Antes de redigir, resuma internamente o contrato:

| Elemento | Pergunta de projeto |
|---|---|
| Gatilhos positivos | Que pedidos devem ativar a Skill? |
| Gatilhos negativos | Que pedidos parecidos não devem ativá-la? |
| Pré-condições | O que precisa estar disponível antes de executar? |
| Procedimento | Quais etapas e decisões produzem o resultado? |
| Ferramentas | Quais capacidades reais são necessárias? |
| Saída | Qual artefato ou resposta encerra a tarefa? |
| Verificação | Como comprovar que a saída atende aos critérios? |
| Recuperação | O que fazer se faltarem dados, ferramentas ou permissões? |
| Segurança | Quais ações são sensíveis, irreversíveis ou dependem de confirmação? |

Inclua no escopo apenas o necessário para entregar o resultado. Defina explicitamente o que a Skill não faz quando isso evitar acionamentos ou expectativas incorretas.

### 4. Pesquisar requisitos e capacidades atuais

Quando a Skill depender de um padrão, produto, API, biblioteca, política ou ferramenta que possa ter mudado:

1. Consulte documentação oficial ou a fonte primária mais confiável disponível.
2. Verifique a versão, data, compatibilidade e limitações relevantes.
3. Separe requisitos do formato Agent Skills de convenções específicas de um cliente.
4. Não copie comandos ou campos de exemplos sem confirmar que são aplicáveis.
5. Registre links e a data de verificação em uma referência somente quando isso ajudar futuras manutenções.

Se não houver acesso à fonte ou ao ambiente, declare a limitação e escreva instruções condicionais, em vez de afirmar compatibilidade não verificada.

### 5. Escolher a arquitetura mínima

Comece com `SKILL.md` único. Adicione recursos somente quando houver uma razão concreta:

| Recurso | Use quando | Evite quando |
|---|---|---|
| `references/` | Houver critérios extensos, conhecimento de domínio, especificações ou exemplos que só são necessários em alguns casos. | A informação for essencial em toda execução e couber claramente no `SKILL.md`. |
| `assets/` | O agente precisar copiar, preencher ou entregar modelos, esquemas, imagens ou arquivos estáticos. | O conteúdo puder ser descrito em poucas instruções sem perda. |
| `scripts/` | Uma operação determinística, repetitiva e verificável justificar automação. | O script apenas duplicar raciocínio, exigir dependências excessivas ou não puder ser executado no ambiente-alvo. |

Regras de organização:

- Mantenha os arquivos auxiliares em primeiro nível (`references/criterios-de-projeto.md`, `assets/modelo-skill.md`, `scripts/validate_skill.py`).
- Evite cadeias de referências: o `SKILL.md` deve apontar diretamente para o recurso necessário.
- Cada referência deve ter um assunto definido e ser carregada sob demanda.
- Não crie pastas vazias ou arquivos auxiliares só para parecer modular.
- Scripts devem documentar dependências, parâmetros, efeitos colaterais e exemplos de uso; tratar erros e nunca executar ações destrutivas sem autorização.

### 6. Escrever metadados que acionem corretamente

O frontmatter deve ser YAML válido. No mínimo, inclua `name` e `description`.

**`name`**

- Use `kebab-case` em ASCII para máxima portabilidade, por exemplo `analise-de-contratos`.
- Mantenha entre 1 e 64 caracteres; use apenas letras minúsculas, números e hífens.
- Não comece/termine com hífen nem use hífens consecutivos.
- Faça o nome corresponder exatamente ao diretório da Skill.

**`description`**

- Descreva o que a Skill faz e quando deve ser usada.
- Inclua termos reais que o usuário provavelmente usará ao pedir a tarefa.
- Prefira gatilhos específicos a frases vagas como “ajuda com produtividade”.
- Mantenha entre 1 e 1024 caracteres.
- Não coloque todo o procedimento na descrição; ela serve principalmente para descoberta e acionamento.

Adicione `compatibility` apenas quando houver requisito real de ambiente. Use `metadata` somente para dados úteis e portáveis. Não dependa de `allowed-tools`: o campo é experimental e o suporte varia entre clientes. Só declare ferramentas permitidas quando o ambiente-alvo documentar esse mecanismo e a lista estiver correta.

### 7. Escrever instruções executáveis

Organize o corpo do `SKILL.md` para permitir leitura rápida. Conforme o caso, inclua:

1. missão e resultado esperado;
2. quando ativar e quando não ativar;
3. pré-condições e dados de entrada;
4. fluxo numerado com decisões explícitas;
5. uso de ferramentas reais e seus limites;
6. critérios de qualidade e verificação;
7. tratamento de exceções e recuperação;
8. formato de entrega e exemplos curtos.

Ao escrever cada etapa:

- Diga **o que fazer**, **quando fazer** e **qual resultado observar**.
- Use condições `se/então/senão` quando houver ramificações.
- Diferencie obrigatório, recomendado e opcional.
- Defina o que fazer quando uma fonte, arquivo, ferramenta ou permissão estiver indisponível.
- Evite regras vagas (“seja cuidadoso”, “faça o melhor”) sem traduzir isso em critérios observáveis.
- Evite duplicar a mesma regra em vários pontos; referencie uma seção ou arquivo.
- Não dependa de contexto que não estará disponível em uma nova conversa.
- Preserve a autonomia do agente dentro do escopo, mas exija confirmação antes de ações externas, irreversíveis, financeiras, destrutivas ou que afetem terceiros quando aplicável.

### 8. Criar recursos auxiliares

Carregue `references/criterios-de-projeto.md` quando precisar aprofundar arquitetura, escopo, gatilhos ou escrita operacional.

Carregue `references/validacao-e-testes.md` ao revisar, testar, publicar ou diagnosticar uma Skill.

Use `assets/modelo-skill.md` como ponto de partida para uma nova Skill. Adapte ou remova as seções que não se aplicarem; não preserve placeholders no resultado final.

Use `assets/matriz-de-testes.md` para desenhar casos positivos, negativos, ambíguos e de falha. Não inclua casos irrelevantes apenas para preencher a matriz.

### 9. Validar formato e comportamento

Faça, no mínimo, as verificações aplicáveis:

- frontmatter abre e fecha corretamente e contém YAML válido;
- `name` e `description` atendem às regras e o nome corresponde à pasta;
- links e caminhos relativos citados existem;
- o `SKILL.md` tem escopo claro e pode ser seguido sem contexto oculto;
- o texto não inventa ferramentas, comandos, versões ou permissões;
- gatilhos positivos e negativos estão distinguíveis;
- etapas, decisões, erros e critérios de conclusão estão definidos;
- referências são realmente necessárias e não duplicam o corpo;
- exemplos são coerentes com as instruções;
- não há placeholders, contradições, instruções circulares ou regras impossíveis.

Quando disponível, execute o validador oficial `skills-ref validate <caminho-da-skill>`. O script `scripts/validate_skill.py` deste pacote é uma verificação auxiliar e não substitui o validador oficial.

Depois, simule pelo menos:

- um pedido típico que deve ativar a Skill;
- um pedido parecido que não deve ativá-la;
- um caso com informação ausente ou ambígua;
- um caso em que ferramenta, arquivo ou permissão não esteja disponível;
- um caso de limite, segurança ou falha, se aplicável.

Use a matriz em `assets/matriz-de-testes.md` como apoio. Corrija falhas de comportamento antes de considerar a Skill concluída.

### 10. Entregar e manter

Ao concluir, entregue:

- a pasta da Skill com todos os arquivos necessários;
- um resumo breve das decisões de arquitetura;
- as premissas ou limitações relevantes;
- os testes executados e seus resultados, distinguindo validação estática de teste funcional;
- instruções de instalação/uso compatíveis com o ambiente conhecido.

Se o ambiente permitir gerar arquivos, ofereça o diretório e um `.zip` pronto para distribuição. Não afirme que a Skill foi instalada, publicada ou testada em um agente real sem evidência.

Em revisões, preserve comportamentos que o usuário aprovou. Faça a menor alteração que resolva o problema, atualize referências afetadas e repita os testes pertinentes. Não reescreva tudo sem necessidade.

## Padrões de decisão

- **Informação crítica ausente:** pergunte apenas o necessário; se não bloquear, adote uma premissa conservadora e identifique-a.
- **Pedido muito amplo:** delimite uma primeira versão útil com escopo explícito; não tente cobrir todos os domínios possíveis.
- **Ferramenta não confirmada:** não invente o nome nem a sintaxe. Procure a documentação ou descreva a etapa como dependente de ferramenta disponível.
- **Padrão possivelmente desatualizado:** verifique fonte primária antes de fixar detalhes na Skill.
- **Skill extensa:** mova conhecimento condicional para referências, sem fragmentar instruções essenciais.
- **Skill simples:** mantenha apenas `SKILL.md`; modularidade não é um objetivo por si só.
- **Risco ou ação externa:** documente limites, permissões e ponto de confirmação.
- **Validação parcial:** entregue o que foi possível e nomeie exatamente o que ficou sem verificar.

## Critério de conclusão

Considere a Skill pronta quando um agente que não participou da conversa conseguir identificar quando usá-la, executar o fluxo com as informações disponíveis, reconhecer limites e falhas, produzir a saída esperada e verificar o próprio trabalho — sem depender de explicações improvisadas do autor.
