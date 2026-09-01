# U-PGA-09 — deterministic priority policy

Esta unidade materializa no PGA a parcela normativa do contrato PGH 2.0 `CT-PGH2-DETERMINISTIC-ELECTION-FABRIC@1.0.0`. A fonte é o artefato U268 pinado por repositório, commit, caminho e SHA-256; nenhuma linha candidata de skill é promovida por esta unidade.

## Cinco bandas

A política possui exatamente `P0_GOVERNED`, `P1_HIGH`, `P2_NORMAL`, `P3_LOW` e `P4_BACKGROUND`. `P2_NORMAL` é o default. A banda **human-reserved** é `P0_GOVERNED`: somente decisão humana ou política PGA autorizada pode defini-la. As demais bandas podem vir de política governada do projeto.

Prioridade e autoridade são eixos diferentes. A hierarquia **L1–L5** de autoridade permanece intacta: prioridade nunca concede autoridade, nunca ignora lock/lease/fence/shared-work/human block e nunca autoriza preempção automática.

## Fronteira de runtime

PGA descreve política, autoridade, prioridade, gates e evolução. PGA **não cria scheduler**, worker, lease, grant nem estado runtime e não executa preempção. A materialização operacional pertence ao owner de runtime/PGD e precisa aplicar os próprios fences/CAS/leases.

Em filas, a prioridade só pode participar quando o contrato da fila declarar essa capacidade. Contrato **strict FIFO** continua FIFO e não é reordenado por P0–P4.

## Compatibilidade e release

Esta reconciliação é pós-release e não move nem reescreve `v1.0.0`. O objetivo é disponibilizar uma política normativa consumível pelo runtime e pelo fecho PGH 2.0 sem criar segunda autoridade.

Os gates `RECONCILIATION_CLOSURE` e `DEPENDENCY_REFERENCES` só avançam para PASS depois da regressão PGA e da reconciliação do estado remoto.
