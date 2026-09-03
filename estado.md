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
- H01–H05 — fechadas em 2026-09-02; H02/H03/H04/H05 executadas pela opção A aprovada pelo usuário.

## Decisões humanas pendentes
- Nenhuma local no PGA.
- Externa ao PGA: H06 em `projeto_dependencia` decide a consolidação dos serviços de anexos `lib/processAttachments.ts` e `lib/supabase/attachments.ts`; nenhuma remoção foi inferida.

## Decisões fechadas nesta emenda
- `SentinelDevLima` avançou para `sentinel-dev-lima-project@0.1.3` em `8dd25727febf99a1eeb1b2469c896e0029ed046f`: README arquitetural aceito; typecheck ampliado para `src` + `api`; webhook corrigido para raw-body/HMAC antes de JSON parse; embedding reconciliado em Gemini/768; 11 de 22 entradas aceitas e 11 `preexistente`.
- `projeto_dependencia` avançou para `projeto-dependencia-project@0.1.3` em `aa0129a00213e4e7142fa74d4aa63f4566eeaef2`: README e `ORIENTACOES_REUSO.md` aceitos; store principal confirmado como Zustand/localStorage iniciado por mocks; Supabase confirmado como integração parcial de anexos; 12 de 76 entradas aceitas e 64 `preexistente`; H06 permaneceu pendente.
- `controle_matheus_eng_docentes` permanece em `controle-matheus-eng-docentes-project@0.1.2`, commit verificável `d8985f00cef1be7b1dc4709df410dc25e7cd9fea`: 11 de 141 entradas atuais aceitas e 130 `preexistente`; H04/H05 fechadas.
- Catálogo global reconciliado em `708922c00bcb84e8ee5f2f5d0a2af617af209652`; `CATALOGO_SKILLS=PASS accepted=83 pending=1 canonical=83` e `SYNC_GUARD=PASS`.

## Pendências técnicas não humanas
- Nenhuma local no PGA após U-PGA-17; o rastro incompleto da auditoria Sentinel U-PGA-16 foi fechado prospectivamente como `ABORTED_INCOMPLETE_HISTORICAL_NO_PROMOTION`, sem promover estado externo.
- `SentinelDevLima`: 11 entradas `preexistente`; typecheck/runtime Node, execução GitHub Actions e migrations PostgreSQL/pgvector ainda não homologados no ambiente disponível.
- `projeto_dependencia`: 64 entradas `preexistente`; lockfile diverge de `package.json`, store geral continua mock/localStorage e Supabase/RLS/sessão real exigem gate externo; U-DEPENDENCIA-03 preserva `TELEMETRY_ORDER=FAIL_RECORDED` porque leitura/clone read-only precederam o início instrumentado.
- `controle_matheus_eng_docentes`: 130 entradas `preexistente`; README/build/Vercel/Supabase/SUAP ainda exigem reconciliação/gates próprios.
- `governanca-operacional-de-ambientes@0.1.4` permanece `em_curso` por seus próprios portões de uso real/binding concreto.
- O filesystem do host continua sob forte pressão de espaço; falhas `ENOSPC` foram observadas durante commit temporário do EduMonitor, sem perda de dados publicados.

## Trabalho compartilhado
- ponteiro: `manifesto.yaml.trabalho_compartilhado` — vazio após fechamento U-PGA-17.

## Competências ativas nesta unidade
- `pga-project@0.4.0`.
- `desenvolvedor-de-software@15`.
- `github-incremental-reconciliation@7`.
- `governanca-ontologica-de-skills@1.0.5`.
- `telemetry-data-visualization@2`.
- `controle-matheus-eng-docentes-project@0.1.2`.
- `projeto-dependencia-project@0.1.3`.
- `sentinel-dev-lima-project@0.1.3`.

## Competências instaladas para unidades futuras
- As três skills acima permanecem referências canônicas no catálogo; competências adicionais só entram por lacuna real de cobertura ou falha de portão comprovada.

## Falhas de portão por tipo de entrada
- `estrutura PGA`: PASS.
- `release PGA 1.0`: PASS; release não foi reaberta.
- `catálogo`: `CATALOGO_SKILLS=PASS accepted=83 pending=1 canonical=83`; `SYNC_GUARD=PASS`.
- `Sentinel`: documentação/estrutura de webhook/typecheck/embedding reconciliadas; executores externos permanecem `NAO_VERIFICADO`.
- `EduMonitor`: documentação/reuso PASS; arquitetura store/mock e Supabase parcial classificada; H06 pendente; `TELEMETRY_ORDER=FAIL_RECORDED` preservado.
- `Controle Docente`: H04/H05 permanecem fechadas; demais integrações não foram promovidas por leitura.

## Divergências da última reconciliação
- corrigidas: snapshot central atualizado de skills `0.1.2` para Sentinel/EduMonitor `0.1.3`, contagens reconciliadas e H06 registrada como fronteira humana externa.
- pendentes de autorização: nenhuma local no PGA; H06 apenas no contexto EduMonitor.

## Entradas aceitas
- 1–33.

## Próxima unidade
- PGA não possui unidade local pendente. Continuidade recomendada: executar gates externos/Node/PostgreSQL dos projetos e resolver H06 quando houver decisão humana, sem promoção em massa.
## U-PGA-17 — reconciliação canônica de telemetria incompleta
- base canônica GitHub observada: `b8ee38c1a60e43c4bab61ec21b9c9f302418c1bc`, a mesma identidade congelada pelo fixed point PGH U284.
- `U-PGA-16-EXTERNAL-AUDIT-SNAPSHOT-RECONCILIATION` permanece histórico com início/fim próprios e não é reexecutado.
- `U-PGA-16-SENTINEL-WORKFLOW-WEBHOOK-MIGRATION-AUDIT` possuía somente `telemetria_inicio`; ausência de evidência de conclusão foi preservada e o evento foi encerrado agora como `ABORTED_INCOMPLETE_HISTORICAL_NO_PROMOTION`.
- os dados externos de Sentinel/EduMonitor/Controle Docente presentes no snapshot `b8ee38c1...` são observações históricas daquele corte, não autoridade viva nem promoção automática.
- fronteiras PGA/PGDMD permanecem inalteradas: `PGDMD_ACCESSORY_OF_PGA`, sem scheduler/runtime/grants próprios; Project-Skill permanece `pga-project@0.4.0`.
- `DELTA_INVENTORY=PASS`; `LEARNING_PRESERVED=PASS`; nenhum force-push e nenhuma tag histórica alterada.
