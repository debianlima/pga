# U-PGA-06 — PGDMD como protocolo acessório do PGA

## Decisão materializada

A relação canônica é `PGDMD_ACCESSORY_OF_PGA`. O PGDMD especializa governança de domínio, enquanto PGA permanece a autoridade geral de política, autoridade, prioridade e evolução governada.

Nesta unidade PGDMD nasce como **contrato/módulo acessório dentro do PGA**. Não é criado repositório próprio, lifecycle independente, grant system ou runtime.

## NormativeDomainPackage

O objeto versionado `NormativeDomainPackage` referencia:

- modelo normativo do domínio;
- políticas;
- padrões/standards;
- processos;
- procedimentos;
- ordem explícita de precedência;
- herança de pacotes/domínios superiores;
- exceções sempre ligadas a `authority_ref` e `decision_ref`.

O pacote é uma referência normativa governada. Ele não vira conhecimento homologado por si: PGH consome a referência versionada e a projeta para contexto técnico/evidência conforme seus gates.

## Fronteiras

PGDMD **não cria grants** e não expande autoridade além do PGA. PGDMD **não possui scheduler**, fila, worker, lease ou runtime. Tarefas e execução continuam no PGD. Skills/conhecimento/ontologia de conhecimento permanecem no PGH. RHGD continua responsável apenas por federação conforme contratos próprios.

A projeção para PGD contém restrições/política aplicável, nunca transferência de ownership de runtime.

## Materialização futura

Um **repositório próprio** para PGDMD só pode ser extraído se surgir estado mutável, API e ciclo de evolução próprios que justifiquem lifecycle separado. Este contrato não cria essa condição automaticamente.

## Release

PGA continua em `1.0.0`, tag histórica `v1.0.0` imutável. A skill `pga-project@0.1.0` já contém a regra de que PGA governa política/autoridade e não possui runtime vivo; não há bump artificial de skill.
