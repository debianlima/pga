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
- H01 como pendência de vínculo/bootstrap — resolvida pelo usuário em 2026-09-02.

## Decisões humanas pendentes
- Nenhuma local no PGA.

## Decisões fechadas nesta emenda
- H01-A: `controle_matheus_eng_docentes`, `projeto_dependencia` e `SentinelDevLima` recebem uma skill raiz própria cada um.
- H01-C: `laboratorio_hardware_2025` e `Laboratario-de-Hardware-2025-web` são classificados nesta governança como repositórios/arquivos de evidência científica; não recebem bootstrap/skill raiz por similaridade.
- `controle-matheus-eng-docentes-project@0.1.0` foi publicado em `controle_matheus_eng_docentes` no commit `5fc1f582ceb9244e363a3392ea3cc5f99132221a` sobre baseline `0dadb80be26c9fc7b982b547cec1cac8c6614095`.
- `projeto-dependencia-project@0.1.0` foi publicado em `projeto_dependencia` no commit `50f3ebbf203a39922ac44354cf47298f6a739cfc` sobre baseline `1153a8a14724f44e96594d89cc0fb315d016e7ff`.
- `sentinel-dev-lima-project@0.1.0` foi publicado em `SentinelDevLima` no commit `39634b8d692a6013361ee6db8b0cd99aedd90f50` sobre baseline `af6d517c2497b7709755f1d9c9786a38c6a6eeb5`.
- Catálogo reconciliado no commit `2959c45684788850a87bff662e65506652b46ab4`: as três skills foram registradas, consumidores atualizados, `projetos_sem_skill` ficou vazio e a classificação científica foi registrada em `evidencias/SCIENCE-LAB-HARDWARE-2025-CLASSIFICATION.yaml`.

## Pendências técnicas não humanas
- Nenhuma local no PGA após U-PGA-14.
- Externa ao PGA: os 135 artefatos baseline de `controle_matheus_eng_docentes`, 69 de `projeto_dependencia` e 15 de `SentinelDevLima` permanecem `preexistente`/`nao-classificado` até auditoria por tipo e portão; o bootstrap não os promoveu a `aceito`.
- Externa ao PGA: `governanca-operacional-de-ambientes@0.1.4` permanece `em_curso` por seus próprios portões de uso real/binding concreto.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento U-PGA-14.

## Competências ativas nesta unidade
- `pga-project@0.4.0` — raiz administrativa.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.
- `controle-matheus-eng-docentes-project@0.1.0`, `projeto-dependencia-project@0.1.0` e `sentinel-dev-lima-project@0.1.0` — raízes criadas/vinculadas por H01-A.

## Competências instaladas para unidades futuras
- As três novas skills raiz acima; competências de domínio adicionais só entram por tipo sem cobertura ou evidência de falha de portão.

## Falhas de portão por tipo de entrada
- `estrutura`: três bootstraps passaram `PGH_BOOTSTRAP=PASS`, namespace fechado e secret scan dos arquivos novos.
- `catalogo-global`: `CATALOGO_SKILLS=PASS accepted=83 pending=1 canonical=83`; `SYNC_GUARD=PASS`; `projetos_sem_skill=[]`.
- `evidencia-cientifica`: H01-C registrada com heads observados `ea9d54bec6806403ef2870bc7b99f9204210c814` e `43d60a3b257958122fd47ff2258acea6b4d58ae5`; nenhuma skill raiz criada para esses acervos.
- `rastro`: a unidade administrativa U14 iniciou telemetria antes de declarar bloco compartilhado no PGA; `SHARED_BLOCK_ORDER=FAIL_RECORDED`. Cada repositório bootstrap declarou seu próprio bloco antes do primeiro artefato e o liberou após os gates.

## Divergências da última reconciliação
- corrigidas: cinco itens removidos de `projetos_sem_skill`; três convertidos em projetos PGH com skill própria e dois classificados como evidência científica por decisão humana; catálogo/hash/consumidores reconciliados.
- pendentes de autorização: nenhuma local no PGA.

## Entradas aceitas
- 1–33.

## Próxima unidade
- PGA não possui unidade local pendente. Nos três projetos recém-estruturados, a próxima unidade é auditoria dos artefatos `preexistente`, sem promoção em massa.
