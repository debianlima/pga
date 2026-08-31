# U-PGA-01 — Integração MSGCD com PGH U20

## Estado
Handoff versionado para o futuro repositório canônico do **PGA — Protocolo de Autogovernança**. `PAG` permanece somente como alias histórico; **PGA** é a sigla canônica do Protocolo de Autogovernança. Enquanto não existir repositório standalone identificável, esta unidade permanece preservada no repositório do PGH e vinculada ao Issue #15.

## Missão PGA consolidada
PGA governa o contexto organizacional e a evolução governada de objetos.

Perguntas centrais:
- por quê esta organização faz isso?
- sob quais políticas, valores, prioridades e modelos?
- qual autoridade humana se aplica?
- o que deve evoluir e sob quais gates?

## GovernedObject PGA
O termo amplo `GovernedObject` fica reservado ao PGA e pode representar:
- protocolo;
- procedimento;
- processo;
- método;
- política;
- contrato;
- projeto-modelo;
- ativo;
- recurso;
- serviço;
- arquitetura;
- modelo de construção;
- regra organizacional.

O PGH usa `KnowledgeObject` para objetos cognitivos como Evidence/Claim/Norm/Artifact/Dataset/Experiment/EffectRecord. Essa separação evita colisão ontológica.

## Policy Snapshot → PGH
PGA deve publicar snapshots imutáveis de política/autoridade que o PGH referencia por `GovernanceContextBinding`:
- policy ref;
- versão;
- hash;
- autoridade;
- escopos aplicáveis;
- organização/tenant;
- estado.

O PGH congela esse contexto no `pgh.lock` por hash; não reimplementa a lógica normativa PGA.

## Autoevolução / gestão de procedimentos
A evolução governada não é exclusiva de protocolos. Qualquer `GovernedObject` elegível pode entrar no ciclo:

`evidência -> EvolutionProposal -> ImpactStudy -> plano aprovado -> protótipo/pesquisa/simulação/implementação candidata -> gates congelados -> validação -> homologação -> nova versão`

A evolução deve preservar identidade, versão anterior, motivação, evidências, autoridade, impacto, alternativas, rollback, histórico e proveniência.

Agentes podem automatizar pesquisa, comparação, simulação e execução de gates, mas não podem autoexpandir autoridade nem alterar política silenciosamente.

## Relação com PGD Outcome/Efficacy
PGD produz evidência sobre `executou?`, `funcionou?`, efeitos esperados/observados, regressões e integridade. PGH consolida essa evidência como conhecimento observado/homologado conforme seus gates. PGA pode então utilizar evidência consolidada para propor evolução de procedimento, política, protocolo, recurso ou outro GovernedObject.

Fluxo:

`PGA policy -> PGH knowledge/authorization -> PGD execution/outcome -> PGH evidence/knowledge -> PGA evolution proposal`

## Prioridade
PGA produz prioridade normativa/estratégica de projetos e objetos considerando valor institucional, urgência, risco, obrigação, impacto humano, custo e autoridade competente. PGD converte essa prioridade em escalonamento operacional sem ultrapassar capacidade e autorizações.

## Gates futuros PGA
- `POLICY_SNAPSHOT_IMMUTABLE`
- `AUTHORITY_PROVENANCE_COMPLETE`
- `GOVERNED_OBJECT_IDENTITY_PRESERVED`
- `NO_SILENT_POLICY_MUTATION`
- `NO_SELF_AUTHORITY_EXPANSION`
- `EVOLUTION_PLAN_APPROVED_BEFORE_RESULTS`
- `GATES_FROZEN_BEFORE_VALIDATION`
- `ROLLBACK_OR_DEPRECATION_DEFINED`
- `CULTURAL_CONTEXT_NE_EXECUTABLE_AUTHORITY`
- `STRATEGIC_PRIORITY_NE_RUNTIME_SCHEDULER`

## Migração
Quando o repositório standalone PGA existir, esta unidade deve ser migrada com linhagem explícita ao commit U20 original e ao Issue #15.

## U33 — política de agentes
A decisão humana de 30/08/2026 incorpora agentes à fronteira da tríade sem mover runtime para o PGA. O futuro `AgentGovernancePolicySnapshot` é superfície PGA e governa classes/papéis permitidos, limites de autonomia, fronteiras de aprovação humana, política de provider/modelo, restrições cross-project e prioridade estratégica.

PGA não possui `AgentInstance`, heartbeat, worker, profile runtime, fila, lease ou scheduler. Esses estados vivos pertencem ao PGD. O PGH referencia o snapshot PGA por `GovernanceContextBinding` e aplica autorização semântica; o PGD materializa a execução.

O painel único consome o snapshot PGA como plano normativo, mas não recebe autoridade independente para alterar política. `PAG` não cria um quarto protocolo: permanece alias histórico de PGA.
