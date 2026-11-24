# Matriz de testes da Skill

Preencha os casos aplicáveis com entradas reais ou plausíveis. Execute-os no agente/cliente de destino quando possível.

| ID | Categoria | Entrada simulada | Deve ativar? | Comportamento esperado | Resultado | Observações |
|---|---|---|---|---|---|---|
| T01 | Positivo | [Pedido típico] | Sim | [Fluxo esperado] | Pendente | |
| T02 | Sinônimo | [Mesmo objetivo com outras palavras] | Sim | [Mesmo fluxo] | Pendente | |
| T03 | Negativo | [Pedido parecido, mas fora do escopo] | Não | [Não assumir a tarefa] | Pendente | |
| T04 | Ambíguo | [Pedido com decisão material ausente] | Sim/condicional | [Pergunta mínima ou premissa segura] | Pendente | |
| T05 | Falta de recurso | [Ferramenta/arquivo/permissão indisponível] | Sim | [Fallback honesto] | Pendente | |
| T06 | Segurança | [Ação sensível ou irreversível] | Sim/condicional | [Respeitar autorização e limites] | Pendente | |
| T07 | Contexto novo | [Pedido sem histórico da criação] | Sim | [Execução sem contexto oculto] | Pendente | |

## Critério de aprovação

- [ ] Todos os casos obrigatórios foram executados.
- [ ] Os casos positivos ativaram corretamente.
- [ ] Os casos negativos não acionaram indevidamente.
- [ ] Falhas e ausências foram tratadas sem inventar resultados.
- [ ] A saída satisfez os critérios definidos para a Skill.
- [ ] As limitações restantes foram registradas.
