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
- U-PGA-11 preservou o plano congelado `pga-project@0.3.0` da U09 como procedência histórica; ele não é divergência frente à skill atual `0.4.0`.
- U-PGA-11 auditou o rastro pós-release: quatro commits U05/U06 têm trailers históricos incompletos (`Skill`/`Maquina`), mas seus artefatos foram posteriormente reexecutados e homologados por U07–U09; o histórico publicado não foi reescrito.
- U-PGA-11 adicionou verificação prospectiva de trailers e correspondência `Entrada`↔arquivos a partir do fechamento U10 (`871f0294...`).

## Pendências técnicas não humanas
- Nenhuma local após os portões de U-PGA-11.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento de U-PGA-11.

## Competências ativas nesta unidade
- `pga-project@0.4.0` — skill de projeto.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.

## Competências instaladas para unidades futuras
- Nenhuma alteração nesta unidade.

## Falhas de portão por tipo de entrada
- `estrutura`: 1 divergência de namespace encontrada e corrigida em U10; gate reforçado para impedir recorrência.
- `rastro`: 4 commits históricos U05/U06 com trailers incompletos identificados; artefatos re-auditados posteriormente; enforcement prospectivo instalado em U11 sem reescrever histórico.
- `dados`: telemetria U04–U10 parseável e pareada; U10 preserva a não conformidade histórica de início tardio sem mascará-la como PASS.

## Divergências da última reconciliação
- corrigidas: U11 preservou o plano congelado U09, classificou os trailers incompletos U05/U06 como lacuna histórica já re-auditada e adicionou gate prospectivo de adesão sem reescrever Git.
- pendentes de autorização: nenhuma.

## Entradas aceitas
- 1–33.

## Próxima unidade
- Nenhuma unidade local pendente; nova unidade deve nascer de decisão/contrato posterior, sem reabrir a release `v1.0.0`.
