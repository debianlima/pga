# U-PGA-07 — GovernanceAttentionItem e projeção Q1–Q7

Esta unidade materializa no PGA o contrato de **GovernanceAttentionItem** definido no bootstrap U-241. A fonte é `debianlima/pgh-distributed-session-control-plane@f5047f72914c6634982df30c8ce0f8747af5cfb3:config/3.0/governance-decisions.yaml`, fixada também por SHA-256.

## Regra de fila humana

Um item ainda pendente pode aparecer em `human_attention_queue` com os campos mínimos `decision_id`, projeto, tarefa, evidência, categoria, opções, impacto, reversibilidade, dependências, deadline real quando houver, autoridade necessária e as ações `more_info | approve | reject | modify`.

Para **Q1–Q7**, a fonte humana já contém `RESOLVED` ou `RESOLVED_PROVENANCE`. Por isso todos recebem `queue_disposition=REMOVED_RESOLVED` e a fila humana desta projeção fica vazia. Resolver a decisão não apaga o trabalho técnico que ela criou: cada decisão gera um **follow-up técnico** auditável, ligado de volta ao `decision_id` e às evidências.

## Follow-ups técnicos

Os sete follow-ups preservam exatamente a direção humana: Work34 key-auth, gate técnico do Desktop nativo, private-by-default com agentes de serviço de rede, hash H09 somente se o artefato canônico aparecer, mitigação T-069 sem outage, Project-Skills separadas de OpenTelemetry/SigNoz e baseline físico exclusivo ATU antes de thresholds.

Um follow-up técnico não volta para a fila humana só porque está aberto. Nova decisão humana só é necessária se aparecer conflito semântico, nova autoridade ou mudança do contrato aprovado.

## Fronteira de autoridade

Esta projeção é política/evidência. Ela **não cria scheduler**, worker, lease, fila runtime, grant ou estado vivo no PGA e não altera decisão humana. Execução continua pertencendo às camadas donas (PGD/POD/runtime); o PGA só governa política, autoridade, prioridade, gates e evolução governada.

A release `v1.0.0` permanece imutável; U-PGA-07 é reconciliação pós-release. O gate final exige `RECONCILIATION_CLOSURE=PASS` e `DEPENDENCY_REFERENCES=PASS` antes do fechamento.
