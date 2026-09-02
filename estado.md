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
- H01 como pendência de vínculo/bootstrap — resolvida em 2026-09-02.
- H02, H03, H04 e H05 como pendências de consolidação — resolvidas em 2026-09-02 por aprovação humana da opção A em cada decisão.

## Decisões humanas pendentes
- Nenhuma local no PGA.
- Nenhuma das consolidações H01–H05 permanece pendente.

## Decisões fechadas nesta emenda
- H02-A: em `SentinelDevLima`, `src/agents/codebase-indexer.ts` foi removido e `src/indexer/codebase-indexer.ts` permaneceu canônico; skill atual `sentinel-dev-lima-project@0.1.2`; gate final publicado em `8418f8f5403a86b93b3b0d38be38fdb145fd0ef5`.
- H03-A: em `projeto_dependencia`, `store/should-deploy.js` foi removido e `scripts/should-deploy.js` permaneceu canônico; skill atual `projeto-dependencia-project@0.1.2`; gate final publicado em `b89872fb9e2360296fb6596834135f35db424baa`.
- H04-A: em `controle_matheus_eng_docentes`, `docs/README_SUBSTITUIR_ARQUIVOS_COMPLETOS.md` foi removido e `docs/DEPLOY_MANUAL_SUAP_SEM_PONTO_COMPLETO.md` permaneceu canônico.
- H05-A: em `controle_matheus_eng_docentes`, `sql/insercao_funcionando.sql` foi removido e `sql/999_dados_demonstracao.sql` permaneceu canônico; `sql/ORDEM_REAL_MIGRATIONS_P3.md` foi reconciliado; skill atual `controle-matheus-eng-docentes-project@0.1.2`; gate final publicado em `d8985f00cef1be7b1dc4709df410dc25e7cd9fea`.
- Catálogo global reconciliado em `92ea5c638034e5e57cd88433b978b878478e5259` com as três skills em `0.1.2`; `CATALOGO_SKILLS=PASS` e `SYNC_GUARD=PASS`.

## Pendências técnicas não humanas
- Nenhuma local no PGA após U-PGA-15.
- `SentinelDevLima`: 12 entradas preexistentes permanecem sem portão completo; Node/typecheck e integrações externas ainda não foram homologados neste host.
- `projeto_dependencia`: 66 entradas preexistentes permanecem; lockfile continua divergente de `package.json` e build/lint/typecheck seguem não verificados neste host.
- `controle_matheus_eng_docentes`: 130 entradas preexistentes permanecem; README segue divergente da árvore atual e build/lint/typecheck/Vercel/Supabase/SUAP ainda exigem gates próprios.
- `governanca-operacional-de-ambientes@0.1.4` permanece `em_curso` por seus próprios portões de uso real/binding concreto.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento U-PGA-15.

## Competências ativas nesta unidade
- `pga-project@0.4.0`.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.
- `controle-matheus-eng-docentes-project@0.1.2`.
- `projeto-dependencia-project@0.1.2`.
- `sentinel-dev-lima-project@0.1.2`.

## Competências instaladas para unidades futuras
- As três skills de projeto acima permanecem referências canônicas no catálogo; competências adicionais só entram por lacuna de cobertura ou falha de portão comprovada.

## Falhas de portão por tipo de entrada
- `estrutura PGA`: PASS.
- `catálogo`: `CATALOGO_SKILLS=PASS accepted=83 pending=1 canonical=83`; `SYNC_GUARD=PASS`.
- `consolidação de árvore`: H02/H03/H04/H05 PASS, com referências operacionais obsoletas removidas ou reconciliadas.
- `execução Node`: NAO_VERIFICADO neste host por falha nativa já registrada; não foi usada como aprovação nem reprovação de código.

## Divergências da última reconciliação
- corrigidas: H02–H05 fechadas, skills atualizadas para 0.1.2 e catálogo sincronizado.
- pendentes de autorização: nenhuma local no PGA.

## Entradas aceitas
- 1–33.

## Próxima unidade
- PGA não possui unidade local pendente. A continuidade operacional deve auditar os artefatos preexistentes restantes nos três projetos por domínio e portão, sem promoção em massa.
