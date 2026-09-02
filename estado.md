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
- Nenhuma decisão humana local do PGA.

## Decisões fechadas nesta emenda
- U-PGA-13 provou que `enrior` estava incorretamente em `projetos_sem_skill`: o remoto declara `enrior-project@1.0.5` em `.github/skills/enrior-project/SKILL.md`, e o catálogo já registrava essa raiz como `aceito`.
- O catálogo global foi reconciliado no commit `ab2fabca8f06868a81029fccedb1f1e94e9fa259`: `enrior` saiu de `projetos_sem_skill`, o hash de `controle/caminhos-canonicos.yaml` foi atualizado e o validador passou a rejeitar a contradição conservadora `<projeto>-project/<projeto>-projeto` ↔ `projetos_sem_skill`.
- Após a correção, permanecem cinco projetos realmente sem skill raiz visível nas branches observadas: `laboratorio_hardware_2025`, `Laboratario-de-Hardware-2025-web`, `controle_matheus_eng_docentes`, `projeto_dependencia` e `SentinelDevLima`.
- O par de laboratórios possui candidato relacionado já registrado, `laboratorios-informatica-ifc-videira-projeto@0.1.1`; nenhuma vinculação foi inferida por similaridade.

## Pendências técnicas não humanas
- Nenhuma local no PGA após U-PGA-13.
- Externa ao PGA: cinco projetos continuam em `projetos_sem_skill`; a próxima ação de vínculo/bootstrap depende de decisão humana no contexto de cada projeto.
- Externa ao PGA: `governanca-operacional-de-ambientes@0.1.4` permanece `em_curso` por seus próprios portões de uso real/binding concreto.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento de U-PGA-13.

## Competências ativas nesta unidade
- `pga-project@0.4.0` — skill de projeto.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.

## Competências instaladas para unidades futuras
- Nenhuma alteração nesta unidade.

## Falhas de portão por tipo de entrada
- `estrutura`: namespace fechado desde U10; sem regressão em U13.
- `rastro`: enforcement prospectivo ativo desde U11; sem regressão em U13.
- `catalogo-global`: contradição `enrior`↔`projetos_sem_skill` corrigida; `CATALOGO_SKILLS=PASS` e `SYNC_GUARD=PASS` após atualização do hash canônico.
- `dados`: telemetria U04–U12 parseável e pareada; U10 preserva a não conformidade histórica de início tardio sem mascará-la como PASS.

## Divergências da última reconciliação
- corrigidas: `enrior` removido de `projetos_sem_skill` com gate prospectivo conservador; projeção de hash reconciliada.
- pendentes de autorização: vínculos/bootstrap dos cinco projetos externos sem skill raiz; nenhuma pendência local do PGA.

## Entradas aceitas
- 1–33.

## Próxima unidade
- Nenhuma unidade local PGA pendente; continuidade global depende de decisão humana de vínculo/bootstrap para os projetos externos sem skill raiz.
