# Validação e testes de Skills

Use esta referência antes de entregar, distribuir ou alterar uma Skill existente.

## 1. Camadas de validação

### A. Estrutural

Verifique diretório, `SKILL.md`, YAML frontmatter, campos obrigatórios, limites de tamanho, nome e referências locais. Use `skills-ref validate <diretório>` quando disponível. O validador auxiliar incluído neste pacote ajuda a detectar erros comuns, mas não é uma implementação completa da especificação.

### B. Editorial e operacional

Leia o `SKILL.md` como se fosse um agente sem acesso à conversa original:

- O gatilho está claro?
- A primeira ação está definida?
- As entradas e saídas são explícitas?
- As decisões têm condições observáveis?
- As ferramentas e os caminhos realmente existem?
- Há uma estratégia para dados, permissões e ferramentas ausentes?
- Há critério de conclusão verificável?
- As referências são carregadas somente quando necessárias?

### C. Comportamental

Execute simulações com frases de usuário independentes do texto da Skill. Não basta perguntar “a Skill parece boa?”; observe se o comportamento esperado acontece.

### D. Compatibilidade

Quando a Skill for destinada a um cliente específico, confirme como esse cliente descobre Skills, interpreta frontmatter, expõe recursos e permite executar scripts. Não presuma que todos os clientes suportam extensões opcionais da mesma maneira.

## 2. Matriz mínima de testes

| Caso | Entrada de teste | Resultado esperado |
|---|---|---|
| Positivo | Pedido típico, direto e claro. | A Skill é selecionada e executa o fluxo. |
| Sinônimo | Mesmo trabalho descrito com vocabulário diferente. | A Skill ainda é selecionada. |
| Negativo | Pedido relacionado, mas fora do escopo. | A Skill não assume a tarefa indevidamente. |
| Ambíguo | Pedido com um detalhe que pode alterar a solução. | O agente faz a pergunta mínima ou declara uma premissa segura. |
| Falta de recurso | Arquivo, ferramenta ou permissão indisponível. | O agente não inventa sucesso; informa a limitação e oferece caminho válido. |
| Limite/risco | Ação destrutiva, externa, sensível ou não autorizada. | O agente respeita o limite e solicita autorização quando necessário. |
| Contexto novo | A Skill é usada sem a conversa em que foi criada. | O procedimento continua compreensível e executável. |

Adapte a matriz: retire cenários irrelevantes e inclua riscos específicos do domínio.

## 3. Critérios de aceitação

Uma Skill passa quando:

- os casos positivos ativam a Skill;
- os casos negativos não produzem falsos acionamentos importantes;
- ambiguidades são resolvidas sem perguntas desnecessárias;
- falhas levam a recuperação ou comunicação clara;
- a saída atende aos critérios definidos no contrato;
- não há dependência de contexto ausente;
- nenhuma ferramenta, execução ou validação é alegada sem evidência.

## 4. Relato de validação

Use estados precisos:

- **Validado estruturalmente:** frontmatter, nomes, arquivos e referências foram conferidos.
- **Validado pelo `skills-ref`:** o comando oficial terminou sem erros.
- **Testado por simulação:** cenários de acionamento e fluxo foram executados em avaliação controlada.
- **Testado no cliente-alvo:** a Skill foi carregada e executada no produto/ambiente declarado.
- **Não verificado:** algo depende de acesso ou ambiente indisponível.

Não misture esses estados. Um arquivo pode ser estruturalmente válido sem ter sido testado em um agente real.

## 5. Regressão em revisões

Ao alterar uma Skill existente:

1. Identifique o comportamento aprovado que deve permanecer.
2. Mude apenas o necessário para corrigir a falha ou atender ao novo requisito.
3. Atualize referências, modelos e testes que dependam da alteração.
4. Reexecute os casos afetados e os principais gatilhos negativos.
5. Registre mudanças incompatíveis ou novas pré-condições.
