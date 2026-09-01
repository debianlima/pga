---
name: pga-project
versao: 0.4.0
description: Skill de projeto do PGA 1.0 para política, autoridade, prioridade, atenção humana e evolução governada; sem scheduler, lease ou runtime vivo.
tipo_competencia: projeto
origem:
  projeto_de_origem: protocolo-governanca-heterogenea
  commit_divergencia: a68ba9b460bd1d2050d57873fdc1c648732ece07
---
# PGA Project Skill

PGA governa política, autoridade, prioridade estratégica e evolução governada. Não possui estado runtime vivo e não autoexpande autoridade. Mudança normativa exige evidência, plano, gates congelados, validação e homologação.
## Governança de atenção humana

- `GovernanceAttentionItem` representa somente decisão ainda não resolvida que exige ação humana; contém projeto/tarefa/evidência/categoria/opções/impacto/reversibilidade/dependências/deadline real/autoridade e ações `more_info|approve|reject|modify`.
- Decisão fonte em `RESOLVED` ou `RESOLVED_PROVENANCE` sai da fila humana com `REMOVED_RESOLVED`; isso **não** apaga o trabalho técnico derivado.
- Todo trabalho derivado permanece como `GovernanceTechnicalFollowUp`, ligado ao `decision_id` e a evidências versionadas. Follow-up técnico aberto não reabre a decisão humana.
- Repositório fora do canônico ou divergência não reconciliável gera atenção/reconciliação; nunca é corrigido silenciosamente.

## Algoritmo de projeção

1. Fixar a fonte de decisões por repositório, commit, caminho e hash.
2. Para decisão não resolvida, produzir `GovernanceAttentionItem` com as ações humanas permitidas.
3. Para `RESOLVED*`, remover da fila humana e preservar decisão/autoridade/proveniência.
4. Produzir follow-up técnico auditável quando houver ação material decorrente da decisão.
5. Não criar grants, scheduler, worker, lease nem estado runtime no PGA; execução pertence às camadas próprias.

## Invariantes

- PGA governa política, autoridade, prioridade, gates e evolução governada; não executa scheduler/runtime.
- Decisão humana resolvida não volta à fila por existir dívida técnica.
- Follow-up técnico não amplia autoridade nem substitui decisão humana.
- Release `v1.0.0` é imutável; reconciliações pós-release não reescrevem a tag.
## Private-by-default e agentes de serviço de rede

- `Q3-NETWORK-SHARING-DEFAULT` mantém recursos, skills, projetos e chats privados por padrão; adesão à rede é sempre explícita.
- Após join explícito, a política PGA descreve **exatamente dois** papéis efêmeros: um `network_control_agent` (`network-control-only`) e um `distributed_processing_agent` (`distributed-processing-only`), ambos com `count=1`.
- Os dois papéis não compartilham recursos privados implicitamente; sharing adicional exige grant explícito por principal/grupo/tenant/público.
- PGA descreve a política, mas não cria scheduler, worker, lease, runtime, grant ou preempção. A execução é delegada ao owner de runtime/PGD e a federação de rede ao owner RHGD.
- A materialização de política não substitui a execução operacional G4 nem autoriza A07 a agir como runtime owner.

## Prioridade determinística sem transferência de autoridade

- **Aprendizado:** P0–P4 é política normativa do PGA, mas prioridade permanece ortogonal à autoridade L1–L5 e nunca cria permissão por si só.
- **Evidência/gate:** U-PGA-09-DETERMINISTIC-PRIORITY-POLICY, 2026-09-01; `FIVE_PRIORITY_BANDS=PASS`, `HUMAN_RESERVED_P0=PASS`, `AUTHORITY_PRIORITY_SEPARATION=PASS`, `NO_AUTOMATIC_PREEMPTION=PASS`, `STRICT_FIFO_PRESERVED=PASS`, `NO_PGA_RUNTIME=PASS`.
- **Evita:** tratar P0 como bypass de lock/lease/fence/human block, reordenar fila strict FIFO sem opt-in ou deslocar scheduler/runtime para o PGA.
- **Plataforma/pressupostos:** política versionada em YAML/JSON Schema; runtime continua sob PGD/runtime-owner e filas só aplicam prioridade quando seu contrato autoriza.
