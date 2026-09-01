---
name: pga-project
versao: 0.2.0
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
