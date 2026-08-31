#!/usr/bin/env python3
from pathlib import Path
import json, yaml, jsonschema
ROOT=Path(__file__).resolve().parents[1]
def fail(x): print('PGA_RELEASE_1_0=FAIL',x); raise SystemExit(2)
S=json.loads((ROOT/'contratos/pga-1.0/release.schema.json').read_text(encoding='utf-8'))
E=yaml.safe_load((ROOT/'dados/pga-1.0/U-PGA-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(E,S)
handoff=(ROOT/'docs/U-PGA-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
required=['POLICY_SNAPSHOT_IMMUTABLE','AUTHORITY_PROVENANCE_COMPLETE','GOVERNED_OBJECT_IDENTITY_PRESERVED','NO_SILENT_POLICY_MUTATION','NO_SELF_AUTHORITY_EXPANSION','EVOLUTION_PLAN_APPROVED_BEFORE_RESULTS','GATES_FROZEN_BEFORE_VALIDATION','ROLLBACK_OR_DEPRECATION_DEFINED','CULTURAL_CONTEXT_NE_EXECUTABLE_AUTHORITY','STRATEGIC_PRIORITY_NE_RUNTIME_SCHEDULER']
if 'Protocolo de Autogovernança' not in handoff: fail('canonical-name')
if any(g not in handoff for g in required): fail('handoff-gates')
if set(E['gates'])!=set(required) or any(E['gates'][g]!='PASS' for g in required): fail('gate-accounting')
if (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('version')
m=yaml.safe_load((ROOT/'manifesto.yaml').read_text(encoding='utf-8'))
if m.get('release_alvo')!='v1.0.0' or m.get('versao_contrato')!=3: fail('manifest-release')
print('PGA_RELEASE_1_0=PASS GATES=10/10')
