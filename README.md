# PGA — Protocolo de Autogovernança

Repositório standalone inicial do PGA, materializado a partir do handoff preservado no PGH 2.0 candidato.

O PGA governa política, autoridade organizacional, prioridade estratégica e evolução governada de GovernedObject. Não possui worker, heartbeat, fila, lease ou scheduler.

## Dependência PGD reconciliada — H01-R2

A construção/conciliação auxiliar do PGA ocorre somente depois dos gates `PGD_AUXILIAR_RECONCILIATION=PASS` e `PGD_IDENTITY_H01_R2=PASS`. A referência PGD desta emenda é `366388d8c52f696d81b7277075b87e8fc144ca1b`.

`debianlima/pgd` permanece a fonte do protocolo PGD; `debianlima/pgh-distributed-session-control-plane` é a implementação canônica de execução. Essa relação não transfere scheduler, workers, leases ou estado runtime para o PGA e não amplia sua autoridade.

Origem normativa: debianlima/protocolo-governanca-heterogenea@a68ba9b460bd1d2050d57873fdc1c648732ece07, documento docs/pga/U-PGA-01-msgcd-u20-handoff.md.

## Release 1.0

PGA 1.0 é homologado somente dentro da tríade PGH 2.0 + PGD 1.0 + PGA 1.0; a evidência e os gates locais vivem em `dados/pga-1.0/` e `tests/verify_release_1_0.py`.
