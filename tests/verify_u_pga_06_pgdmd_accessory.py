#!/usr/bin/env python3
from pathlib import Path
import json,yaml,jsonschema
ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pga-1.0/pgdmd-domain-governance.schema.json'
DATA=ROOT/'dados/pga-1.0/U-PGA-06-pgdmd-accessory.yaml'
DOC=ROOT/'docs/U-PGA-06-pgdmd-accessory.md'
def fail(x): print('PGA_PGDMD_U06=FAIL',x); raise SystemExit(2)
def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    d=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    ex=d.get('contract_example') or {}
    jsonschema.validate(ex,schema)
    if d.get('unit')!='U-PGA-06-PGDMD-ACCESSORY-MATERIALIZATION': fail('unit')
    if d.get('canonical_relation')!='PGDMD_ACCESSORY_OF_PGA': fail('relation')
    auth=ex.get('authority_boundary') or {}
    if auth.get('pga_authority_ref')!='pga://authority/domain-governance-example': fail('pga-authority-ref')
    for k in ('creates_grants','creates_runtime','creates_scheduler','creates_queue','creates_skill_runtime'):
        if auth.get(k) is not False: fail('forbidden:'+k)
    pkg=ex.get('domain_package') or {}
    if pkg.get('domain_id')!='software-delivery' or pkg.get('version')!='1.0.0': fail('package')
    kinds={x.get('kind') for x in pkg.get('normative_refs') or []}
    if kinds != {'policy','standard','process','procedure'}: fail('normative-kinds')
    if pkg.get('precedence')!=['policy://security/1','standard://iso/example','process://delivery/2','procedure://change/4']: fail('precedence')
    if pkg.get('inherits_from')!=['pgdmd://domain/base-software/1.0.0']: fail('inheritance')
    exc=pkg.get('exceptions') or []
    if len(exc)!=1 or not exc[0].get('authority_ref') or not exc[0].get('decision_ref'): fail('exception-authority')
    if ex.get('consumer_projection',{}).get('PGH')!='versioned_normative_domain_reference': fail('pgh-projection')
    if ex.get('consumer_projection',{}).get('PGD')!='policy_constraints_only_no_runtime_ownership_transfer': fail('pgd-projection')
    gates=d.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','PGDMD_PGA_RELATION','DOMAIN_PACKAGE_SCHEMA','PGA_AUTHORITY_PRESERVED','NO_GRANT_CREATION','NO_RUNTIME_CREATION','NO_SKILL_OWNERSHIP_TRANSFER','PGH_REFERENCE_PROJECTION','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    if any(gates.get(k)!='PASS' for k in required): fail('gates')
    lex=yaml.safe_load((ROOT/'lexico.yaml').read_text(encoding='utf-8'))
    terms=lex.get('termos') or {}
    if 'PGDMD' not in terms or 'NormativeDomainPackage' not in terms: fail('lexicon')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('PGDMD_ACCESSORY_OF_PGA','não cria grants','não possui scheduler','NormativeDomainPackage','repositório próprio'):
        if marker not in text: fail('doc:'+marker)
    m=yaml.safe_load((ROOT/'manifesto.yaml').read_text(encoding='utf-8'))
    if m.get('release_alvo')!='v1.0.0' or (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('release')
    print('PGA_PGDMD_U06=PASS SCHEMA=PASS AUTHORITY=PASS NO_RUNTIME=PASS')
if __name__=='__main__': main()
