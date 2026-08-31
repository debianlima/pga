# U-PGA-02 — Homologação PGA 1.0

PGA 1.0 formaliza política, autoridade, prioridade estratégica e evolução governada. Não possui scheduler, worker, heartbeat, lease ou estado runtime vivo; esses pertencem ao PGD. O PGH referencia snapshots PGA e aplica autorização semântica.

## Invariantes

- `PolicySnapshot` é imutável e possui proveniência de autoridade;
- não há mutação silenciosa nem autoexpansão de autoridade;
- `GovernedObject` preserva identidade entre versões;
- plano aprovado precede resultados e os gates são congelados antes da validação;
- rollback ou depreciação é obrigatório;
- contexto cultural não equivale a autoridade executável;
- prioridade estratégica PGA não equivale ao scheduler runtime PGD.

## Dependência da tríade

Esta release só é publicada como parte da homologação T-019/T-020 com PGH 2.0 e PGD 1.0. O tag final é criado somente depois do gate conjunto.
