#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'dados/pga-1.0/U-PGA-05-core-system-context-reconciliation.yaml'
DOC=ROOT/'docs/U-PGA-05-core-system-context-reconciliation.md'
def fail(x): print('PGA_CORE_SYSTEM_CONTEXT_U05=FAIL',x); raise SystemExit(2)
def main():
    if not DATA.exists(): fail('missing-data')
    if not DOC.exists(): fail('missing-doc')
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    if d.get('unit')!='U-PGA-05-CORE-SYSTEM-CONTEXT-RECONCILIATION': fail('unit')
    refs=d.get('refs') or {}
    expected={
      'pga_base':'17ace9afe02af7dcb5ec14df7843ea1a39d7aebb',
      'pgd_u07':'743567ba2b4a5e6db204a9d508b7997a1b760326',
      'pgh_main':'edbfefa6ef4d0bd2e6581e6781e82e167c583b96',
      'runtime':'f033b622ce6a3e59f4a3d2d29f903b3f4a267b32',
      'system_vision_catalog':'c1f208fb3470eeced0fd3da96d948efa196cb38c'}
    for k,v in expected.items():
        if refs.get(k)!=v: fail('ref:'+k)
    if d.get('system_vision_id')!='PGH-SUITE-SYSTEM-VISION-1': fail('vision')
    a=d.get('authority') or {}
    if a.get('PGA')!='policy_authority_priority_gates_governed_evolution': fail('pga-authority')
    if a.get('PGDMD')!='accessory_domain_governance_under_PGA': fail('pgdmd-relation')
    if a.get('PGH')!='knowledge_contracts_skills_semantics_evidence': fail('pgh-authority')
    if a.get('PGD')!='tasks_messages_queues_leases_scheduler_runtime_state': fail('pgd-authority')
    if a.get('RHGD')!='federation_without_second_scheduler': fail('rhgd-authority')
    runtime=d.get('runtime_boundary') or {}
    for k in ('scheduler','worker','heartbeat','lease','runtime_state'):
        if runtime.get(k) is not False: fail('pga-runtime:'+k)
    if runtime.get('pgd_reference')!='743567ba2b4a5e6db204a9d508b7997a1b760326': fail('pgd-runtime-ref')
    pgdmd=d.get('pgdmd') or {}
    if pgdmd.get('canonical_relation')!='PGDMD_ACCESSORY_OF_PGA' or pgdmd.get('creates_grants') is not False or pgdmd.get('creates_runtime') is not False: fail('pgdmd-boundary')
    hist=d.get('historical_auxiliary_dependency') or {}
    if hist.get('head')!='366388d8c52f696d81b7277075b87e8fc144ca1b' or hist.get('preserved_as_historical_enablement_evidence') is not True: fail('historical-pgd-dep')
    rel=d.get('release') or {}
    if rel.get('version')!='1.0.0' or rel.get('tag')!='v1.0.0' or rel.get('tag_commit')!='0985ea0052436b07f9e6029df42bbafd68fda024' or rel.get('immutable') is not True: fail('release')
    if d.get('project_skill_change_required')!='NO': fail('skill-bump')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','PGD_U07_DEPENDENCY','UPSTREAM_CORE_SAFE_POINT','U250_OPERATIONAL_RECONCILIATION','U255_SYSTEM_VISION','PGDMD_PGA_RELATION','AUTHORITY_BOUNDARY','NO_PGA_RUNTIME','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('PGDMD_ACCESSORY_OF_PGA','743567ba2b4a5e6db204a9d508b7997a1b760326','PGH-SUITE-SYSTEM-VISION-1','PGA continua sem scheduler','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    print('PGA_CORE_SYSTEM_CONTEXT_U05=PASS PGD_U07=PASS PGDMD=PASS NO_PGA_RUNTIME=PASS RELEASE_IMMUTABLE=PASS')
if __name__=='__main__': main()
