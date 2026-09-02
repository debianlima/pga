# Estado — 2026-09-02 — contrato v3

## Decisões vigentes
- PGA 1.0.0 está homologado; `VERSION=1.0.0` e a tag `v1.0.0` permanecem imutáveis.
- PGA governa política, autoridade, prioridade estratégica, gates e evolução governada; não possui scheduler, worker, heartbeat, lease ou estado runtime vivo.
- Política e autoridade não sofrem mutação silenciosa nem autoexpansão.
- `GovernanceAttentionItem` representa somente decisão humana não resolvida; decisão resolvida sai da fila humana sem apagar `GovernanceTechnicalFollowUp` derivado.
- `Q3-NETWORK-SHARING-DEFAULT`: recursos são privados por padrão; adesão à rede é explícita e materializa exatamente os papéis efêmeros `network_control_agent` e `distributed_processing_agent`, sem sharing implícito.
- P0–P4 são bandas normativas; `P0_GOVERNED` é reservado ao humano, prioridade permanece ortogonal à autoridade e não concede bypass de lock/lease/fence/human block nem preempção automática.
- Após `PGD_AUXILIAR_RECONCILIATION=PASS`, o papel `auxiliar` pode participar de construção e conciliação incremental do PGA sem ampliar autoridade nem substituir decisão humana.

## Decisões superadas
- PGA 0.1.0 como estado de repouso standalone — superado pela release PGA 1.0.0.
- `estado_release: triad_ready` — superado pela evidência contratualmente validada `maturity: homologated` da release 1.0.0.

## Decisões humanas pendentes
- Nenhuma.

## Decisões fechadas nesta emenda
- U-PGA-10 reconciliou o namespace do manifesto com `git ls-files`, declarou `dados/telemetria-unidades.jsonl` e tornou essa igualdade verificável em `tests/verify_project.py`.
- U-PGA-10 consolidou este arquivo como snapshot atual, removendo blocos históricos acumulados e estados de execução já encerrados.
- U-PGA-10 alinhou `manifesto.yaml.estado_release` a `homologated`, conforme a evidência validada por `contratos/pga-1.0/release.schema.json`.

## Pendências técnicas não humanas
- Nenhuma local após os portões de U-PGA-10.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento de U-PGA-10.

## Competências ativas nesta unidade
- `pga-project@0.4.0` — skill de projeto.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.

## Competências instaladas para unidades futuras
- Nenhuma alteração nesta unidade.

## Falhas de portão por tipo de entrada
- `estrutura`: 1 divergência de namespace encontrada e corrigida; gate reforçado para impedir recorrência.
- `dados`: telemetria histórica U04–U09 parseável e pareada; U10 registra explicitamente que o evento de início foi tardio nesta execução.

## Divergências da última reconciliação
- corrigidas: `dados/telemetria-unidades.jsonl` declarado como entrada 33; `estado.md` convertido em snapshot; `estado_release` alinhado a `homologated`; `verify_project.py` passou a verificar namespace fechado e pares de telemetria.
- pendentes de autorização: nenhuma.

## Entradas aceitas
- 1–33.

## Próxima unidade
- Nenhuma unidade local pendente; nova unidade deve nascer de decisão/contrato posterior, sem reabrir a release `v1.0.0`.
