#!/usr/bin/env python3
from pathlib import Path
import json
import yaml
import jsonschema

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pga-1.0/network-service-agents.schema.json'
DATA=ROOT/'dados/pga-1.0/U-PGA-08-network-service-agents.yaml'
DOC=ROOT/'docs/U-PGA-08-network-service-agents.md'
SOURCE_COMMIT='f5047f72914c6634982df30c8ce0f8747af5cfb3'
SOURCE_SHA256='cc79afcd94345752c0e0b5cf9883c48a5956f09a91bcde990fccb941f4ff903b'

def fail(reason):
    print('PGA_NETWORK_SERVICE_AGENTS_U08=FAIL',reason)
    raise SystemExit(2)

def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    data=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    jsonschema.validate(data,schema)
    if data.get('unit')!='U-PGA-08-NETWORK-SERVICE-AGENTS': fail('unit')
    src=data.get('source') or {}
    if src.get('decision_id')!='Q3-NETWORK-SHARING-DEFAULT': fail('decision-id')
    if src.get('repository')!='debianlima/pgh-distributed-session-control-plane': fail('source-repo')
    if src.get('commit')!=SOURCE_COMMIT or src.get('path')!='config/3.0/governance-decisions.yaml' or src.get('sha256')!=SOURCE_SHA256: fail('source-pin')
    if src.get('selected')!='PRIVATE_PLUS_TWO_NETWORK_SERVICE_AGENTS' or src.get('authority')!='human-operator': fail('source-authority')
    policy=data.get('policy') or {}
    if policy.get('default_scope')!='private': fail('default-scope')
    if policy.get('network_join')!='explicit-only': fail('network-join')
    if policy.get('private_resources_shared_implicitly') is not False: fail('implicit-private-sharing')
    if policy.get('additional_sharing')!='explicit-grants-by-principal-group-tenant-public': fail('additional-sharing')
    agents=data.get('network_service_agents') or []
    if len(agents)!=2: fail('exactly-two-agents')
    by={x.get('role'):x for x in agents}
    if set(by)!={'network_control_agent','distributed_processing_agent'}: fail('roles')
    n=by['network_control_agent']; d=by['distributed_processing_agent']
    if (n.get('count'),n.get('lifecycle'),n.get('scope'))!=(1,'ephemeral','network-control-only'): fail('network-control-shape')
    if (d.get('count'),d.get('lifecycle'),d.get('scope'))!=(1,'ephemeral','distributed-processing-only'): fail('distributed-processing-shape')
    if n.get('purpose')!='interconexao_saude_manutencao_rede_descentralizada': fail('network-control-purpose')
    if d.get('purpose')!='receber_enviar_carga_cognitiva_rede': fail('distributed-processing-purpose')
    if any(x.get('created_by_pga') is not False for x in agents): fail('PGA-must-not-create-agents')
    if any(x.get('runtime_owner')!='PGD/runtime-owner' for x in agents): fail('runtime-owner')
    if any(x.get('network_join_required') is not True for x in agents): fail('join-required')
    boundary=data.get('authority_boundary') or {}
    for k in ('creates_scheduler','creates_worker','creates_lease','creates_runtime_state','creates_grant','shares_private_resource_implicitly','preempts_existing_work'):
        if boundary.get(k) is not False: fail('authority-boundary:'+k)
    if boundary.get('PGA')!='policy_authority_priority_gates_governed_evolution': fail('pga-boundary')
    if boundary.get('runtime_execution')!='delegated_to_runtime_owner_after_explicit_join_and_grants': fail('runtime-boundary')
    own=data.get('ownership') or {}
    if own.get('policy_owner')!='PGA' or own.get('runtime_owner')!='PGD/runtime-owner': fail('ownership')
    if own.get('network_federation_owner')!='RHGD/network-owner': fail('network-owner')
    if own.get('scheduler_duplication') is not False: fail('scheduler-duplication')
    gates=data.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','SOURCE_PIN','PRIVATE_BY_DEFAULT','EXPLICIT_JOIN','EXACTLY_TWO_AGENTS','EPHEMERAL_LIFECYCLE','SCOPE_ISOLATION','NO_IMPLICIT_PRIVATE_SHARING','AUTHORITY_BOUNDARY','NO_PGA_RUNTIME','RELEASE_IMMUTABILITY']
    for k in required:
        if gates.get(k)!='PASS': fail('gate:'+k)
    for k in ('RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES'):
        if gates.get(k) not in ('PENDING','PASS'): fail('gate:'+k)
    if (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('release-version')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('Q3-NETWORK-SHARING-DEFAULT','private-by-default','network_control_agent','distributed_processing_agent','exactly two','explicit grants','não cria runtime','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    print('PGA_NETWORK_SERVICE_AGENTS_U08=PASS DEFAULT=PRIVATE JOIN=EXPLICIT AGENTS=2 EPHEMERAL=PASS NO_PGA_RUNTIME=PASS')

if __name__=='__main__': main()
