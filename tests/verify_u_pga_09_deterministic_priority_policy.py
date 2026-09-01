#!/usr/bin/env python3
from pathlib import Path
import json
import yaml
import jsonschema

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pga-1.0/deterministic-priority-policy.schema.json'
DATA=ROOT/'dados/pga-1.0/U-PGA-09-deterministic-priority-policy.yaml'
DOC=ROOT/'docs/U-PGA-09-deterministic-priority-policy.md'
SOURCE_COMMIT='f6c47aa104dbba0359afd69cff0fd58889c5b348'
SOURCE_SHA256='44acaa08e273ec34a118ab092dc9b749ddf2e5d62d3121e8cfd4c96d6b83eb67'
EXPECTED=[
    ('P0_GOVERNED',0,False,'human_or_pga_only'),
    ('P1_HIGH',1,False,'governed_project_policy'),
    ('P2_NORMAL',2,False,'governed_project_policy'),
    ('P3_LOW',3,False,'governed_project_policy'),
    ('P4_BACKGROUND',4,False,'governed_project_policy'),
]

def fail(reason):
    print('PGA_DETERMINISTIC_PRIORITY_U09=FAIL',reason)
    raise SystemExit(2)

def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    data=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    jsonschema.validate(data,schema)
    if data.get('schema')!='pga-deterministic-priority-policy/1': fail('schema')
    if data.get('unit')!='U-PGA-09-DETERMINISTIC-PRIORITY-POLICY': fail('unit')
    src=data.get('source') or {}
    if src.get('repository')!='debianlima/protocolo-governanca-heterogenea': fail('source-repo')
    if src.get('commit')!=SOURCE_COMMIT: fail('source-commit')
    if src.get('path')!='dados/pgh-2.0/U268-deterministic-election-fabric.yaml': fail('source-path')
    if src.get('sha256')!=SOURCE_SHA256: fail('source-sha')
    if src.get('contract_id')!='CT-PGH2-DETERMINISTIC-ELECTION-FABRIC@1.0.0': fail('source-contract')
    if src.get('decision_id')!='HUMAN-U268-DETERMINISTIC-ELECTION-FABRIC-20260901': fail('decision')
    if src.get('authority')!='human-operator': fail('decision-authority')
    bands=data.get('priority_bands') or []
    got=[(x.get('id'),x.get('rank'),x.get('automatic_preemption'),x.get('set_by')) for x in bands]
    if got!=EXPECTED: fail('priority-bands')
    if sum(1 for x in bands if x.get('default') is True)!=1 or next(x for x in bands if x.get('default') is True).get('id')!='P2_NORMAL': fail('default-band')
    policy=data.get('policy') or {}
    if policy.get('human_reserved_band')!='P0_GOVERNED': fail('human-reserved-band')
    if policy.get('priority_grants_authority') is not False: fail('priority-must-not-grant-authority')
    if policy.get('priority_can_bypass_locks_leases_fences') is not False: fail('priority-must-not-bypass-fences')
    if policy.get('priority_can_preempt_running_work') is not False: fail('priority-must-not-preempt')
    if policy.get('runtime_owner')!='PGD/runtime-owner': fail('runtime-owner')
    queue=data.get('queue_policy') or {}
    if queue.get('strict_fifo_contract_preserved') is not True: fail('fifo-preservation')
    if queue.get('priority_applies_only_when_queue_contract_allows') is not True: fail('queue-opt-in')
    boundary=data.get('authority_boundary') or {}
    if boundary.get('PGA')!='policy_authority_priority_gates_governed_evolution': fail('pga-boundary')
    for k in ('creates_scheduler','creates_worker','creates_lease','creates_runtime_state','creates_grant','performs_preemption'):
        if boundary.get(k) is not False: fail('authority-boundary:'+k)
    if boundary.get('L1_L5_authority_preserved') is not True: fail('authority-levels')
    release=data.get('release') or {}
    if release!={'version':'1.0.0','tag':'v1.0.0','immutable':True}: fail('release-immutability')
    gates=data.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','SOURCE_PIN','FIVE_PRIORITY_BANDS','HUMAN_RESERVED_P0','AUTHORITY_PRIORITY_SEPARATION','NO_AUTOMATIC_PREEMPTION','STRICT_FIFO_PRESERVED','NO_PGA_RUNTIME','RELEASE_IMMUTABILITY']
    for k in required:
        if gates.get(k)!='PASS': fail('gate:'+k)
    for k in ('RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES'):
        if gates.get(k) not in ('PENDING','PASS'): fail('gate:'+k)
    if (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('version')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('P0_GOVERNED','P1_HIGH','P2_NORMAL','P3_LOW','P4_BACKGROUND','human-reserved','L1–L5','strict FIFO','não cria scheduler','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    print('PGA_DETERMINISTIC_PRIORITY_U09=PASS BANDS=5 HUMAN_RESERVED=P0 AUTHORITY_SEPARATION=PASS NO_PREEMPTION=PASS NO_PGA_RUNTIME=PASS')

if __name__=='__main__': main()
