# U-PGA-08 — política de agentes temporários de serviço de rede

A fonte humana é `Q3-NETWORK-SHARING-DEFAULT`. A decisão é **private-by-default**: recursos, skills, projetos e chats permanecem privados até adesão explícita à rede. A adesão não compartilha privados automaticamente; qualquer compartilhamento adicional exige **explicit grants** por principal, grupo, tenant ou público.

## exactly two agentes de serviço

Após o join explícito, a política prevê exatamente dois papéis, ambos efêmeros e escopados:

- `network_control_agent`: `count=1`, `lifecycle=ephemeral`, `scope=network-control-only`; trata interconexão, saúde e manutenção da rede descentralizada.
- `distributed_processing_agent`: `count=1`, `lifecycle=ephemeral`, `scope=distributed-processing-only`; recebe/envia carga cognitiva da rede.

Esses papéis não autorizam acesso implícito a recursos privados e não são equivalentes a um segundo scheduler.

## Fronteira de autoridade

O PGA fixa política, autoridade, prioridade e gates. Ele **não cria runtime**, scheduler, worker, lease, grant nem preempção. A materialização executável dos agentes cabe ao owner de runtime/PGD depois de join explícito e grants válidos; a federação de rede permanece sob o owner de rede/RHGD. Assim, esta unidade fecha apenas a política PGA e não executa o trabalho operacional G4 de A05/L05.

A release `v1.0.0` permanece imutável.
